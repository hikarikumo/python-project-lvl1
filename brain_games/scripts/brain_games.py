import sys
import os
from importlib import import_module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


cli = import_module("cli")
main = cli.main


if __name__ == "__main__":
    main()
