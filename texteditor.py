import tkinter as tk
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, "r") as file:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(tk.END, file.read())

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, "w") as file:
            file.write(text_editor.get(1.0, tk.END))

def clear_text():
    text_editor.delete(1.0, tk.END)



root = tk.Tk()
root.title("Text Editor")

# Text Widget
text_editor = tk.Text(root)
text_editor.pack()

# Menu
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Clear", command=clear_text)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Text Font", command=clear_text)
menu_bar.add_cascade(label="Format", menu=edit_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Zoom", command=clear_text)
menu_bar.add_cascade(label="View", menu=edit_menu)





root.config(menu=menu_bar)

root.mainloop()
