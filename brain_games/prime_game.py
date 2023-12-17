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
    """Check if the number is prime."""
    divisors = [count for count in range(1, number + 1) if number % count == 0]
    return len(divisors) == 2


def prime_game(name):
    """Brain game prime logic."""
    for _ in range(3):
        random_number, user_answer = question_prime()
        prime_status = is_prime(random_number)
        
        expected_answer = 'yes' if prime_status else 'no'
        
        if user_answer == expected_answer:
            print(f'Your answer: {user_answer} {random_number} is prime')
            print('Correct!')
            if _ == 2:
                print(f'Congratulations, {name}!')
                return True
        else:
            print(f"Let's try again, {name}!")
            return False


def main():
    """Run brain-prime game."""
    greet_first()
    prime_goal()
    name = welcome_user()
    prime_game(name)


if __name__ == '__main__':
    main()
