TribeRecord + GUI
=================
_Learning Objective: Create a graphical user interface (GUI)_

Introduction
------------
In an earlier lab we built the `TribeRecord` class. In this lab exercise, we will reuse that class for this program and add a graphical user interface (GUI) to collect input. When the user submits their data, a new `TribeRecord` object will be instantiated and formatted output printed to a file.

Step 1: Import Tkinter
----------------------
Check out this site for a brief summary of how to use Tkinter to make GUIs in Python: [Tkinter Cheat Sheet](https://www.geeksforgeeks.org/tkinter-cheat-sheet/)

You will need to `import Tkinter` then put the following two lines:

```
root = Tk()
root.mainloop()
```

Step 2: Create your widgets
---------------------------
In your GUI include labels and entry or text widgets for each piece of information needed from the user. You must also include a checkbox to indicate whether the tribe is still active or not. Between the two lines of code from Step 1 you will create your widgets and add them to the GUI. Below is an example of what the GUI could look like.

![active example of tribe record GUI](https://i.imgur.com/5Acz5LK.png)

There are multiple choices you could make here, but the code below is an example of creating one widget and adding it to the GUI.

```
tname_label = Label(root, text="Tribe Name")
tname_label.grid(row=0, column=0)
```

Step 3: Define your actions
---------------------------
There are two events in your GUI that should trigger actions: checking/unchecking the checkbox, and clicking the submit button.

1. If the checkbox is checked, then the current status prompts must be set to empty and disappear from the GUI. Below is what the GUI could look like when the box is checked.

![no longer active example of tribe record GUI](https://i.imgur.com/nrXWQWx.png)

2. The second event to expect is the user clicking the submit button. When this happens, your program must create a `TribeRecord` object using the provided data from the user, then print the resulting object to file. Use the append option for the file so that it adds to the file rather than replacing what is already there. This way, you could store a list of tribes.

If you have not completed the original `TribeRecord` lab where you made the class, we provided a partial one to allow you to complete this current lab. The partial `TribeRecord` class provided has only two methods, **`init`** and **`str`**, essential to making your GUI lab's submit button work.

Step 4: Test With Real Data
---------------------------
Run your program and enter real data for two tribes. One should still be active so you can check that all of the data fields are working correctly. The second tribe should no longer be active so that you can ensure the checkbox is working appropriately. You may use the data you or a peer posted in the prep discussion.

Submit
------
There are no automated tests for this lab. Use the following checklist to see if your program has all necessary components.

*   Has a GUI with prompts and a way for user to type data for each instance variable of the `TribeRecord`.
*   Has a checkbox which when checked/unchecked adds or removes the current status fields as appropriate.
*   Has a submit button which when clicked instantiates a `TribeRecord` object and prints it to file (by appending not replacing).
*   Two (or more) tribes are saved in the file to show that you completed Step 4.

If you want to play around with it and add color, a completion message, or any other personalization then go for it! Just make sure that all of the above requirements are still met.