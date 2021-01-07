# to-do-list
To Do List with Reminder Notifications

Note: Ensure that .exe or .py are in the same folder as image files and .dat files and that the file names for images and .dat stay the same.

This is a basic to-do list that I created for my personal use in Python using Tkinter and win10toast libraries. It saves tasks from the user to a .dat file (tasks.dat) which must be saved in the same folder as the .exe or source code (or .py file)

Use .exe for practical use and right click to create shortcut to desktop.

Use to-do-1.py to edit the code.

Reminders can be enabled from the menu bar that by default occur ever hour in the form of Windows notifications. It also informs the user of how many tasks are on the list at the time.

To change the interval for reminders, change the number in the root.after() function (line 60 of source code) to desired time in milliseconds. (Currently at 3600000 milliseconds, or one hour).

Selected tasks can be deleted via right click menu or Delete key.

Common key binds for saving (Ctrl+S), closing window (Ctrl+W), and adding tasks (Return) have also been included for added functionality.

