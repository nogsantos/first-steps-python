# -*- coding: utf-8 -*-
import random
import header


class Guessing:
    secret_number = random.randrange(1, 101)
    score = 1000
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
            print("You win! Total Score {} points\n".format(self.score))
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
            self.calculate_score()

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
        header.define("Welcome to the guessing game!")

    def is_bigger(self):
        return self.guess < self.secret_number

    def is_smaller(self):
        return self.guess > self.secret_number

    def calculate_score(self):
        losses = abs(self.secret_number - self.guess)
        self.score = self.score = losses


if __name__ == "__main__":
    Guessing()
