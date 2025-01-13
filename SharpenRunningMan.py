import cv2
import numpy as np

# Load the image
image_path = r"C:\Users\User\Desktop\School\ISE\RunningMan.jpg"
image = cv2.imread(image_path)

# Apply Gaussian Blur to the image
blurred_image = cv2.GaussianBlur(image, (5, 5), 1.5)

# Create the unsharp mask by subtracting the blurred image from the original
sharpened_image = cv2.addWeighted(image, 1.5, blurred_image, -0.5, 0)

# Save and show the result
output_path = r"C:\Users\User\Desktop\School\ISE\RunningManSharpened.jpg"
cv2.imwrite(output_path, sharpened_image)

cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
