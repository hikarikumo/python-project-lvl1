import sys
import os
from importlib import import_module

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


calc_game = import_module("calc_game")
main = calc_game.main


if __name__ == "__main__":
    main()
