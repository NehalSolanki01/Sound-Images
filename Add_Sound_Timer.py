import time
import winsound  # For sound

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
    winsound.PlaySound(r"c:\Users\HP EliteBook 840 G4\Music\acoustic-guitar-loop-f-91bpm-132687.wav", winsound.SND_FILENAME)  # Beep when timer ends

# Input time in seconds
seconds = input("Enter the time in seconds: ")

# Function call
countdown_timer(int(seconds))
