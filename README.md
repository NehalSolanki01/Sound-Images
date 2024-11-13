# 1 Countdown Timer with Sound Notification

This Python script is a simple countdown timer that allows you to set a time in seconds. It displays the countdown in the format `MM:SS` (minutes:seconds) and plays a sound when the time is up.

## Requirements

- Python 3.x
- `winsound` module (included in the standard library on Windows)

## Features

1. **Countdown Timer**: 
   - The timer will display the time remaining in the format `MM:SS` (minutes:seconds).
   - The countdown decreases every second until it reaches zero.
   
2. **Sound Notification**:
   - When the timer reaches zero, a sound is played using the `winsound` module.

3. **Input Validation**:
   - The user is prompted to enter a valid number of seconds.
   - The script ensures the input is a positive integer and handles invalid inputs.

## How It Works

1. **Enter Time in Seconds**:  
   The user enters the time in seconds (a positive integer).
   
2. **Countdown Display**:  
   The script shows the countdown in `MM:SS` format. It updates every second until the timer reaches zero.
   
3. **Play Sound on Completion**:  
   Once the countdown finishes, the script plays a sound from a `.wav` file specified in the script.

## Usage

### Steps to Run

1. **Update the Sound File Path**:  
   Make sure the path to the sound file is correct. The script currently uses:
   ```python
   winsound.PlaySound(r"c:\Users\HP EliteBook 840 G4\Music\acoustic-guitar-loop-f-91bpm-132687.wav", winsound.SND_FILENAME)
   ```
   Replace this path with the location of a `.wav` file you wish to use for the sound notification.

2. **Run the Script**:  
   Open a Python environment and run the script.

3. **Input Time**:  
   Enter the number of seconds for the countdown when prompted.

4. **Listen for the Sound**:  
   Once the countdown reaches zero, the sound file will play to notify you that the time is up.

## Notes

- This script works only on Windows due to the use of the `winsound` module for sound playback.
- Ensure that the sound file path is correct to avoid errors.
- The script assumes the user will enter a valid positive integer for the countdown.

## If you want to replace `winsound` (which is Windows-specific) with a cross-platform solution, you can use other libraries such as:

1. **`pygame`**: A popular library that can play sound on both Windows, macOS, and Linux.

2. **`playsound`**: A simple and lightweight library for playing sound files in any Python environment.

3. **`pydub`**: A powerful audio manipulation library, but it requires `pydub` and `ffmpeg` to work with sound files.

### 1. Using `pygame` for sound

First, you need to install `pygame`:

```bash
pip install pygame
```

Then, you can replace `winsound` with `pygame` like this:

```python
import time
import pygame

# Initialize the mixer
pygame.mixer.init()

# Function Definition
def countdown_timer(seconds):
    while seconds > 0:
        mins = int(seconds / 60)
        secs = int(seconds % 60)
        timer = f'{mins:02d}:{secs:02d}'  # Format with leading zeros
        print(timer, end="\r")  # Use carriage return to overwrite the line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1

    # Play a sound when time is up
    print("Time's up!")
    pygame.mixer.music.load(r"c:\path\to\sound.wav")  # Path to your sound file
    pygame.mixer.music.play()

# Input time in seconds
seconds = input("Enter the time in seconds: ")

# Function call
countdown_timer(int(seconds))
```

### 2. Using `playsound` for sound

The `playsound` module is another easy-to-use solution, especially if you just want to play a sound without additional functionality like mixing or volume control.

First, install `playsound`:

```bash
pip install playsound
```

Then, replace `winsound` with `playsound`:

```python
import time
from playsound import playsound

# Function Definition
def countdown_timer(seconds):
    while seconds > 0:
        mins = int(seconds / 60)
        secs = int(seconds % 60)
        timer = f'{mins:02d}:{secs:02d}'  # Format with leading zeros
        print(timer, end="\r")  # Use carriage return to overwrite the line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1

    # Play a sound when time is up
    print("Time's up!")
    playsound(r"c:\path\to\sound.wav")  # Path to your sound file

# Input time in seconds
seconds = input("Enter the time in seconds: ")

# Function call
countdown_timer(int(seconds))
```

