import random
import prompt
from cli import greet_first, welcome_user


def question_prime():
    """Ask the question and return a tuple (number_to_guess, user_answer)."""
    number_to_guess = random.randint(1, 100)
    user_answer = prompt.string(f'Number: {number_to_guess}\n')
    return number_to_guess, user_answer


def prime_goal():
    """Provide information about the goal of the prime game to the user."""
    print('Answer "yes" if given number is prime. Otherwise answer "no".\n')


def is_prime(number):
    divisors = [count for count in range(1, number + 1) if number % count == 0]
    return len(divisors) == 2


def prime_game(name):
    attempts = 3
    for _ in range(attempts):
        random_number, user_answer = question_prime()
        if is_prime(random_number) == (user_answer.lower() == 'yes'):
            print(f'Your answer: {user_answer} {random_number} is prime')
            print('Correct!')
            print(f'Congratulations, {name}!')
            return True

        print(f"Let's try again, {name}!")

    print(f'Sorry, you have used all {attempts} attempts. The correct answer was {"yes" if is_prime(random_number) else "no"} {random_number}.')
    return False


def main():
    """Run brain-prime game."""
    greet_first()
    prime_goal()
    name = welcome_user()
    prime_game(name)


if __name__ == '__main__':
    main()
