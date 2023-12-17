import random
import prompt
from cli import greet_first, welcome_user


OPERATIONS = {
    'summation': ('+', lambda x, y: x + y),
    'subtraction': ('-', lambda x, y: x - y),
    'multiplication': ('*', lambda x, y: x * y),
}


def get_random_numbers():
    return random.randint(0, 100), random.randint(0, 100)


def generate_question(operation):
    symbol, _ = OPERATIONS[operation]
    num1, num2 = get_random_numbers()
    return f'Question: {num1} {symbol} {num2}\n', num1, num2


def check_answer(question, answer, correct_answer):
    if answer == str(correct_answer):
        print(f'Your answer: {answer}')
        print('Correct!')
        return True
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
    return False


def play_game(operation):
    question, num1, num2 = generate_question(operation)
    correct_answer = OPERATIONS[operation][1](num1, num2)
    user_answer = prompt.string(question)
    return check_answer(question, user_answer, correct_answer)


def user_fail_message(name):
    print(f"Let's try again, {name}!")


def calc_game_logic(name):
    operations = list(OPERATIONS.keys())
    random.shuffle(operations)
    for operation in operations:
        if not play_game(operation):
            user_fail_message(name)
            return
    print(f'Congratulations, {name}!')


def main():
    greet_first()
    print('What is the result of the expression?\n')
    name = welcome_user()
    calc_game_logic(name)


if __name__ == '__main__':
    main()
