import cv2
import numpy as np

# Load the image
image_path = r"C:\Users\User\Desktop\School\ISE\BackGround_Removed\Scientist.png"  
image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

# Check if the image has an alpha channel (transparency)
if image.shape[2] == 4:  # RGBA format
    # Split the image into color and alpha channel
    bgr = image[:, :, :3]
    alpha = image[:, :, 3]

    # Remove outline by refining alpha mask
    alpha = cv2.GaussianBlur(alpha, (5, 5), 0)  # Adjust kernel size as needed

    # Recombine the refined alpha channel with the color channels
    image = cv2.merge((bgr, alpha))

# Sharpen the image
# Define a sharpening kernel
sharpen_kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]], dtype=np.float32)

# Apply the sharpening filter to the BGR channels
sharpened = cv2.filter2D(image[:, :, :3], -1, sharpen_kernel)

# Combine the sharpened image with the alpha channel
if image.shape[2] == 4:  # Re-add alpha channel if present
    result = cv2.merge((sharpened, alpha))
else:
    result = sharpened

# Save and display the result
output_path = r"C:\Users\User\Desktop\School\ISE\BackGround_Removed\Scientist2.png"
cv2.imwrite(output_path, result)

# Display the final image
cv2.imshow("Sharpened Image", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Sharpened image saved at: {output_path}")
