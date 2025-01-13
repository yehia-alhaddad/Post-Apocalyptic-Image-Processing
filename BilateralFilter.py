import cv2
import numpy as np

# Load the image
image_path = r"C:\Users\User\Desktop\School\ISE\OriginPictures\Man.jpg"
image = cv2.imread(image_path)

# Apply bilateral filter
# Parameters: (image, d, sigmaColor, sigmaSpace)
# - d: Diameter of the pixel neighborhood
# - sigmaColor: Filter sigma in color space (larger value means more colors are mixed)
# - sigmaSpace: Filter sigma in coordinate space (larger value means more distant pixels are considered)
filtered_image = cv2.bilateralFilter(image, d=50, sigmaColor=75, sigmaSpace=75)

# Save the filtered image
save_path = r"C:\Users\User\Desktop\School\ISE\BilateralFilterMan.jpg"
cv2.imwrite(save_path, filtered_image)

# Display the images (optional)
cv2.imshow("Original Image", image)
cv2.imshow("Bilateral Filtered Image", filtered_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Filtered image saved at: {save_path}")
