import tkinter as tk
from tkinter import messagebox
import random

# Function to get computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Function to update the result and scores
def play(user_choice):
    global user_score, computer_score
    
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    
    result_text.set(f"You chose {user_choice}, Computer chose {computer_choice}.")
    
    if winner == "tie":
        result_text.set(result_text.get() + " It's a tie!")
    elif winner == "user":
        user_score += 1
        result_text.set(result_text.get() + " You win!")
    else:
        computer_score += 1
        result_text.set(result_text.get() + " You lose!")
    
    score_text.set(f"Scores - You: {user_score} | Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_text.set("")
    score_text.set(f"Scores - You: {user_score} | Computer: {computer_score}")

# Initialize scores
user_score = 0
computer_score = 0

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Create and set the result text variable
result_text = tk.StringVar()
score_text = tk.StringVar()
score_text.set(f"Scores - You: {user_score} | Computer: {computer_score}")

# Create widgets
result_label = tk.Label(root, textvariable=result_text, font=("Helvetica", 12))
score_label = tk.Label(root, textvariable=score_text, font=("Helvetica", 12))
rock_button = tk.Button(root, text="Rock", command=lambda: play("rock"))
paper_button = tk.Button(root, text="Paper", command=lambda: play("paper"))
scissors_button = tk.Button(root, text="Scissors", command=lambda: play("scissors"))
reset_button = tk.Button(root, text="Reset Game", command=reset_game)

# Place widgets on the window
result_label.pack(pady=10)
score_label.pack(pady=10)
rock_button.pack(side="left", padx=20, pady=20)
paper_button.pack(side="left", padx=20, pady=20)
scissors_button.pack(side="left", padx=20, pady=20)
reset_button.pack(pady=20)

# Start the main event loop
root.mainloop()
