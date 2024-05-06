# Kahoot Bot

## Description
This script automates participation in Kahoot quizzes by providing answers to questions based on a predefined solution set. It utilizes Selenium WebDriver to interact with the Kahoot website.

## Requirements
- Python 3.x
- selenium

## Installation
1. Install Python 3.x from [here](https://www.python.org/downloads/).
2. Install Selenium WebDriver using pip:
    ```
    pip install selenium
    ```

## Usage
1. Write your quiz questions and solutions in a text file in the following format:
    ```
    # Quiz Title #
    first Solution Question 1 | second Solution Question 1 | third ...
    first Solution Question 2 | second Solution Question 2 | third ...
    ...
    ```
    If there is only one correct answer just write it down. If it is a True/False question, just write "True" or "False"
    Save the file with a `.txt` extension.

2. Run the script with the following command:
    ```
    python kahoot_bot.py <quiz_file> [--sleep <milliseconds>]
    ```
    - `<quiz_file>`: Path to the text file containing the quiz questions and solutions.
    - `--sleep <milliseconds>` (optional): Milliseconds to sleep between iterations (default: 1000).

3. Sit back and watch the bot participate in the Kahoot quiz! You only have to put in the kahoot id and name