import cv2
import numpy as np
from PIL import Image

# Paths to input and output files
foreground_image_path = '/content/Nuke.jpg'  # The nuclear explosion image
background_image_path = '/content/City.jpg'  # The background cityscape
output_gif_path = '/content/City_With_Nuke.gif'

# Load the images
foreground = Image.open(foreground_image_path)
background = Image.open(background_image_path)

# Function to remove green screen, darken background, and overlay the foreground on the background
def remove_green_screen_and_darken_background(foreground, background):
    # Convert the images to numpy arrays
    foreground_array = np.array(foreground)
    background_array = np.array(background.resize(foreground.size))  # Match sizes

    # Darken the background by reducing its brightness
    darkening_factor = 0.5  # 0.0 to 1.0 range where 1.0 is no change
    background_array = (background_array * darkening_factor).astype(np.uint8)

    # Define green screen color range in RGB (as PIL uses RGB)
    lower_green = np.array([0, 120, 0], dtype=np.uint8)
    upper_green = np.array([120, 255, 120], dtype=np.uint8)

    # Create a mask for the green screen
    mask = cv2.inRange(foreground_array, lower_green, upper_green)
    mask_inv = cv2.bitwise_not(mask)

    # Apply the masks to the foreground and background
    foreground_cleaned = cv2.bitwise_and(foreground_array, foreground_array, mask=mask_inv)
    background_cleaned = cv2.bitwise_and(background_array, background_array, mask=mask)

    # Combine the images
    combined = cv2.add(foreground_cleaned, background_cleaned)

    # Convert the result back to a PIL image
    return Image.fromarray(combined)

# Process the images
result_image = remove_green_screen_and_darken_background(foreground, background)

# Save the single frame as a GIF with no animation (1 frame only)
result_image.save(
    output_gif_path,
    save_all=False,  # No additional frames
    loop=0  # Infinite loop if viewed in a player
)

# Output the path where the GIF is saved
output_gif_path
