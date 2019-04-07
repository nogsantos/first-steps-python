# -*- coding: utf-8 -*-
import random
import header


def play():
    header.define("Welcome to the hangman game!")

    _file = open("words", "r")
    words_from_file = []

    for line in _file:
        line = line.strip()
        words_from_file.append(line)

    _file.close()

    word_of_time = random.randrange(0, len(words_from_file))
    secret_word = words_from_file[word_of_time].upper()
    secret_word_list = ["_" for each_letter in secret_word]
    hanged = False
    hit = False
    # @todo - number of attempts
    hints_attempts = len(secret_word) if len(secret_word) < 5 else len(secret_word) - 3
    hints = 0

    print("{} letters in {} attempts {} ".format(len(secret_word_list), hints_attempts, secret_word_list))

    while not hanged and not hit:

        guess = input("Which letter?\n").strip().upper()

        if guess in secret_word:
            index = 0
            for word in secret_word:
                if guess == word:
                    secret_word_list[index] = word
                index += 1

        hints += 1

        missing_words = str(secret_word_list.count("_"))
        print(secret_word_list)

        print("{} words missing".format(missing_words), "Attempt: {} of {}".format(hints, hints_attempts))

        hanged = hints == hints_attempts
        hit = "_" not in secret_word_list

    if hit:
        print("You win!")
    else:
        print("You lose!")

    print("Game over")


if __name__ == "__main__":
    play()
