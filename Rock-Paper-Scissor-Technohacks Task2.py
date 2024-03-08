#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import random
choice_counter = {"Rock": 0, "Paper": 0, "Scissors": 0}
def play(player_choice):
    global choice_counter
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = ""
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "You lose!"
    result_text = f"Computer chose: {computer_choice}\n{result}"
    display_result(result_text)
    choice_counter[player_choice] += 1
    check_reset()
def display_result(result_text):
    result_window = tk.Toplevel(root)
    result_window.title("Game Result")
    result_label = tk.Label(result_window, text=result_text)
    result_label.pack()
def reset_counters():
    for choice in choice_counter:
        choice_counter[choice] = 0
def check_reset():
    if all(counter > 0 for counter in choice_counter.values()):
        reset_counters()
        start_game()   
def start_game():
    global root
    root = tk.Tk()
    root.title("Rock Paper Scissors")
    rock_button = tk.Button(root, text="Rock", command=lambda: play("Rock"))
    rock_button.pack()
    paper_button = tk.Button(root, text="Paper", command=lambda: play("Paper"))
    paper_button.pack()
    scissors_button = tk.Button(root, text="Scissors", command=lambda: play("Scissors"))
    scissors_button.pack()
    root.mainloop()
start_game()


# In[ ]:




