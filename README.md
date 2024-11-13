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

