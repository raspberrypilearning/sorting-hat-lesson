# Teacher Setup Instructions


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

