import tkinter as tk
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)
    return user_choice, computer_choice, result

def update_display(user_choice, computer_choice, result):
    user_label.config(text=f"Your choice: {user_choice}")
    computer_label.config(text=f"Computer's choice: {computer_choice}")
    result_label.config(text=result)

def on_play():
    user_choice = choice_var.get()
    user_choice, computer_choice, result = play_game(user_choice)
    update_display(user_choice, computer_choice, result)

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

choices = ['rock', 'paper', 'scissors']
choice_var = tk.StringVar()
choice_var.set('rock')

user_label = tk.Label(root, text="Your choice: ")
user_label.pack()

computer_label = tk.Label(root, text="Computer's choice: ")
computer_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

for choice in choices:
    tk.Radiobutton(root, text=choice, variable=choice_var, value=choice).pack()

play_button = tk.Button(root, text="Play", command=on_play)
play_button.pack()

root.mainloop()
