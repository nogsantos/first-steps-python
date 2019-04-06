class Guessing:
    secret_number = 42
    guess = 0

    def __init__(self):
        self.show_message()
        self.show_input()

    def secret(self):
        if self.secret_number == self.guess:
            print("You win!")
        else:
            print("You lose!")
            if self.is_biggest(self.guess, self.secret_number):
                print("Is Bigger then")
            elif self.is_smaller(self.guess, self.secret_number):
                print("Is Smaller then")

    def show_input(self):
        str_guess = input("What is the number: ")
        self.is_a_valid_input(str_guess)
        self.guess = int(str_guess)
        self.secret()

    @staticmethod
    def is_a_valid_input(guess):
        if not guess:
            raise ValueError("Can not be empty")

    @staticmethod
    def show_message():
        message = "Well come to the guessing game!"
        line = "*******************************"
        print(line, message, line)

    @staticmethod
    def is_biggest(num, guess):
        return num > guess

    @staticmethod
    def is_smaller(num, guess):
        return num < guess
