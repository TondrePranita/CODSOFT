# Importing all the necessary modules
from tkinter import *

# Functions for adding and deleting task
def add_item(entry: Entry, listbox: Listbox):
    new_task = entry.get()

    listbox.insert(END, new_task)

    with open('task1.txt', 'a') as tasks_list_file:
        tasks_list_file.write(f'\n{new_task}')


def delete_item(listbox: Listbox):
    listbox.delete(ACTIVE)

    with open('tasks.txt', 'r+') as tasks_list_file:
        lines = tasks_list_file.readlines()

        tasks_list_file.truncate()

        for line in lines:
            if listbox.get(ACTIVE) == line[:-2]:
                lines.remove(line)
            tasks_list_file.write(line)

        tasks_list_file.close()


# Initializing the GUI window
root = Tk()
root.title('To-Do-List')
root.geometry('300x400')
root.resizable(0, 0)
root.iconbitmap('img.ico')
root.config(bg="#58b6a2")

# Heading Label
F1 = Frame(root, bg='#072853')
F1.pack(side=TOP,fill='x')

L1 = Label(F1,text='ALL TASKS', bg='#072853',fg='white',font="Helvetica 20 bold")
L1.pack()

# Listbox with all the tasks with a Scrollbar
task_box = Listbox(root, bg='#e8e6e5', fg='black', font=('Helvetica', 12), height=12, width=23)

scroller = Scrollbar(root, orient=VERTICAL, command=task_box.yview)
scroller.place(x=260, y=60, height=232)

task_box.config(yscrollcommand=scroller.set)

task_box.place(x=40, y=60)

# Adding items to the Listbox
with open('task1.txt', 'r+') as tasks_list:
    for task in tasks_list:
        task_box.insert(END, task)
    tasks_list.close()

# Creating the Entry widget where the user can enter a new item
new_item_entry = Entry(root, width=31, bg='#efe2f4', font=('Helvetica', 10), relief='ridge',borderwidth='2')
new_item_entry.place(x=35, y=310)

# Creating the Buttons
add_btn = Button(root, text='Add Item', bg='black',fg='white', width=10, font=('Helvetica', 12),
                 command=lambda: add_item(new_item_entry, task_box))
add_btn.place(x=45, y=350)

delete_btn = Button(root, text='Delete Item', bg='black',fg='white', width=10, font=('Helvetica', 12),
                 command=lambda: delete_item(task_box))
delete_btn.place(x=150, y=350)

# Finalizing the window
root.update()
root.mainloop()