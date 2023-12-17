import prompt
import random
import general_module
from cli import greet_first, welcome_user

def check_if_even(number):
    """Return true if even."""
    return number % 2 == 0

def even_question():
    print("Answer 'yes' if number even otherwise answer 'no'.")

def even_wrong_answer(correct_answer):
    print(f"'{correct_answer}' is wrong answer ;(. Correct answer was '{'no' if correct_answer == 'yes' else 'yes'}.")

def even_game():
    """
    Verify the correct answer.

    Test what does the user type in: yes or not.
    Other characters are not allowed.
    Verify the correct answer provided by user.

    Returns:
        True ot False according to the provided answer by user.
    """
    random_number = random.randint(0, 1000)
    even_result = check_if_even(random_number)
    print(random_number)
    even_question()
    answer = prompt.string().lower()  # Convert answer to lowercase for case-insensitive comparison
    if answer in ['yes', 'no']:
        if (answer == 'yes' and even_result) or (answer == 'no' and not even_result):
            return True
        even_wrong_answer(answer)
        return False
    else:
        print("Invalid input. Please answer 'yes' or 'no'.")
        return False

def even_game_logic(name):
    """Even game main logic."""
    for _ in range(3):
        received_value = even_game()
        if not received_value:
            general_module.try_again(name)
            break
        general_module.correct_answer()

def main():
    """Run brain-even game."""
    greet_first()
    name = welcome_user()
    even_game_logic(name)

if __name__ == '__main__':
    main()
