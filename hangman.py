# -*- coding: utf-8 -*-
import header


def play():
    header.define("Welcome to the hangman game!")

    secret_word = "bananaaa"
    hanged = False
    hit = False

    while not hanged and not hit:

        guess = input("Which letter?\n")
        index = 0
        for word in secret_word:
            if guess.lower() == word.lower():
                print("I found the letter {} in position {} ".format(word, index))
            index = index + 1


if __name__ == "__main__":
    play()