### 3. Using `pydub` for sound

If you need advanced audio features or support for various audio formats, `pydub` is a great option. However, you also need to install `pydub` and `ffmpeg`.

First, install `pydub`:

```bash
pip install pydub
```

And make sure you have `ffmpeg` installed (you can follow [this guide](https://github.com/jiaaro/pydub#dependencies) for installing `ffmpeg`).

Then you can use `pydub` like this:

```python
import time
from pydub import AudioSegment
from pydub.playback import play

# Function Definition
def countdown_timer(seconds):
    while seconds > 0:
        mins = int(seconds / 60)
        secs = int(seconds % 60)
        timer = f'{mins:02d}:{secs:02d}'  # Format with leading zeros
        print(timer, end="\r")  # Use carriage return to overwrite the line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1

    # Play a sound when time is up
    print("Time's up!")
    sound = AudioSegment.from_wav(r"c:\path\to\sound.wav")  # Path to your sound file
    play(sound)

# Input time in seconds
seconds = input("Enter the time in seconds: ")

# Function call
countdown_timer(int(seconds))
```

### Summary of Libraries:
- **`pygame`**: Cross-platform (Windows, macOS, Linux) and supports advanced sound features.
- **`playsound`**: Simple, lightweight, and cross-platform; works well for basic sound playback.
- **`pydub`**: Powerful, supports many formats, but requires additional setup with `ffmpeg`.

If you just need basic functionality, **`playsound`** is the easiest option. If you want more control over the sound or support for various audio formats, **`pygame`** or **`pydub`** would be better choices.

___________________________________________________________________________________________________________________________________________________________________

# 2. Dice Roller App

This is a simple Dice Roller application built using Python's `tkinter` and `Pillow` (for image handling) libraries. The app allows users to roll a virtual dice, displaying a random dice face along with a sound effect.

## Features

- **Dice Rolling**: The user can click a "Roll Dice" button to simulate a dice roll, displaying one of six possible dice faces.
- **Sound Effect**: A beep sound is played when the dice is rolled, adding to the interaction.
- **Images**: Each dice face is represented by an image (dice1.png, dice2.png, etc.) that gets updated on the screen with every roll.
- **Exit Button**: There is an exit button to close the application.

## Requirements

- Python 3.x
- `tkinter` (for GUI functionality) - This comes pre-installed with Python.
- `Pillow` (for image processing) - Install using:
  ```bash
  pip install pillow
  ```

## File Setup

Make sure you have the following dice images (dice1.png, dice2.png, dice3.png, dice4.png, dice5.png, dice6.png) available in the same directory as the script. The images should represent the faces of the dice (1 to 6).

## How to Run

1. **Prepare the Images**:  
   Ensure you have the dice images (dice1.png, dice2.png, etc.) in the same folder as the script. You can resize them if needed, but the app resizes them to fit the window.

2. **Install Pillow**:  
   If you don’t have the Pillow library installed, use the following command to install it:
   ```bash
   pip install pillow
   ```

3. **Run the Script**:  
   Once everything is set up, you can run the script in your Python environment. The window will open, displaying the initial dice image (dice1.png).

4. **Interact with the App**:  
   - Click the "Roll Dice" button to roll the dice, which will display a random dice face (from 1 to 6).
   - Click the "Exit" button to close the application.

## Code Explanation

- **Dice Roll Function**: The `roll_dice` function generates a random number between 1 and 6, and updates the displayed image of the dice accordingly.
- **Sound Effect**: A sound is played using `winsound.Beep()` when the dice is rolled.
- **Image Handling**: Dice images are loaded using `Pillow`, resized to fit the window, and displayed using `tkinter.Label`.


## Notes

- **Windows Only**: The `winsound` module used for the sound is only available on Windows.
- **Image Formats**: Make sure the dice images are in `.png` format and are named `dice1.png`, `dice2.png`, ..., `dice6.png`. The images should be placed in the same directory as the script.
- **Customizing Dice Faces**: You can customize the dice images to suit your needs, as long as the image filenames are in the correct order (dice1.png, dice2.png, etc.).

