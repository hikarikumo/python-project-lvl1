import random
import prompt
from cli import greet_first, welcome_user


def question_gcd():
    """Ask the question and return a tuple (is_correct, gcd_value)."""
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    gcd = gcd_calc(random_number1, random_number2)
    
    question_to_user_gcd = prompt.string(f'Question: {random_number1} {random_number2}\n')
    
    return question_to_user_gcd == str(gcd), gcd


def gcd_goal_message():
    """Information about the goal to the user."""
    print('Find the greatest common divisor of given numbers.\n')


def gcd_calc(random_number1, random_number2):
    """Calculate gcd of two random values."""
    list_div1 = [count_n for count_n in range(1, random_number1 + 1) if random_number1 % count_n == 0]
    list_div2 = [count_m for count_m in range(1, random_number2 + 1) if random_number2 % count_m == 0]
    
    common_list = [index for index in list_div1 + list_div2 if index in list_div1 and index in list_div2]
    return common_list[-1]


def gcd_game(name):
    """Execute main game logic."""
    for _ in range(3):
        status_calc, gcd = question_gcd()
        if status_calc:
            print(f'Your answer: {gcd}\nCorrect!')
            if _ == 2:
                print(f'Congratulations, {name}!')
                return True
        else:
            print(f"Let's try again, {name}!")
            return False


def main():
    """Run brain-gcd game."""
    greet_first()
    gcd_goal_message()
    name = welcome_user()
    gcd_game(name)


if __name__ == '__main__':
    main()
