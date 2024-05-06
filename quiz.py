from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    driver = webdriver.Chrome()
    driver.get("https://kahoot.it")  # Specify the full URL of the Kahoot game

    while True:
        try:
            question_element = driver.find_element(By.XPATH, '//span[@class="question-title__Title-sc-12qj0yr-1 iVjdnd"]')
            question_text = question_element.text
            print("Question:", question_text)
        except:
            print("Question not found")
            time.sleep(1)

except KeyboardInterrupt:
    print("Script interrupted by user.")
finally:
    driver.quit()
