import sys
import os
from importlib import import_module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


even_game = import_module("even_game")
main = even_game.main


if __name__ == "__main__":
    main()
