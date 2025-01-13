import cv2

# Callback function to select a region of interest
def select_roi(event, x, y, flags, param):
    global roi, cropping, ref_point
    
    if event == cv2.EVENT_LBUTTONDOWN:  # Mouse press
        cropping = True
        ref_point = [(x, y)]
    elif event == cv2.EVENT_LBUTTONUP:  # Mouse release
        cropping = False
        ref_point.append((x, y))
        cv2.rectangle(temp_image, ref_point[0], ref_point[1], (0, 255, 0), 2)
        cv2.imshow("Image", temp_image)
        roi = ref_point

# Initialize variables
cropping = False
ref_point = []

# Load image
image_path = r"C:\Users\User\Desktop\School\ISE\OriginPictures\ManRun.jpg"
image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError(f"Image not found at: {image_path}")
temp_image = image.copy()

# Display image and wait for ROI selection
cv2.imshow("Image", temp_image)
cv2.setMouseCallback("Image", select_roi)
cv2.waitKey(0)

# Crop the selected region
if len(ref_point) == 2:
    x1, y1 = ref_point[0]
    x2, y2 = ref_point[1]
    cropped_image = image[y1:y2, x1:x2]
    cv2.imshow("Cropped", cropped_image)
    cv2.imwrite(r"C:\Users\User\Desktop\School\ISE\ManRun.jpg", cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
