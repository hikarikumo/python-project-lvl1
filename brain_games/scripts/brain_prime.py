import sys
import os
from importlib import import_module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


prime_game = import_module("prime_game")
main = prime_game.main


if __name__ == "__main__":
    main()
