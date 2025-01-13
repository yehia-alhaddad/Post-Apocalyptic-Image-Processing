import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image_path = r"C:\Users\User\Desktop\School\ISE\RunningManSharpened.jpg"
image = cv2.imread(image_path)

# Resize the image for easier handling (optional)
image = cv2.resize(image, (600, 800))  # Adjust size if needed

# Create a mask
mask = np.zeros(image.shape[:2], dtype=np.uint8)

# Define the rectangle around the subject (coordinates can be adjusted)
rect = (50, 50, 500, 800)  # (x, y, width, height)

# Run GrabCut algorithm
bgd_model = np.zeros((1, 65), dtype=np.float64)  # Background model
fgd_model = np.zeros((1, 65), dtype=np.float64)  # Foreground model

cv2.grabCut(image, mask, rect, bgd_model, fgd_model, iterCount=5, mode=cv2.GC_INIT_WITH_RECT)

# Modify the mask
# Pixels marked as 0 or 2 are background, 1 or 3 are foreground
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

# Apply the mask to the image
foreground = image * mask2[:, :, np.newaxis]

# Change the background color
background_color = (0, 0, 255)  
background = np.full_like(image, background_color, dtype=np.uint8)

# Combine the foreground and the new background
result = np.where(mask2[:, :, np.newaxis] == 1, foreground, background)

# Save and display the output
output_path = r"C:\Users\User\Desktop\School\ISE\BackGround_Removed\RunningManSharpened.png"
cv2.imwrite(output_path, result)

# Show the result
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()

print(f"Image with background color changed saved at: {output_path}")
