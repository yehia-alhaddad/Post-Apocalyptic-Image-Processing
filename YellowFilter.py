from PIL import Image
import numpy as np

# Load the base image
image = Image.open(r"C:\Users\User\Desktop\School\ISE\DesertManShack2.png")

# Convert the image to RGB (if it is not already in RGB mode)
image = image.convert("RGB")

# Convert the image to a numpy array
image_array = np.array(image)

image_array[..., 0] = image_array[..., 0] * 1.0  # Red channel 
image_array[..., 1] = image_array[..., 1] * 1.0  # Green channel 
image_array[..., 2] = image_array[..., 2] * 0.7  # Blue channel 

# Clip the values to ensure they stay within the valid range [0, 255]
image_array = np.clip(image_array, 0, 255)

# Convert the numpy array back to an image
yellowish_image = Image.fromarray(image_array.astype('uint8'))

# Save the result to a specified path
save_path = r"C:\Users\User\Desktop\School\ISE\DesertManShack3.png"
yellowish_image.save(save_path)

# Show the resulting image (optional)
yellowish_image.show()

print(f"Image saved at: {save_path}")
