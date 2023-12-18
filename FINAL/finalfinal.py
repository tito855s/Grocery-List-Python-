import tkinter as tk

def add_item():
    # Get item and price from entry fields
    item = entry_item.get()
    price = entry_price.get()
    # Check if both item and price are entered
    if item and price:
        # Combine item and price
        item_with_price = f"{item} - ${price}"
        # Add item with price to the listbox
        listbox.insert(tk.END, item_with_price)
        # Clear entry fields
        entry_item.delete(0, tk.END)
        entry_price.delete(0, tk.END)

def remove_item():
    # Get the index of the selected item
    selected = listbox.curselection()
    # Check if an item is selected
    if selected:
        # Remove the selected item from the listbox
        listbox.delete(selected)

def clear_list():
    # Clear all items from the listbox
    listbox.delete(0, tk.END)

def save_list():
    # Get all items from the listbox
    items = listbox.get(0, tk.END)
    # Write each item to a text file
    with open("grocery_list.txt", "w") as file:
        for item in items:
            file.write(item + "\n")

def start_list():
    # Hide the main menu
    main_menu.pack_forget()
    # Show the grocery list interface
    frame.pack(padx=20, pady=20)

def quit_app():
    # Close the application
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Grocery List")

# Configure main menu style
main_menu = tk.Frame(root, bg="#136e28", padx=300, pady=300)

# Title for the main menu
title_label = tk.Label(main_menu, text="Welcome to my grocery list", font=("Arial", 20), fg="white", bg="#136e28")
title_label.pack(pady=20)


# Button to start the list
start_button = tk.Button(main_menu, text="Start a List", command=start_list, padx=20, pady=10, bg="#f08080", fg="white")
start_button.pack(pady=10)

# Button to quit the application
quit_button = tk.Button(main_menu, text="Quit", command=quit_app, padx=20, pady=10, bg="#f08080", fg="white")
quit_button.pack()

# Create the grocery list interface (initially hidden)
frame = tk.Frame(root, bg="#136e28", width=800, height=500, padx=300, pady=300)

# Label for entering item
label_item = tk.Label(frame, text="Enter Item:")
label_item.grid(row=0, column=0)

# Entry field for item
entry_item = tk.Entry(frame)
entry_item.grid(row=0, column=1)

# Label for entering price
label_price = tk.Label(frame, text="Enter Price:")
label_price.grid(row=0, column=2)

# Entry field for price
entry_price = tk.Entry(frame)
entry_price.grid(row=0, column=3)

# Button to add item to the listbox
add_button = tk.Button(frame, text="Add", command=add_item)
add_button.grid(row=0, column=4, padx=5)

# Button to remove selected item from the listbox
remove_button = tk.Button(frame, text="Remove", command=remove_item)
remove_button.grid(row=1, column=0, pady=10)

# Button to clear all items from the listbox
clear_button = tk.Button(frame, text="Clear List", command=clear_list)
clear_button.grid(row=1, column=1)

# Button to save the list to a text file
save_button = tk.Button(frame, text="Save List", command=save_list)
save_button.grid(row=1, column=2)

# Listbox to display items
listbox = tk.Listbox(frame, width=40, height=10)
listbox.grid(row=2, columnspan=5, pady=10)

# Display the main menu
main_menu.pack()

# Run the application
root.mainloop()
