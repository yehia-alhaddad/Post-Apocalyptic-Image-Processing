import cv2
import numpy as np
from PIL import Image
import os

# Load the base image and the image to be inserted
base_image = Image.open(r"C:\Users\User\Desktop\School\ISE\lab.jpg")
insert_image = Image.open(r"C:\Users\User\Desktop\School\ISE\BackGround_Removed\Scientist2.png")

# Resize the insert image if necessary (optional)
insert_image = insert_image.resize((170, 200))  # Resize to fit your needs

# Define the position where you want to paste the second image
position = (270, 47)  # (x, y) coordinates for the top-left corner of the insert image

# Paste the image onto the base image
base_image.paste(insert_image, position, insert_image)  # The third argument is the mask for transparency (if applicable)

# Convert the image to RGB to avoid the 'RGBA' to 'JPEG' error
base_image = base_image.convert("RGB")

# Define the save path
save_path = r"C:\Users\User\Desktop\School\ISE\ScientistinLab.png"

# Create the folder if it doesn't exist
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the result to the specified path
base_image.save(save_path)

# Show the resulting image (optional)
base_image.show()

print(f"Image saved at: {save_path}")
