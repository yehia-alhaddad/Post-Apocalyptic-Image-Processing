import cv2
import numpy as np

# Load the image
image_path = r"C:\Users\User\Desktop\School\ISE\ScientistinLab.png"
image = cv2.imread(image_path)
result = image.copy()

# Initialize global variables for clicked point and glow properties
selected_point = None

def on_mouse(event, x, y, flags, param):
    """Mouse callback function to select the glow area."""
    global selected_point
    if event == cv2.EVENT_LBUTTONDOWN:
        selected_point = (x, y)  # Save the clicked position

def apply_glow():
    """Apply the glow effect based on the selected point and color."""
    global result
    if selected_point is None:
        return  # Do nothing if no point is selected

    # Create a mask with a circle at the selected point
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.circle(mask, selected_point, glow_radius, 255, -1)

    # Expand the mask using Gaussian blur
    glow = cv2.GaussianBlur(mask, (glow_radius * 2 + 1, glow_radius * 2 + 1), 0)

    # Create the red glow (red channel is last in BGR format)
    red_glow = cv2.merge([np.zeros_like(glow), np.zeros_like(glow), glow])

    # Add the red glow to the original image
    result = cv2.addWeighted(image, 1.0, red_glow.astype(np.uint8), glow_intensity, 0)

def on_change(val):
    """Callback for trackbar changes."""
    global glow_radius, glow_intensity
    glow_radius = cv2.getTrackbarPos('Radius', 'Glow Controls')
    glow_intensity = cv2.getTrackbarPos('Intensity', 'Glow Controls') / 100
    apply_glow()

# Initialize default glow properties
glow_radius = 50
glow_intensity = 0.5

# Create a window for controls and set up trackbars
cv2.namedWindow('Glow Controls')
cv2.createTrackbar('Radius', 'Glow Controls', glow_radius, 100, on_change)
cv2.createTrackbar('Intensity', 'Glow Controls', int(glow_intensity * 100), 100, on_change)

# Set up mouse callback for selecting the glow area
cv2.namedWindow('Beaker Glow')
cv2.setMouseCallback('Beaker Glow', on_mouse)

# Main loop
while True:
    cv2.imshow('Beaker Glow', result)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # Press 'Esc' to save and exit
        # Save the result as a copy
        output_path = r"C:\Users\User\Desktop\School\ISE\ScientistinLab2.png"
        cv2.imwrite(output_path, result)
        print(f"Image saved as: {output_path}")
        break

cv2.destroyAllWindows()
    