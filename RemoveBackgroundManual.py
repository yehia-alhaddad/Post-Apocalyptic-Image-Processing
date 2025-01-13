import cv2
import numpy as np

# Load the image
image_path = r"C:\Users\User\Desktop\School\ISE\BackGround_Removed\RunningManSharpened.png"
image = cv2.imread(image_path)
clone = image.copy()

# Mask for background removal
mask = np.zeros(image.shape[:2], dtype=np.uint8)

# Variables for drawing
drawing = False  # True if the mouse is pressed
ix, iy = -1, -1  # Initial coordinates

# Background colors to choose from
colors = [(0, 0, 0), (255, 255, 255), (0, 0, 255), (0, 255, 0), (255, 0, 0)]  # Black, White, Red, Green, Blue
current_color_index = 0  # Index for the current background color

# Mouse callback function
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:  # When the left mouse button is pressed
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:  # When the mouse is moving
        if drawing:
            # Draw on the mask where the user moves the mouse
            cv2.circle(mask, (x, y), 10, 255, -1)  # Adjust the brush size (10)

    elif event == cv2.EVENT_LBUTTONUP:  # When the left mouse button is released
        drawing = False
        cv2.circle(mask, (x, y), 10, 255, -1)

# Set the mouse callback
cv2.namedWindow("Interactive Background Removal")
cv2.setMouseCallback("Interactive Background Removal", draw_circle)

while True:
    # Create the current background with the selected color
    background = np.full_like(image, colors[current_color_index])

    # Combine the image and the mask for preview
    preview = np.where(mask[:, :, np.newaxis] == 255, background, clone)
    
    # Show the preview
    cv2.imshow("Interactive Background Removal", preview)

    # Wait for key input
    key = cv2.waitKey(1) & 0xFF
    if key == ord("r"):  # Reset the mask
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
    elif key == ord("s"):  # Save the result
        output_path = r"C:\Users\User\Desktop\School\ISE\BackGround_Removed\RunningManSharpened2.png"
        cv2.imwrite(output_path, preview)
        print(f"Refined image saved at: {output_path}")
        break
    elif key == ord("c"):  # Change background color
        current_color_index = (current_color_index + 1) % len(colors)  # Cycle through colors
    elif key == 27:  # ESC to exit
        break

# Close the windows
cv2.destroyAllWindows()
