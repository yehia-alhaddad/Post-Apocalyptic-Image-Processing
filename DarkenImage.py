import cv2
import numpy as np

# Load the image
image_path = r"C:\Users\User\Desktop\School\ISE\ScientistinLab.png"
image = cv2.imread(image_path)

# Darken the image by scaling down the pixel values
darkened_image = cv2.convertScaleAbs(image, alpha=0.5, beta=0)  # alpha < 1 will darken

# Save and display the darkened image
output_path = r"C:\Users\User\Desktop\School\ISE\ScientistinLab2.png"
cv2.imwrite(output_path, darkened_image)

# Display the darkened image
cv2.imshow("Darkened Image", darkened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Darkened image saved at: {output_path}")
