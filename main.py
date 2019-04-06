# -*- coding: utf-8 -*-
from guessing import Guessing
import hangman
import header


def main():
    header.define("Welcome!")

    print("(1) - Guessing")
    print("(2) - Hangman")

    game = int(input(">> Choose your game: "))

    if game == 1:
        Guessing()
    elif game == 2:
        hangman.play()
    else:
        print("Game {} is not present".format(game))


if __name__ == "__main__":
    main()
