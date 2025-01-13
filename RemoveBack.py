import cv2
import numpy as np
from PIL import Image
import os

# Paths for the input image and output directory
img = r'C:\Users\User\Desktop\School\ISE\OriginPictures\zombie.jpg'
save = r'C:\Users\User\Desktop\School\ISE\BackGround_Removed'

def remove_background_color(image_path, target_color, save_path, threshold=50):

    # Open the image and convert to RGBA format
    img = Image.open(image_path)
    img = img.convert("RGBA")
    data = img.getdata()
    new_data = []
    
    # Iterate over each pixel and check if it's close to the target color
    for item in data:
        # Check if the pixel is close to the target color
        if (abs(item[0] - target_color[0]) < threshold and 
            abs(item[1] - target_color[1]) < threshold and 
            abs(item[2] - target_color[2]) < threshold):
            new_data.append(((0,0,0,0)))  # Transparent pixel
        else:
            new_data.append(item)
    
    # Update the image data
    img.putdata(new_data)

    # Ensure the save path exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    # Save the modified image to the specified path
    save_name = os.path.join(save_path, "Zombie.png")
    img.save(save_name, "PNG")
    print(f"Modified image saved at: {save_name}")

remove_background_color(img, (255, 255, 255), save)
