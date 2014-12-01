# Lesson 1 - Sorting Hat

## Introduction
In this lesson, students will create a Raspberry Pi powered Harry Potter style sorting hat. Students will also learn how to connect a physical button to the Pibrella and program it to control the sorting hat.

## Learning Objectives
- Know that computer programs can make decisions, and that a simple form of decision is called a conditional (If, Else and Else if).
- Be able to devise a program to randomly sort students into different groups or houses.

## Learning Outcomes:
**All students are able to:**
- Use an if statement.
- Begin to write a function containing conditionals (if, else and else if) to randomly return a house name with support.

**Most students are able to:**
- Modify code in the `if` branches to create different execution paths.
- Write a function containing conditionals (if, else and else if) to randomly return a house name with minimal support

**Some students are able to:**
- Write a complete program in Python 3 using functions, while and for loops and conditionals (if, else and else if) with minimal support.

## Lesson Summary
- Introduction to setting up a Raspberry Pi
- Writing a python program using functions, loops and conditionals.

## Starter
Read pages pages 85 - 97 from [Harry Potter and the Philosopher's Stone](http://www.amazon.co.uk/Harry-Potter-Philosophers-Stone-Rowling/dp/0747558191) to the class (this could have been set as homework from the priovous lesson) or alternatively if you have access to the Harry Potter and the Philosopher's Stone Film, play the sorting hat clip. You could also ask students to sort themselves into the four houses of ravenclaw, slytherin, hufflepuff and gryffindor just for fun and discuss their reasoning. 

## Main Development
1. Demonstrate the final sorting hat project to the class by selecting students, asking them to wear the hat and then asking another student to press the button. Discuss with students what do they think is needed to make the project. Draw out through questioning and list on the board all the component pieces. Ask students to tell you if they are hardware or software related.

1. Direct students to attach their Pibrella to the Raspberry Pi. See [student instructions](student-instructions.md) to complete this task.
 *WARNING! The Raspberry Pi must be shutdown before connecting to GPIO.* 

1. Ask students to set up the rest of their Raspberry Pi equipment, turn it on and log into their Pi using the username `pi` and the password `raspberry`.
  *Note that students will not see any text when typing the password but assure them it is working. Why do they think this might   be the case? Hint: what might happen if someone was looking over their shoulder?*

1. Next, students should load the graphical environment by typing `startx`. Once the desktop has loaded, students should be directed to load LXTerminal by double clicking on the desktop icon. Once loaded, they should type `sudo idle3 &` to load the Python 3 programming environment IDLE3 as the super user, sso that they can access the GPIO pins with their code.
  *Note that this series of lessons uses Python 3. If students run IDLE then their code may not run.*
  Explain to students that **IDLE3** is an application or environment that allows you to write a simple program using the programming language Python. It allows you to write, edit and run code. 

1. Ask students to click on **File** and **New Window** to open a blank text editor window. They should be directed to then click on **File** and **Save As**. They should save their file as `sorting-hat.py`.

1. Recap with students the syntax for importing modules. Remind students of the list they created at the start of the lesson about the component parts they would need for the project to work. Draw out through questioning the following syntax and ask students to type it in:

 ```python
 import pibrella
 import time
 import random
 import os
 ```
 
 Students may not have come across the python library `os`. This allows you to execute a shell command as if you were using the command line interface. 
 
1. At this point you could set the students the task of trying to create the program depending on the ability and prior learning. You may wish to write out parts of the code and ask them to complete just the conditionals. 

 All the steps to completing this program can be found in the [student instructions](student-instructions.md). The final code is also avaliable to you.  

## Plenary
Direct students to swap seats with another pair or group. They have a few minutes to test the other groups' programs, and suggest at least one improvement by writing a comment using the # symbol. Students should then return to their programs and make the suggested improvement.

## Extension

- Connect multiple LEDs (One for each Hogwarts House / Group) and make each one flash depending on which house / group is picked
- Ask students to record their own audio (These could be houses in your school, colours or numbers)
- Add a second switch which will power up the Raspberry Pi and launch the python script on startup.
