#!/usr/bin/env python3
from brain_games.games import parity_check
from brain_games.logic import start_game


def main():
    print(start_game(parity_check))


if __name__ == '__main__':
    main()
