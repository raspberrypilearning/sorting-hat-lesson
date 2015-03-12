# Software installation

This lesson can be completed using Python or Scratch.

You'll need to be online to install packages.

First update and upgrade your system. Enter the following commands in to the terminal:

```bash
sudo apt-get update
sudo apt-get upgrade
```

## Option 1: Python

You'll need to make sure you have the following packages installed to proceed with the workshop.

- python3-pibrella
- mpg123

Now install the packages you'll need:

```bash
sudo apt-get install mpg123 python3-pip
sudo pip-3.2 install pibrella
```

Test you have the Pibrella library installed by entering the following command:

```bash
sudo python3 -c "import pibrella"
```

If you get an error saying `No module named pibrella` then check you entered the commands above correctly.

Test you have the `mpg123` installed by entering the following command:

```bash
mpg123
```

If you get an error saying `The program 'mpg123' is currently not installed.` then check you entered the commands above correctly.

## Option 2: Scratch

Alternatively, you could use ScratchGPIO instead of Python, in which case the above packages are unneccessary but you'll need to install ScratchGPIO.

Install ScratchGPIO with the following commands:

```bash
wget http://goo.gl/xzJlz7 -O isgh6.sh
sudo bash isgh6.sh
```

and you'll find the ScratchGPIO icon on the desktop.

## Audio Files

Students will need the following audio files to announce the house they will sort students into. You can download them from the command line using the wget command:

```bash
wget http://teachwithict.weebly.com/uploads/5/5/8/2/5582303/ravenclaw.mp3
wget http://teachwithict.weebly.com/uploads/5/5/8/2/5582303/slytherin.mp3
wget http://teachwithict.weebly.com/uploads/5/5/8/2/5582303/hufflepuff.mp3
wget http://teachwithict.weebly.com/uploads/5/5/8/2/5582303/gryffindor.mp3
```

Or save the files from the web browser:

- [ravenclaw.mp3](http://teachwithict.weebly.com/uploads/5/5/8/2/5582303/ravenclaw.mp3)
- [slytherin.mp3](http://teachwithict.weebly.com/uploads/5/5/8/2/5582303/slytherin.mp3)
- [hufflepuff.mp3](http://teachwithict.weebly.com/uploads/5/5/8/2/5582303/hufflepuff.mp3)
- [gryffindor.mp3](http://teachwithict.weebly.com/uploads/5/5/8/2/5582303/gryffindor.mp3)

Alternatively, students could record their own sounds.
