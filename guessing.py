# -*- coding: utf-8 -*-
import random


class Guessing:
    secret_number = random.randrange(1, 101)
    attempts = 0
    guess = 0
    is_in_loop = True

    def __init__(self):
        self.show_message()
        while self.is_in_loop:
            self.show_input()

    def secret(self):
        self.attempts = self.attempts + 1
        if self.secret_number == self.guess:
            print("You win!\n")
            print("Number of attempts: {}".format(self.attempts))
            self.is_in_loop = False
        else:
            message = "You miss, {}"
            result = "the number is "
            if self.is_bigger():
                result += "Bigger"
            elif self.is_smaller():
                result += "Smaller"
            print(message.format(result))

    def show_input(self):
        if self.attempts > 0:
            print("\n", "Again!", "\n")
        str_guess = input(">> What is the number that I thing between 1 and 100?\n")
        if self.is_a_valid_input(str_guess):
            self.guess = self.is_a_valid_input(str_guess)
            self.secret()
        else:
            print("Error:", "The number must be between 1 and 10")

    @staticmethod
    def is_a_valid_input(guess):
        if not guess:
            raise ValueError("The value can't be empty and must be an number")

        the_number = int(guess)

        if 0 < the_number < 101:
            return the_number
        else:
            return False

    @staticmethod
    def show_message():
        message = "Welcome to the guessing game!"
        line = "*******************************"
        header = "{}\n{}\n{}".format(line, message, line)
        print(header)

    def is_bigger(self):
        return self.guess < self.secret_number

    def is_smaller(self):
        return self.guess > self.secret_number
