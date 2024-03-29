import tkinter as tk
from tkinter import messagebox
import pygame
from PIL import Image, ImageTk  # Import Image and ImageTk modules from PIL


# Initialize pygame mixer
pygame.mixer.init()

# Load sound effects
pick_up_sound = pygame.mixer.Sound("mixkit-casino-bling-achievement-2067.wav")
move_sound = pygame.mixer.Sound("coin_c_02-102844.mp3")

# Map of the game
rooms = {
    'Start': {'North': 'Hagrid', 'South': 'Chamber', 'East': 'Friends'},
    'Hagrid': {'South': 'Start','East': 'Market', 'Item': 'Cloak'},
    'Chamber': {'North': 'Start','East':'Dumbledore', 'Item': 'Diary'},
    'Friends' : {'West': 'Start','East': 'Hogwards', 'South': 'Dumbledore', 'Item': 'Bond'},
    'Market' : {'East': 'Snape','West':'Hagrid','Item': 'Wand'},
    'Snape': {'West': 'Market', 'Item': 'Truth'},
    'Dumbledore': {'North': 'Friends','West':'Chamber', 'Item': 'Memory'},
    'Hogwards': {'West': 'Friends','Boss': 'Voldemort'}
}

# Inventory list
inventory=[]



# Function to move to a new room
# Function to move to a new room
def move(direction):
    global current_room
    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
        update_display()
        play_sound(move_sound)
        
        if current_room == 'Hogwards' and 'Boss' in rooms[current_room]:
            if len(inventory) < 6:
                description = "You lost the fight with Voldemort because you don't have all six items."
            else:
                description = "Congratulations! You defeated Voldemort with all six items!"
            label.config(text=description)
    else:
        messagebox.showinfo("Error", "You can't go that way.")



# Function to pick up an item
def pick_up():
    global current_room
    global inventory
    if "Item" in rooms[current_room]:
        item = rooms[current_room]["Item"]
        if item not in inventory:
            inventory.append(item)
            update_display()
            play_sound(pick_up_sound)
        else:
            messagebox.showinfo("Info", f"You already have the {item}.")
    else:
        messagebox.showinfo("Info", "There is no item here.")

# Function to update the display with room information and inventory
def update_display():
    description = f"You are in {current_room}\n"
    if "Item" in rooms[current_room]:
        description += f"You see a {rooms[current_room]['Item']} here.\n"
    else:
        description += "There are no items here.\n"
    description += f"Inventory: {inventory}"
    label.config(text=description)

# Function to play sound
def play_sound(sound):
    sound.play()

# Function to play background music
def play_music():
    pygame.mixer.music.load("bg music.mp3")
    pygame.mixer.music.play(-1)  # -1 means loop indefinitely

# Function to stop background music
def stop_music():
    pygame.mixer.music.stop()

# Initialize GUI
root = tk.Tk()
root.title("Text Adventure Game")

# Create label for displaying room information
label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=300)
label.pack(pady=10)

# Create buttons for movement
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

north_button = tk.Button(button_frame, text="North", command=lambda: move("North"))
north_button.grid(row=0, column=1)

south_button = tk.Button(button_frame, text="South", command=lambda: move("South"))
south_button.grid(row=2, column=1)

east_button = tk.Button(button_frame, text="East", command=lambda: move("East"))
east_button.grid(row=1, column=2)

west_button = tk.Button(button_frame, text="West", command=lambda: move("West"))
west_button.grid(row=1, column=0)

# Create button for picking up item
pick_up_button = tk.Button(root, text="Pick Up Item", command=pick_up)
pick_up_button.pack()

# Create buttons for music control
music_frame = tk.Frame(root)
music_frame.pack(pady=10)

play_music_button = tk.Button(music_frame, text="Play Music", command=play_music)
play_music_button.grid(row=0, column=0, padx=10)

stop_music_button = tk.Button(music_frame, text="Stop Music", command=stop_music)
stop_music_button.grid(row=0, column=1, padx=10)

# Load and display image
image = Image.open(r"C:\Users\Nandhikaa Narayanani\Desktop\text based game\images\at_hogwards.png")

photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo)
image_label.image = photo  # Keep a reference to avoid garbage collection
image_label.pack()


# Set initial room and update display
current_room = "Start"
update_display()

root.mainloop()







