from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def stress_test_singular(ip: str, question_no: int = 1, headless: bool = False):
    options = webdriver.FirefoxOptions()
    if headless:
        options.add_argument("--headless")
    driver = webdriver.Firefox(options=options, keep_alive=True)
    driver.get(f"http://{ip}:8000/login/")
    try:
        WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, 'user-el'))  # Replace with actual element ID
            )
    except:
        pass
    username_input = driver.find_element(By.ID, "user-el")
    username_input.send_keys("Yash")
    password_input = driver.find_element(By.ID, "pass-el")
    password_input.send_keys("Bhavans@123")
    driver.find_element(By.CLASS_NAME, "button-52").click()

    try:
        WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'custom-btn'))  # Replace with actual element ID
            )
    except:
        pass

    question_format_url = f"http://{ip}:8000/question/**/"

    # quetion 1:
    question = question_format_url.replace("**", str(question_no))
    driver.get(question)
    try:
        WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'ace_content'))  # Replace with actual element ID
            )
    except:
        pass
    textbox = driver.find_element(By.CLASS_NAME, "ace_content")
    textbox.click()
    textbox = driver.find_element(By.CLASS_NAME, "ace_text-input")
    textbox.send_keys("print('HELLO WORLD')")

    driver.execute_script('sendResult();')
    
    driver.quit()