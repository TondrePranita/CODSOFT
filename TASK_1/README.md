# To Do List Application :
To-Do Lists are actually a list of your daily tasks that you keep on your person to remind yourself of the tasks you have to accomplish that day. In this project, I have made a GUI based python to-do list with options to add and delete items in the list using the Tkinter module and File I/O.
<br />
<br />
The files required in to-do list project are:
1. task1.txt – The text file where all our tasks will be stored
2. Task_1.py – The python script file
<br />
Here are the steps you will need to execute to build this python project:<br /><br />
Step 1 : Importing all the necessary libraries.<br />
Step 2 : Initializing the window and placing all the components in it.<br />
Step 3 : Creating the add_item and delete_item functions.<br />
<br />
<br />
To initialize the to-do list window, you need to initialize the Tk() class to a variable. Then, you need to set the following attributes:<br />
' title() ' method is used to give a title to the project window.<br />
' geometry() ' method is used to set the initial geometry of window.<br />
' resizable() ' method is used to allow/deny the user the permission to resize the python to-do list window. It takes truthy and falsy values and arguments to the parameters width and height.<br />
' config() ' method is used to configure some extra attributes of the window, like bg or background to set the background color.<br />
' update() ' and .mainloop() methods are used to put the window in a loop to prevent it from closing nanoseconds after it opens.<br />
<br />
<br />
The Label class is used to create a label that displays the static screen on the window and set the following parameters to it:<br />
' text attribute ' - is used to mention the text that will be displayed on the label.<br />
' font ' - is used to specify the font family, size and effects on the text.
<br />
<br />
The Button class is used to create a button on the screen that executes a function as a command when pressed.
command attribute is the function that will run when the button is pressed. 
Width attribute is the width of the button in pixels.
<br />
<br />
The Entry class is used to add an input widget to the window that accepts input data from the user.
The .get() method is used to get the text inputted by the user.
<br />
<br />
The Listbox class is used to add a list box to the window that displays multiple items on the screen.
<br />
<br />
The Scrollbar class is used to add a scroll bar to the widget on the window to navigate up and down, or right to left in said widget.
<br />
<br />
In the add_item function, we will give the Entry object’s user-provided text to a variable and then insert that variable to the last of our listbox object.
In the delete_item function, the user will give the function one argument that will be a listbox object. In this function, we will delete the item selected in the listbox object.line of our text file.

# Output :
![Screenshot (3)](https://github.com/TondrePranita/CODSOFT/assets/138645068/de334fa3-3caa-4ecb-ac0f-2413ba73bdc7)


