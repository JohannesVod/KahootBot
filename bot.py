from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys
import argparse

handled_questions = set()

def cleanStr(st):
    return str(st.encode(sys.stdout.encoding, errors='replace'))

def score(str1, str2, m, n):
    # edit distance calculation
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j    # Min. operations = j
            elif j == 0:
                dp[i][j] = i    # Min. operations = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1])    # Replace
    print(str1, str2, dp[m][n])
    return dp[m][n]

def HandleQuestion(question, driver, solutions):
    if question in handled_questions:
        return
    sols = solutions[len(handled_questions)]
    handled_questions.add(question)
    choice_elements = driver.find_elements(By.XPATH, '//button[contains(@class, "choice__Choice-sc-ym3b8f-4")]')
    choice_to_score = [None for _ in range(len(choice_elements))]
    for i, choice_element in enumerate(choice_elements):
        this_ans = cleanStr(choice_element.find_element(By.XPATH, './/div[contains(@class, "choice__ChoiceText-sc-ym3b8f-5")]').text)
        print(this_ans)
        choice_to_score[i] = min([score(this_ans, sol, len(this_ans), len(sol)) for sol in sols])
    choices_sorted = [(choice_to_score[i], i) for i in range(len(choice_to_score))]
    choices_sorted.sort()
    answers = [choices_sorted[i][1] for i in range(len(sols))]
    
    for el in answers:
        choice_elements[el].click()
    
    print(f"clicking buttons: f{answers}")

    if len(sols) > 1:
        print("submit mult-question")
        submit_b = driver.find_element(By.XPATH, '//button[contains(@class, "button__Button-sc-vzgdbz-0")]')
        submit_b.click()

def main():
    # Parsing command-line arguments
    parser = argparse.ArgumentParser(description='Quiz Automation Script')
    parser.add_argument('quiz_file', type=str, help='Path to the quiz file')
    parser.add_argument('--sleep', type=int, default=1000, help='Milliseconds to sleep between iterations (default: 1000)')
    args = parser.parse_args()

    # Open the file
    with open(args.quiz_file, 'r') as file:
        lines = file.readlines()
        quiz_title = lines[0].strip("\n").strip('#').strip()
        print(f"using quiz: {quiz_title}")
        solutions = []
        for l in lines[1:]:
            splt = l.split("|")
            sol = []
            for spl in splt:
                spl = cleanStr(spl.strip().replace("\n", ""))
                sol.append(spl)
            solutions.append(sol)

    try:
        driver = webdriver.Chrome()
        driver.get("https://kahoot.it")  # Specify the full URL of the Kahoot game
        while True:
            try:
                question_element = driver.find_element(By.XPATH, '//span[contains(@class, "question-title__Title-sc-12qj0yr-1")]')
                question_text = cleanStr(question_element.text)
                try:
                    HandleQuestion(question_text, driver, solutions)
                except Exception as ex:
                    print(f"Error handling question: {ex}")
            except:
                pass
            time.sleep(args.sleep / 1000)  # Convert milliseconds to seconds
    except KeyboardInterrupt:
        print("Script interrupted by user.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()