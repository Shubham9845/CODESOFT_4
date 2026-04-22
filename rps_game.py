import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

# Function to handle the user's choice and game logic
def play(choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    result = determine_winner(choice, computer_choice)
    
    # Update labels with choices and result
    user_choice_var.set(f"Your choice: {choice.capitalize()}")
    computer_choice_var.set(f"Computer's choice: {computer_choice.capitalize()}")
    result_var.set(result)
    
    # Update scores
    if result == "You win!":
        global user_score
        user_score += 1
    elif result == "You lose!":
        global computer_score
        computer_score += 1
        
    user_score_var.set(f"Your score: {user_score}")
    computer_score_var.set(f"Computer's score: {computer_score}")

# Function to prompt to play again
def play_again():
    response = messagebox.askyesno("Play Again", "Do you want to play another round?")
    if response:
        user_choice_var.set("")
        computer_choice_var.set("")
        result_var.set("")
    else:
        root.destroy()

# Initialize scores
user_score = 0
computer_score = 0

# Create main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Create and place widgets
tk.Label(root, text="Choose Rock, Paper, or Scissors:").grid(row=0, column=0, columnspan=3, pady=10)

tk.Button(root, text="Rock", command=lambda: play('rock')).grid(row=1, column=0, padx=10, pady=10)
tk.Button(root, text="Paper", command=lambda: play('paper')).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Scissors", command=lambda: play('scissors')).grid(row=1, column=2, padx=10, pady=10)

user_choice_var = tk.StringVar()
computer_choice_var = tk.StringVar()
result_var = tk.StringVar()

tk.Label(root, textvariable=user_choice_var).grid(row=2, column=0, columnspan=3, pady=10)
tk.Label(root, textvariable=computer_choice_var).grid(row=3, column=0, columnspan=3, pady=10)
tk.Label(root, textvariable=result_var).grid(row=4, column=0, columnspan=3, pady=10)

user_score_var = tk.StringVar()
computer_score_var = tk.StringVar()

tk.Label(root, textvariable=user_score_var).grid(row=5, column=0, pady=10)
tk.Label(root, textvariable=computer_score_var).grid(row=5, column=2, pady=10)

tk.Button(root, text="Play Again", command=play_again).grid(row=6, column=0, columnspan=3, pady=10)

# Initialize scores display
user_score_var.set(f"Your score: {user_score}")
computer_score_var.set(f"Computer's score: {computer_score}")

# Run the application
root.mainloop()
