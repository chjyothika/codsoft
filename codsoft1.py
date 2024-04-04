import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        label.config(text="Please enter a task.")

def remove_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        label.config(text="Please select a task to remove.")

# Create the main window
root = tk.Tk()
root.title("Dynamic To-Do List")

# Create GUI elements
label = tk.Label(root, text="Enter a task:")
label.pack()

entry = tk.Entry(root, width=30)
entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack()

# Start the main event loop
root.mainloop()
