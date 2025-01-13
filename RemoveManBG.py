import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image_path = r'C:\Users\User\Desktop\School\ISE\ManRun.jpg'
image = cv2.imread(image_path)

# Resize the image for easier processing (optional)
image = cv2.resize(image, (600, 800))

# Create an initial mask
mask = np.zeros(image.shape[:2], dtype=np.uint8)

# Define the rectangle around the subject (adjust coordinates)
rect = (50, 50, image.shape[1] - 100, image.shape[0] - 100)

# Initialize background and foreground models for GrabCut
bgd_model = np.zeros((1, 65), dtype=np.float64)
fgd_model = np.zeros((1, 65), dtype=np.float64)

# Apply GrabCut
cv2.grabCut(image, mask, rect, bgd_model, fgd_model, iterCount=5, mode=cv2.GC_INIT_WITH_RECT)

# Modify the mask - 0 and 2 are background, 1 and 3 are foreground
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

# Isolate the foreground
foreground = image * mask2[:, :, np.newaxis]

# For a white background:
# background = np.full_like(image, (255, 255, 255))

# For a transparent background:
b, g, r = cv2.split(foreground)
rgba = cv2.merge((b, g, r, mask2 * 255))  # Add alpha channel

# Save the output
output_path = r'C:\Users\User\Desktop\School\ISE\ManRun2.jpg'
cv2.imwrite(output_path, rgba)

# Display the result
plt.figure(figsize=(8, 10))
plt.imshow(cv2.cvtColor(foreground, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()

print(f"Image with background removed saved at: {output_path}")
