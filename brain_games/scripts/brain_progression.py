import sys
import os
from importlib import import_module

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


progression_game = import_module("progression_game")
main = progression_game.main


if __name__ == "__main__":
    main()
