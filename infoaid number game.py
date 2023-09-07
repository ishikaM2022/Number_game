import tkinter as tk
import random


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.secret_number = random.randint(1, 100)
        self.attempts_left = 10

        self.label = tk.Label(root, text="Welcome to the Number Guessing Game!")
        self.label.pack(pady=10)

        self.name_label = tk.Label(root, text="Enter your name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        self.name_entry.bind('<Key>', self.update_button_state)

        self.start_button = tk.Button(root, text="Start", state="disabled", command=self.start_game)
        self.start_button.pack(pady=10)

        self.guess_label = tk.Label(root, text="Guess a number (1-100):")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(root)
        self.guess_entry.pack()

        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.restart_button = tk.Button(root, text="Play Again", state="disabled", command=self.restart_game)
        self.restart_button.pack(pady=10)

    def update_button_state(self, event):
        name = self.name_entry.get().strip()
        if name:
            self.start_button.config(state="normal")
        else:
            self.start_button.config(state="disabled")

    def start_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts_left = 10
        self.result_label.config(text="")
        self.restart_button.config(state="disabled")
        self.guess_button.config(state="normal")
        self.start_button.config(state="disabled")

    def check_guess(self):
        guess = int(self.guess_entry.get())
        self.attempts_left -= 1

        if guess < self.secret_number:
            result = "Higher! Attempts left: " + str(self.attempts_left)
        elif guess > self.secret_number:
            result = "Lower! Attempts left: " + str(self.attempts_left)
        else:
            result = "Congratulations! You guessed the number."
            self.guess_button.config(state="disabled")
            self.restart_button.config(state="normal")

        if self.attempts_left == 0:
            result = "Game Over. The secret number was " + str(self.secret_number)
            self.guess_button.config(state="disabled")
            self.restart_button.config(state="normal")

        self.result_label.config(text=result)

    def restart_game(self):
        self.start_game()
        self.name_entry.delete(0, tk.END)
        self.guess_entry.delete(0, tk.END)


root = tk.Tk()
game = NumberGuessingGame(root)
root.mainloop()
