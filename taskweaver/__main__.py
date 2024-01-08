import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from .cli import __main__


def main():
    __main__.main()


if __name__ == "__main__":
    main()
