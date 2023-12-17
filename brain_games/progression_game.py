import random
import prompt
from cli import greet_first, welcome_user


def progression_goal():
    """Information about the goal to the user."""
    print('What number is missing in the progression?\n')


def string_progression(progression):
    """Convert list into parsed string."""
    return ', '.join(map(str, progression))


def question_progression():
    """
    Ask the question and return a tuple (is_correct, missing_element).

    Returns:
        Tuple with True and the missing element if the answer is correct,
        Tuple with False and the missing element otherwise.
    """
    miss_element, progression = progression_show()
    question_to_user = prompt.string(f'Question: {string_progression(progression)}\n')
    return question_to_user == str(miss_element), miss_element


def progression_show():
    """
    Create arithmetic progression.

    Returns:
        Progression with *hidden* element + value of that hidden element.
    """
    random_index = random.randint(1, 10)
    random_step = random.randint(1, 10)
    random_initial = random.randint(1, 10)

    progression = progression_calc(random_step, random_initial)
    keep_value = progression[random_index]
    progression[random_index] = '..'

    return keep_value, progression


def progression_game(name):
    """Perform progression game logic."""
    attempts = 3
    for _ in range(attempts):
        calc_value, miss_element = question_progression()
        if calc_value:
            print(f'Your answer: {miss_element}\nCorrect!')
            if _ == attempts - 1:
                print(f'Congratulations, {name}!')
                return True
        else:
            print(f"Let's try again, {name}!")

    print(f'Sorry, you have used all {attempts} attempts. The correct answer was {miss_element}.')
    return False



def progression_calc(random_step, random_initial):
    """
    Create progression.

    Input:
        Accept two random parameters: position and progression step.

    Returns:
        Returns progression list.
    """
    progression_length = 11
    progression_member = random_initial
    progression = [progression_member + i * random_step for i in range(progression_length)]
    return progression


def main():
    """
    Run brain-progression game.

    Returns:
        Return and verify the proper element inside of the arithmetic progression.
    """
    greet_first()
    progression_goal()
    name = welcome_user()
    progression_game(name)


if __name__ == '__main__':
    main()
