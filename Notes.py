import tkinter as tk
from tkinter import messagebox

# Function to save the content back to Notes.txt
def save_note():
    try:
        with open("Notes.txt", "w") as file:
            file.write(text_box.get("1.0", tk.END))  # Save all text from the text box
        messagebox.showinfo("Success", "Note saved!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to open Notes.txt and read its content
def open_note():
    try:
        with open("Notes.txt", "r") as file:
            content = file.read()
            text_box.insert(tk.END, content)  # Insert the content into the text box
    except FileNotFoundError:
        pass  # If the file doesn't exist yet, we can start with an empty text box

# Create main window
root = tk.Tk()
root.title("Notes App")
root.geometry("300x300")  # Small window size

# Create a Text widget to edit the notes
text_box = tk.Text(root, height=10, width=35)
text_box.pack(padx=10, pady=10)

# Load the content of Notes.txt if it exists
open_note()

# Create a save button
save_button = tk.Button(root, text="Save Note", command=save_note)
save_button.pack(pady=5)

# Run the application
root.mainloop()
