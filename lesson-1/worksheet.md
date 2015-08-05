# Make a Sorting Hat

In this lesson you'll use Python and the Pibrella to create a Sorting Hat application on the Raspberry Pi, so that when you press the button on the Pibrella, it will speak the name of a randomly selected house.

## Setting up your Pibrella

You will need a Pibrella board attached to the GPIO pins on your Raspberry Pi for this lesson. Attach your Pibrella by pushing the connector over the top of the first 26 pins of your Raspberry Pi.

![](images/setup-pibrella.jpg)

## Boot your Raspberry Pi

Now add the rest of the peripherals to your Raspberry Pi, add the power to turn it on, and wait for it to boot. Log into your Raspberry Pi when prompted with the login: `pi` and the password `raspberry`.

## Load IDLE3 as the superuser

1. Load the graphical environment by typing `startx`. Once the desktop has loaded, double-click on the **LXTerminal** desktop icon. 
1. Then type `sudo idle3 &` to load the Python 3 programming environment IDLE3 as the superuser, so that you can access the GPIO pins with your code.

    *Note that this lesson uses Python 3. If you open IDLE instead of IDLE3, your code may not run.*
  
    **IDLE3** is an application or environment that allows you to write a simple program using the programming language Python. It allows you to write, edit and run code. 

1. Click on **File** and **New Window** to open a blank text editor window, then click on **File** and **Save As**. Save your file as `sorting-hat.py`.

## Importing Python libraries

To begin your Sorting Hat program you will need to import all the Python libraries that allow you to control various aspects of your code. For example, you will need the `time` library in order to add pauses or sleeps to your code. You will also need the `random` library so that a house can be selected at random.

 ```python
 import pibrella
 import time
 import random
 import os
 ```
 
You may not have used the Python library `os` before. This allows you to execute a shell command from your code as if you were using the command line interface. You will need this in order to play an mp3 file.
 
## Defining a function

Next, create a function in which to place your code. You can then call this function repeatedly inside a loop later on. To define a function in Python use the word `def` followed by a name for the function, for example:

```python
def randomgenerator():
```

## Using a variable to store a random number

In this program you want to pick a house at random, so we are going to assign each house a number between 1 and 4. The number will be selected at random and stored inside a variable. Much like functions, you could use any variable name; here we have used the name `number`. 

```python
def randomgenerator():
    number = random.randint(1, 4)
```

`random.randint(1, 4)` will return a random integer between 1 and 4. 

## If, elif and else

Now that your code will generate a random number, you will need to set the conditions for what happens if the number that is generated equals 1. To do this in Python, we can use the word `if`.

```python
    if number == 1:
        os.system('mpg123 gryffindor.mp3')
        time.sleep(1)
```

The first line states that if the number (which is the variable containing the random integer between 1 and 4) is equal to 1 (`==` in Python represents 'equal to'), play the Gryffindor audio file then wait for 1 second.

Let's set the condition for the number 2.

```python
    elif number == 2:
        os.system('mpg123 hufflepuff.mp3')
        time.sleep(1)
```

This time we have used the word `elif`; this means **else if**. Else if the number is equal to 2, then play the Hufflepuff audio file. 

What would you type for the number 3 and the number 4?

## The program loop

If you save and run your program now nothing will happen. That is because all the code is stored inside a function. You now need to write the code that will call that function. As you want to be able to press the button again and again, each time randomly selecting a house, the function will need to be called again and again. We can use a `while True:` loop to do this.

You could just type:

```python
while True:
    randomgenerator()
```

then save and run your Python file by clicking on **Run** and **Run Module**. Your random generator will kick out a house name every second. Your Sorting Hat will be efficient, but there might not be enough time to move the hat onto another head! Instead, we can make use of the button in the loop:

```python
while True:
    if pibrella.button.read():
        randomgenerator()
```

Now save and run your code. This time the program will wait for the button to be pressed before it calls the function.

![](images/sorting-hat-code.png)

## What next?

- Try recording your own sounds!
- What else could you use the same code for?
- Can you do the same project with less code? How could it be more efficient?
- Can you do the same project without a Pibrella? Try using a button and a breadboard!
