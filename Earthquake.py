from PIL import Image, ImageSequence, ImageOps
import numpy as np

# Load the image
image_path = '/content/EarthSplit.jpg'
image = Image.open(image_path)

# Zoom into the image slightly
zoom_factor = 1.2  # Zoom in by 20%
width, height = image.size
new_width = int(width / zoom_factor)
new_height = int(height / zoom_factor)
left = (width - new_width) // 2
top = (height - new_height) // 2
right = left + new_width
bottom = top + new_height

# Crop and resize the image to create a zoom effect
zoomed_image = image.crop((left, top, right, bottom)).resize((width, height), Image.LANCZOS)

# Create a sequence of images to mimic a faster shaking effect
frames = []
shake_range = 15  # Maximum number of pixels to shake

# Create shaking effect with 20 frames for faster motion
for i in range(20):
    # Randomly shift the image left or right and up or down
    shift_x = np.random.randint(-shake_range, shake_range)
    shift_y = np.random.randint(-shake_range, shake_range)
    shifted_image = Image.new("RGB", zoomed_image.size)
    shifted_image.paste(zoomed_image, (shift_x, shift_y))
    frames.append(shifted_image)

# Save the sequence as a GIF
gif_path = '/content/earthquake_effect_zoomed.gif'
frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=30, loop=0)

print("GIF created at:", gif_path)
