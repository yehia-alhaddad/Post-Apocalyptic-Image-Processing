from PIL import Image, ImageEnhance
import numpy as np

# Paths for images
zombie_image_path_1 = '/content/360_F_654351346_RZpUnxZp4TgjipNfmLVmdDDHB535RU2V.jpg'
zombie_image_path_2 = '/content/360_F_654351346_RZpUnxZp4TgjipNfmLVmdDDHB535RU2V.jpg'
city_image_path = '/content/istockphoto-1221284462-640x640.jpg'
fire_image_path = '/content/360_F_887632915_ehIu6BsBrVRas13MPcXYYy76jwRSYJQt.jpg'
smoke_image_path = '/content/79bdbfd699a5d55c167fef798d7756c1.jpg'

# Load images
zombie_image_1 = Image.open(zombie_image_path_1).convert("RGBA")
zombie_image_2 = Image.open(zombie_image_path_2).convert("RGBA")
city_image = Image.open(city_image_path).convert("RGBA")
fire_image = Image.open(fire_image_path).convert("RGBA")
smoke_image = Image.open(smoke_image_path).convert("RGBA")

# Resize zombie images
scale_factor = 0.5
zombie_image_1 = zombie_image_1.resize((int(zombie_image_1.width * scale_factor), int(zombie_image_1.height * scale_factor)), Image.LANCZOS)
zombie_image_2 = zombie_image_2.resize((int(zombie_image_2.width * scale_factor), int(zombie_image_2.height * scale_factor)), Image.LANCZOS)

# Function to remove white and light gray background
def remove_background(image):
    data = np.array(image)
    threshold = 200  
    transparency_mask = (
        (data[:, :, 0] > threshold) &
        (data[:, :, 1] > threshold) &
        (data[:, :, 2] > threshold)
    )
    data[transparency_mask] = [0, 0, 0, 0]
    return Image.fromarray(data)

# Apply background removal to fire, smoke, and zombie images
fire_image = remove_background(fire_image)
smoke_image = remove_background(smoke_image)
zombie_image_1 = remove_background(zombie_image_1)
zombie_image_2 = remove_background(zombie_image_2)

# Adjust color of zombies to fit environment
def adjust_color(image, brightness=0.8, contrast=1.2, color=0.8):
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast)
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(color)
    return image

zombie_image_1 = adjust_color(zombie_image_1)
zombie_image_2 = adjust_color(zombie_image_2)

# Darken the background (city image) more to simulate an overcast/rainy effect
def darken_background(image, factor=0.65):  # A darker factor for a rain effect
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

city_image = darken_background(city_image)

# Darken the fire image to make it less intense
def darken_fire(image, factor=0.7):  # Adjust the factor to control the darkness level
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

fire_image = darken_fire(fire_image)

# Positioning zombies
city_width, city_height = city_image.size
zombie_width, zombie_height = zombie_image_1.size
position_1 = (city_width // 2 - zombie_width // 2 - 100, city_height - zombie_height - 50)
position_2 = (city_width // 2 - zombie_width // 2 + 100, city_height - zombie_height - 50)

# Resize smoke to create depth effect
smoke_scale_near = 0.5  # Scale for the right smoke, closer to the viewer
smoke_scale_far = 0.35  # Smaller scale for the left smoke, to simulate distance
smoke_image_near = smoke_image.resize((int(smoke_image.width * smoke_scale_near), int(smoke_image.height * smoke_scale_near)), Image.LANCZOS)
smoke_image_far = smoke_image.resize((int(smoke_image.width * smoke_scale_far), int(smoke_image.height * smoke_scale_far)), Image.LANCZOS)

# Static smoke layers (no movement, placed behind the city image)
smoke_position_left = (50, city_height - smoke_image_far.height - 150)  # Left smoke, smaller to simulate distance
smoke_position_right = (city_width - smoke_image_near.width - 50, city_height - smoke_image_near.height - 150)  # Right smoke, larger to simulate closeness

# Resize fire image to stretch across the city width
fire_height = int(city_height * 0.25)  # Adjust the height of the fire as needed
fire_image = fire_image.resize((city_width, fire_height), Image.LANCZOS)
fire_position = (0, city_height - fire_height - 100)  # Position fire higher and spread across the width

# Create an image with static smoke and zombies (no animation)
final_image = city_image.copy()

# Paste the fire image on top of the city image
final_image.paste(fire_image, fire_position, fire_image)

# Paste static smoke layers (no movement)
final_image.paste(smoke_image_far, smoke_position_left, smoke_image_far)
final_image.paste(smoke_image_near, smoke_position_right, smoke_image_near)

# Paste zombies (static)
final_image.paste(zombie_image_1, position_1, zombie_image_1)
final_image.paste(zombie_image_2, position_2, zombie_image_2)

# Save the final image as a GIF
output_path = '/content/final_static_smoke_zombies.gif'
final_image.save(output_path, format='GIF')

print(f"GIF saved to {output_path}")
