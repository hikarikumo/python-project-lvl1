import sys
import os
from importlib import import_module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


gcd_game = import_module("gcd_game")
main = gcd_game.main


if __name__ == "__main__":
    main()
