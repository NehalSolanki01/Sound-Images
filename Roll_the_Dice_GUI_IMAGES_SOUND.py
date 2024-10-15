import tkinter as tk
import random
import winsound
from PIL import Image, ImageTk  # You need to install Pillow: pip install pillow

# Function to roll the dice and update the image
def roll_dice():
    dice_value = random.randint(1, 6)
    # Update the label with the corresponding dice image
    dice_img_label.config(image=dice_images[dice_value - 1])
    dice_img_label.image = dice_images[dice_value - 1]  # Keep a reference to avoid garbage collection

    # Play a sound when rolling the dice
    winsound.Beep(frequency=1000, duration=200)  # You can adjust the frequency and duration

# Creating the main window
root = tk.Tk()
root.title("Dice Roller")

# Load dice images (you need to have dice1.png, dice2.png, etc.)
dice_images = []
for i in range(1, 7):
    image = Image.open(f"dice{i}.png")  # Make sure the images are in the same directory
    image = image.resize((100, 100), Image.LANCZOS)  # Resize to fit the GUI
    dice_images.append(ImageTk.PhotoImage(image))

# Initial dice image
dice_img_label = tk.Label(root, image=dice_images[0])
dice_img_label.pack(pady=20)

# Creating a button to roll the dice
roll_button = tk.Button(root, text="Roll Dice", command=roll_dice, font=("Helvetica", 16))
roll_button.pack(pady=20)

# Creating a button to exit the application
exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Helvetica", 16))
exit_button.pack(pady=20)

# Running the tkinter main loop
root.mainloop()
