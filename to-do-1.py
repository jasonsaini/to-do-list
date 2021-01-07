import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pickle
from win10toast import ToastNotifier

# Note: (event = None) for functions with keybinds

# Adds tasks from entry to listbox
def add_task(event = None):
    # Gets tasks from entry
    task = entry_tasks.get()
    # Adds tasks if string is present
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_tasks.delete(0, tk.END)

# Deletes cursor selected entry
def delete_task(event = None):
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        pass

# Right click menu function
def on_right_click(event):
    selected = event.widget.curselection()
    if selected:
        try:
            rc_menu.tk_popup(event.x_root, event.y_root)
        finally:
            rc_menu.grab_release()

# Saves tasks to .dat file
def save_tasks(event = None):
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

# Loads tasks from .dat file
def load_tasks(event = None):
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        for task in tasks:
            listbox_tasks.insert(tk.END, task)
    except:
        empty = []
        pickle.dump(empty, open("tasks.dat", "wb"))
        #pickle.dump(empty, open("tasks.dat", "wb"))

# Clears list
def clear_list(event = None):
    listbox_tasks.delete(0,tk.END)

# Enables reminders (currently every hour)
def remind(event = None):
    num_tasks = listbox_tasks.size()
    n = ToastNotifier()
    message = f"You have {str(num_tasks)} items on your To-Do list!"
    n.show_toast("REMINDER", message, duration=10, threaded=True, icon_path= "icon.ico")
    root.after(360000, remind)

# Exit behavior (on window close)
def on_exit(event = None):
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    tasks_on_file = pickle.load(open("tasks.dat", "rb"))
    # Prompts save if changes were made
    if tasks != tasks_on_file:
        save_prompt = tk.messagebox.askyesnocancel(title = "Save List?", message = "Save changes to list?")
        if save_prompt:
            save_tasks()
            root.destroy()
        elif save_prompt is None:
            pass
        else:
            root.destroy()
    # If no changes were made, close window
    else:
        root.destroy()

# Create GUI
# Initialize window
root = tk.Tk()
root.title("To Do List by jason")
root.geometry("300x400")
icon = PhotoImage(file = 'check.png')
root.iconphoto(False, icon)

# Remove maximize button (so window can't be resized)
root.resizable(0,0)

# Key Binds
root.bind('<Return>', add_task)
root.bind('<Button-3>', on_right_click)
root.bind('<Control-s>', save_tasks)
root.bind('<Control-w>', on_exit)
root.bind('<Delete>', delete_task)

# Menu Bar
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff = 0)
file_menu.add_command(label = "Save", command = save_tasks)

edit_menu = tk.Menu(menubar, tearoff = 0)
edit_menu.add_command(label = "Clear list", command = clear_list)

reminder_menu = tk.Menu(menubar, tearoff = 0)
reminder_menu.add_command(label = "Enable reminders", command = remind)

menubar.add_cascade(label = "File", menu = file_menu)
menubar.add_cascade(label = "Edit", menu = edit_menu)
menubar.add_cascade(label = "Reminders", menu = reminder_menu)

root.config(menu = menubar)

# Frame
frame_tasks = tk.Frame(root)
frame_tasks.pack(fill = "both", expand = True)

# Listbox
listbox_tasks = tk.Listbox(frame_tasks, height = 400, width = 4)
listbox_tasks.pack (fill = "both", expand = True)

# Scrollbar
scrollbar_tasks = tk.Scrollbar(listbox_tasks)
scrollbar_tasks.pack(side = tk.RIGHT, fill = tk.Y)

# Assigns scrollbar to listbox
listbox_tasks.config(yscrollcommand = scrollbar_tasks.set)
scrollbar_tasks.pack(side = tk.RIGHT, fill = tk.Y)

# Right Click Menu
rc_menu = tk.Menu(listbox_tasks, tearoff = 0)
rc_menu.add_command(label = "Delete", command = delete_task)

# Entry box (for tasks)
entry_tasks = tk.Entry(root, width = 4)
entry_tasks.pack(fill = tk.X)

# Add task button
button_add_task = tk.Button(entry_tasks, text = "Add task", width = 8, command = add_task)
button_add_task.pack(fill = tk.Y, side = tk.RIGHT)

# Loads tasks list on open
load_tasks()

# Binds exit function to window close
root.protocol("WM_DELETE_WINDOW", on_exit)

root.mainloop()