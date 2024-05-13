import pyautogui
import math
import time
import keyboard

# Function to move the mouse in a circular motion while clicked
def move_in_circle(center_x, center_y, radius):
    angle = 0
    while angle < 2 * math.pi:  # One full rotation
        x = center_x + int(radius * math.cos(angle))
        y = center_y + int(radius * math.sin(angle))
        pyautogui.mouseDown()
        pyautogui.moveTo(x, y, duration=0.001)  # Convert speed to seconds
        angle += 0.2  # Adjusted angle increment for smoother circle
        print(angle)
    pyautogui.mouseUp()

# Function to detect Esc key press
def detect_esc_key():
    while True:
        if keyboard.is_pressed('esc'):
            return True

# Get the screen dimensions
screen_width, screen_height = pyautogui.size()
center_x = screen_width // 2
center_y = screen_height // 2
radius = 270

# Start detecting Esc key press
if detect_esc_key():
    # Offset the pointer by radius
    pyautogui.moveTo(center_x + radius, center_y, duration=0.5)
    # Move in a circular motion while clicked
    move_in_circle(center_x, center_y, radius)
