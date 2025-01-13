import cv2
import numpy as np

# Function to adjust transparency
def adjust_transparency(image, alpha_value):
    # Convert the image to BGRA (add alpha channel)
    image_with_alpha = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    
    # Get the alpha channel (4th channel)
    alpha_channel = image_with_alpha[:, :, 3]
    
    # Adjust the alpha channel based on the input alpha_value (0-255)
    alpha_channel = (alpha_channel * (alpha_value / 255)).astype(np.uint8)
    
    # Replace the original alpha channel with the adjusted one
    image_with_alpha[:, :, 3] = alpha_channel
    
    return image_with_alpha

# Load the image
image_path = r"C:\Users\User\Desktop\School\ISE\smok.png"
image = cv2.imread(image_path)

# Input the alpha value (0 to 255), where 255 is fully opaque and 0 is fully transparent
alpha_value = 150  # You can change this value between 0 and 255 to adjust transparency

# Adjust the transparency based on the given alpha value
image_with_alpha = adjust_transparency(image, alpha_value)

# Save the resulting image (it should be saved as PNG to preserve transparency)
save_path = r"C:\Users\User\Desktop\School\ISE\transparent_smoke.png"
cv2.imwrite(save_path, image_with_alpha)

print(f"Image saved at: {save_path}")

