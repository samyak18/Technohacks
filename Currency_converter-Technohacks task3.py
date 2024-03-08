#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
import requests
def convert_currency():
    base_currency = base_currency_var.get().upper()
    target_currency = target_currency_var.get().upper()
    amount = float(amount_entry.get())
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    if target_currency not in data["rates"]:
        result_window = tk.Toplevel(root)
        result_window.title("Conversion Result")
        result_label = tk.Label(result_window, text=f"Target currency '{target_currency}' is not available.")
        result_label.pack()
    else:
        exchange_rate = data["rates"][target_currency]
        converted_amount = amount * exchange_rate
        result_window = tk.Toplevel(root)
        result_window.title("Conversion Result")
        result_label = tk.Label(result_window, text=f"{amount} {base_currency} is {converted_amount:.2f} {target_currency}")
        result_label.pack()
root = tk.Tk()
root.title("Currency Converter")
currencies = ["INR", "EUR", "GBP", "JPY", "CAD", "AUD"] 
base_currency_label = tk.Label(root, text="Base Currency:")
base_currency_label.grid(row=0, column=0)
base_currency_var = tk.StringVar(root)
base_currency_var.set(currencies[0])
base_currency_dropdown = tk.OptionMenu(root, base_currency_var, *currencies)
base_currency_dropdown.grid(row=0, column=1)
target_currency_label = tk.Label(root, text="Target Currency:")
target_currency_label.grid(row=1, column=0)
target_currency_var = tk.StringVar(root)
target_currency_var.set(currencies[1])
target_currency_dropdown = tk.OptionMenu(root, target_currency_var, *currencies)
target_currency_dropdown.grid(row=1, column=1)
amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=2, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1)
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, columnspan=2)
root.mainloop()


# In[ ]:




