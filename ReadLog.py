import tkinter as tk
from tkinter import scrolledtext

def open_file():
    file_path = "key_logs.txt"
    try:
        with open(file_path, "r") as file:
            content = file.read()
    except FileNotFoundError:
        content = "File not found. Please make sure 'key_logs.txt' exists."
    except Exception as e:
        content = f"Error reading file: {e}"
    
    # Create a window
    window = tk.Tk()
    window.title("Key Logs")
    window.geometry("400x300")  # Set window size (width x height)
    
    # Add a scrollable text widget
    text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=15)
    text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    text_area.insert(tk.END, content)
    text_area.config(state=tk.DISABLED)  # Make the text read-only

    window.mainloop()

if __name__ == "__main__":
    open_file()
