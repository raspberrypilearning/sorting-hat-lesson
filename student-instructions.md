# Student Instructions

## Setting up your [Pibrella](http://pibrella.com/#setup)

You will need a Pibrella board attached to the GPIO pins on your Raspberry Pi for this lesson. Attach your Pibrella by pushing the connector over the top of the first 26 pins of your Raspberry Pi.

![](images/pibrella-setup.png)


## Boot your Raspberry Pi

Now add the rest of the peripherals to your Raspberry Pi, add the power to turn it on, and wait for it to boot. Log into your Raspberry Pi when prompted with the login: `pi` and the password `raspberry`.

## Load IDLE3 as the Super User

1. Load the graphical environment by typing `startx`. Once the desktop has loaded, double clicking on the **LXTerminal** desktop icon. 
1. Then type `sudo idle3 &` to load the Python 3 programming environment IDLE3 as the super user, so that you can access the GPIO pins with your code.
  *Note that this lesson uses Python 3. If you open IDLE then your code may not run.*
  
  **IDLE3** is an application or environment that allows you to write a simple program using the programming language Python. It   allows you to write, edit and run code. 

1. Click on **File** and **New Window** to open a blank text editor window. Then click on **File** and **Save As**. Save your file as `sorting-hat.py`.

## Importing Python Libraries

To begin your sorting hat program you will need to import all the python libraries that allow you to control various aspects of your code. For example, you will need the time library in order to add pauses or sleeps to your code. You will also need the random library so that a house can be selected at random.

 ```python
 import pibrella
 import time
 import random
 import os
 ```
 
 You may not have used the python library `os` before. This allows you to execute a shell command from your code as if you were using the command line interface. You will need this in order to play an mp3 file.
 
## Defining a Function

Next use a function in which to place your code. You can then call this function repeatedly inside a loop later on. To define a function in python use the word `def` followed by a name for the function, for example:

```python
def randomgenerator():
```

## Using a Variable to store a Random Number

In this program you want to pick a house at random. So we are going to assign each house a number between 1 and 4. The number will be selected at random and stored inside a variable. Much like functions, you could use any variable name. Here we have used the name `number`. 

```python
def randomgenerator():
    number = random.randint(1, 4)
```
random.randint(1, 4) will return a random integer between 1 and 4. 

## If, Elif and Else

Now that your code will generate a random number, you will need to set the conditions for what happens if the number that is generated equals 1. To do this in python, we can use the word `if`.

```python
    if number == 1:
        os.system('mpg123 gryffindor.mp3')
        time.sleep(1)
```

The first line states that if the number (which is the variable containing the random integer between 1 and 4) is equal to (we use `==` in python to represent equal to) 1, then ply the gryffindor audio file. Then wait for 1 second.

Let's set the condition for the number 2.

```python
    elif number == 2:
        os.system('mpg123 hufflepuff.mp3')
        time.sleep(1)
```

This time we have used the word `elif` this means **else if**. Else if the bumber is equal to 2 then play the hufflepuff audio file. 

What would you type for the number 3 and the number 4?

## The program loop



