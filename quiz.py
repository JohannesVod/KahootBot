from selenium import webdriver
from selenium.webdriver.common.by import By
import time

solutions = {}
handled_questions = set()

def HandleQuestion(question, driver):
    #if question not in solutions:
    #    return
    #sol = solutions[question]
    print("Question:", question_text)
    choice_elements = driver.find_elements(By.XPATH, '//button[contains(@class, "choice__Choice-sc-ym3b8f-4")]')
    print(choice_elements)
    # Perform actions on the button element here, such as clicking it
    # button_element.click()
    

try:
    driver = webdriver.Chrome()
    driver.get("https://kahoot.it")  # Specify the full URL of the Kahoot game

    while True:
        try:
            question_element = driver.find_element(By.XPATH, '//span[contains(@class, "question-title__Title-sc-12qj0yr-1")]')
            question_text = question_element.text
            HandleQuestion(question_text, driver)
        except:
            print("Question not found")
        time.sleep(1)

except KeyboardInterrupt:
    print("Script interrupted by user.")
finally:
    driver.quit()
