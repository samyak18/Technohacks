#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox
def check():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != " ":
            return buttons[i][0]["text"]
    for j in range(3):
        if buttons[0][j]["text"] == buttons[1][j]["text"] == buttons[2][j]["text"] != " ":
            return buttons[0][j]["text"]
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != " ":
        return buttons[0][0]["text"]
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != " ":
        return buttons[0][2]["text"]
    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] == " ":
                return None
    return "Tie"
def click(i, j):
    global symbol
    if buttons[i][j]["text"] == " ":
        buttons[i][j]["text"] = symbol
        result = check()
        if result is not None:
            if result == "Tie":
                messagebox.showinfo("Game Over", "It's a tie!")
            else:
                messagebox.showinfo("Game Over", f"{result} wins!")
            restart_game()  
        else:
            if symbol == "X":
                symbol = "O"
            else:
                symbol = "X"
def restart_game():
    global symbol
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = " "
            buttons[i][j]["state"] = "normal"
    symbol = "X"
root = tk.Tk()
root.title("Tic Tac Toe")
buttons = [[tk.Button(root, text=" ", font=("Arial", 20), width=4, height=2) for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)
        buttons[i][j]["command"] = lambda i=i, j=j: click(i, j)
symbol = "X"
root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




