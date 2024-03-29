import prompt
import random
import general_module
from cli import greet_first, welcome_user


def check_if_even(number):
    """Return true if even."""
    return number % 2 == 0


def even_wrong_answer(correct):
    print(f"Not '{correct}'. Correct '{'no' if correct == 'yes' else 'yes'}.")


def even_game():
    random_number = random.randint(0, 1000)
    result = check_if_even(random_number)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f"Question: {random_number}")
    answer = (
        prompt.string().lower()
    )  # Convert answer to lowercase for case-insensitive comparison
    if answer in ["yes", "no"]:
        if (answer == "yes" and result) or (answer == "no" and not result):
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
        general_module.correct()
    general_module.game_success_finish(name)


def main():
    """Run brain-even game."""
    greet_first()
    name = welcome_user()
    even_game_logic(name)


if __name__ == "__main__":
    main()
