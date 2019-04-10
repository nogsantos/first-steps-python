# -*- coding: utf-8 -*-
import random
import header


def play():
    header.define("Welcome to the hangman game!")

    secret_word = load_secret_word()

    secret_word_list = ["_" for each_letter in secret_word]

    hints_attempts = len(set(secret_word)) + 3

    print_game_header(hints_attempts, secret_word_list)

    game_result = game_loop(hints_attempts, secret_word, secret_word_list)

    end_game_message(secret_word)

    print_game_result(game_result)


def print_game_header(hints_attempts, secret_word_list):
    print("{} letters in {} attempts {} ".format(len(secret_word_list), hints_attempts, secret_word_list))


def game_loop(hints_attempts, secret_word, secret_word_list):
    hanged = False
    hints = 0
    hit = False
    while not hanged and not hit:
        hints = read_and_hit_hints(hints, secret_word, secret_word_list)

        missing_words = str(secret_word_list.count("_"))

        print_game_status(hints, hints_attempts, missing_words, secret_word_list)

        hanged = hints == hints_attempts
        hit = "_" not in secret_word_list
    return hit


def end_game_message(secret_word):
    print("Game over. The secret word was: {} ".format(secret_word))


def print_game_result(hit):
    if hit:
        win_result()
    else:
        lose_result()


def win_result():
    print("You Win!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def lose_result():
    print("You Lose!")
    print("      _______________       ")
    print("     /               \      ")
    print("    /                 \     ")
    print("  //                   \/\  ")
    print("  \|   XXXX     XXXX   | /  ")
    print("   |   XXXX     XXXX   |/   ")
    print("   |   XXX       XXX   |    ")
    print("   |                   |    ")
    print("   \__      XXX      __/    ")
    print("     |\     XXX     /|      ")
    print("     | |           | |      ")
    print("     | I I I I I I I |      ")
    print("     |  I I I I I I  |      ")
    print("     \_             _/      ")
    print("       \_         _/        ")
    print("         \_______/          ")


def print_game_status(hints, hints_attempts, missing_words, secret_word_list):
    print(secret_word_list)
    print("{} words missing".format(missing_words), "Attempt: {} of {}".format(hints, hints_attempts))


def read_user_input():
    return input("Which letter?\n").strip().upper()


def read_and_hit_hints(hints, secret_word, secret_word_list):
    guess = read_user_input()
    if guess in secret_word:
        index = 0
        for word in secret_word:
            if guess == word:
                secret_word_list[index] = word
            index += 1
    hints += 1
    return hints


def load_secret_word():
    _file = open("words", "r")
    words_from_file = []
    for line in _file:
        line = line.strip()
        words_from_file.append(line)
    _file.close()
    word_of_time = random.randrange(0, len(words_from_file))
    secret_word = words_from_file[word_of_time].upper()
    return secret_word


if __name__ == "__main__":
    play()
