import subprocess

correct_outputs: dict = {
    1.1: "1\n2\n3\n4\n",
    1.2: "4\n1\n2\n5\n",
    1.3: "7\n8\n6\n",
    2.1: 'olleh\n',
    2.2: 'nohtyp\n',
    2.3: 'olleh nohtyp\n',
}

illegal_modules = [''] # Empty list allows all modules, [''] disables all modules
allowed_modules = ['sys'] # NEVER SET IT TO ['']

class PythonChecker:
    
    def __init__(self, debug: bool = False):
      self._debug = debug
      self.last_output = None
    
    def run_python_file(self, file_path: str, args: list = []):
        '''
        Run the python file at given file_path with specified args and returns the output. Does not check for malice
        '''
        try:
            output = subprocess.check_output(['python', file_path] + args, stderr=subprocess.STDOUT, universal_newlines=True)
            if self._debug: print(f"Output generated from {file_path} is:\n\n", output, sep = "")
            return output
        except subprocess.CalledProcessError as e:
            if self._debug: print(f"Error generated from {file_path} is:\n\n", e.output, sep = "")
            return e.output
    

    def is_correct_output(self, team_code, question_index: int, program_code: str, args: list = []):
        '''
        (UNNECESSARY FUNCTION)
        '''
        file_path = f'team_codes/{team_code}-{question_index}.py'
        if self._debug:
            print("--------------- Team code:", team_code, question_index, "---------------")
            print("Trying to write to file: ", file_path)
        with open(file_path, 'w') as f:
            f.write(program_code)
        try:
            output = self.run_python_file(file_path, args)
            return output == self.get_correct_output(question_index)
        except Exception as e:
            if self._debug: print(f"Error occured while running {file_path}:\n", e)
            return False

    def get_correct_output(self, question_index: int):
        '''
        Returns the correct output for th given question index
        '''
        return correct_outputs[question_index]

    def check_python_file(self, question_index: int, file_path: str, args = []) -> bool:
        '''
        Checks whether the given file returns the correct output or not.
        Order of events:
            1. Checking Malice
            2. Trying to run the python file
                i. if executed correctly, returns whether the output was correct or wrong
                ii. if python file fails to execute, returns false
        '''
        if self.is_not_malice(file_path):
            try:
                output = self.run_python_file(file_path, args)
                return output == self.get_correct_output(question_index)
            except Exception as e:
                if self._debug: print(f"Error occurred while running {file_path}:\n", e)
                return False
        else:
            return False
    
    def is_not_malice(self, file_path: str) -> bool:
        '''
        Checks if the file contains illegal modules
        '''
        try:
            with open(file_path) as code:
                code_data = code.read()
                for module in allowed_modules:
                    code_data = code_data.replace(f"import {module}", "", 1)
                code_data = code_data.replace("input_data = eval(sys.argv[1])", "", 1)
                code_data = code_data.replace("del sys", "", 1)
        except OSError as e:
            if self._debug: print("Error while opening file when checking malice: ", e)
            return True # Technically True as file might not exist
        for module in illegal_modules:
            if f"import {module}" in code_data:
                if self._debug:
                    print(code_data)
                return False # Malice detected
            elif f"from {module}" in code_data:
                return False # Malice detected
        return True # Safe
    
    def get_output(self, file_path: str, user_input: list) -> str:
        '''
        Run the python file at given file_path with specified args and returns the output. Checks for malice as well.
        '''
        if self.is_not_malice(file_path):
            return self.run_python_file(file_path, user_input)
        else:
            return "You can not use any modules in this section of the hackathon."
        
        
    
# For testing purposes
# Mock Usage in Final Code
# from python.python_checker import PythonChecker
if __name__ == "__main__":
    TEAM_CODE_MOCK = "AAAAAA"
    PyChecker = PythonChecker(True)
    print(PyChecker.check_python_file(1.2,'test.py'))