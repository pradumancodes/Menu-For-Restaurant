import tkinter as tk

# Menu of the restaurant
menu = {
    'Pizza': 80,
    'Pasta': 50,
    'Burger': 70,
    'Fries': 50,
    'Cold Coffee': 80,
    'Coffee': 80,
}

# Function to add items to the order
def add_to_order():
    item = item_entry.get()
    if item in menu:
        order_total.set(order_total.get() + menu[item])
        order_list.insert(tk.END, f"{item} - Rs{menu[item]}")
        message_label.config(text=f"Item '{item}' has been added to your order.", fg="green")
    else:
        message_label.config(text=f"Item '{item}' is not available!", fg="red")

# Function to display the total order amount
def show_total():
    total = order_total.get()
    message_label.config(text=f"The total amount of your order is Rs{total}.", fg="blue")

# Setting up the GUI
root = tk.Tk()
root.title("Restaurant Ordering System")

# Custom Font
custom_font = ("Helvetica", 14)
title_font = ("Helvetica", 18, "bold")

# Greeting Label
greeting_label = tk.Label(root, text="Welcome To Restaurant", font=title_font)
greeting_label.pack(pady=10)

# Menu Display
menu_label = tk.Label(root, text="\n".join([f"{item}: Rs{price}" for item, price in menu.items()]), font=custom_font)
menu_label.pack(pady=10)

# Entry for Item
item_label = tk.Label(root, text="Enter the name of the item you want to order:", font=custom_font)
item_label.pack(pady=5)
item_entry = tk.Entry(root, font=custom_font)
item_entry.pack(pady=5)

# Button to add item
add_button = tk.Button(root, text="Add to Order", font=custom_font, command=add_to_order)
add_button.pack(pady=10)

# Listbox to show ordered items
order_list = tk.Listbox(root, font=custom_font, width=30)
order_list.pack(pady=10)

# Variable to keep track of total order amount
order_total = tk.IntVar()
order_total.set(0)

# Button to show total
total_button = tk.Button(root, text="Show Total", font=custom_font, command=show_total)
total_button.pack(pady=10)

# Label to display messages
message_label = tk.Label(root, text="", font=custom_font)
message_label.pack(pady=10)

# Start the GUI loop
root.mainloop()
