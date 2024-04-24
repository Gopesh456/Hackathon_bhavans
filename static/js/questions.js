// let editor = document.querySelector("#editor");
let codeEditor = ace.edit("editor");

const submitBtn = document.querySelector(".submit-btn");
const question = document.querySelector("p");
const textArea = document.querySelector("#textarea");
const runBtn = document.querySelector(".run-btn");
const questionNo = parseInt(document.querySelector(".question_no").textContent);
let editorLib = {
  init() {
    // Configure Ace

    // Theme
    codeEditor.setTheme("ace/theme/nord_dark");

    // Set language
    codeEditor.session.setMode("ace/mode/python");
    codeEditor.renderer;
    // Set Options
    codeEditor.setOptions({
      enableBasicAutocompletion: true,
      enableLiveAutocompletion: true,
      autoScrollEditorIntoView: true,
      copyWithEmptySelection: true,
    });
    codeEditor.session.setUseWrapMode(true);
    // Set Default Code
    def_code = "#Dont edit this line of code\n";
    if (questionNo == 1) {
      codeEditor.setValue(def_code + "input_data = eval(input())");
    }
  },
};

editorLib.init();

// runBtn.addEventListener('click',()=>{
// const userCode = codeEditor.getValue();
//     console.log(userCode)
//     textArea.textContent = userCode
// })
