# Teacher Setup Instructions

For this lesson students will need access to:

- A Raspberry Pi
- A keyboard and mouse connected to the RPi
- A monitor connected to the RPi
- Latest NOOBS SD card with Raspbian installed (instructions below)
- Pibrella Python 3 Library on each SD card (instructions below)
- Alternatively you could use Scratch GPIO for this lesson which needs to be installed on each SD card (instructions below)

## Downloading and installing NOOBS

Instructions for best practice on [downloading and installing NOOBS can be read here](https://github.com/raspberrypi/documentation/blob/master/installation/noobs.md).

## Installing additional libraries
You will need to install the following libraries in order for the sorting hat to work:
- Pibrella (This allows you to communicate with the GPIO pins via the Pibrella on the Raspberry Pi)
- mpg123 (This will allow you to play the audio files)

In order to create the sorting hat, students will need to install some additional library packages required for Python:

1. Start by launching LXTerminal by double clicking on LXTerminal desktop icon.
1. Before installing new libraries, it's always a good idea to update the raspbian operating system first. To upgrade the operating system type: `sudo apt-get update` and press **enter**.
1. Once complete download and install pip by typing `sudo apt-get install python3-pip` and pressing **enter** on the keyboard.
1. Next install pibrella library by typing `sudo pip3.2 install pibrella`
1. Finally, install the the mpg123 library by typing `sudo apt-get install mpg123`

## Alternative: Downloading and Installing Scratch GPIO

Instructions on how to [download and install the latest version can be read here](http://cymplecy.github.io/scratch_gpio/).

## Download the Audio Files

Students will need the following audio files to announce the house they will sort students into. Alternatively they could make their own.
- [ravenclaw.mp3](http://teachwithict.weebly.com/uploads/5/5/8/2/5582303/ravenclaw.mp3)
- [slytherin.mp3](http://teachwithict.weebly.com/uploads/5/5/8/2/5582303/slytherin.mp3)
- [hufflepuff.mp3](http://teachwithict.weebly.com/uploads/5/5/8/2/5582303/hufflepuff.mp3)
- [gryffindor.mp3](http://teachwithict.weebly.com/uploads/5/5/8/2/5582303/gryffindor.mp3)

## Making a class set of SD cards

Once you have completed the steps above, you can make a copy of your master SD card and then use that to make a class set.

1. Place your master SD card in a computer or laptop with an SD card reader. 
2. On Windows use [Win disk 32 imager](http://sourceforge.net/projects/win32diskimager/) to make a copy of an SD card. On Mac OSX you can use the `dd` command or a [dd-gui](http://www.gingerbeardman.com/dd-gui/).
3. Remove the master SD card and keep it safe.
4. Take a fresh SD card and insert it into your computer or laptop. 
5. Format the SD card then, using your imaging software, select the image and write it to the card.
6. Repeat the last step for the rest of your cards. 
