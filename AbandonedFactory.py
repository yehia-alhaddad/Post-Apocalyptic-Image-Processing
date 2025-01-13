import random
from PIL import Image, ImageDraw
import gc

# Load the new factory background, car image, fire image, smoke image, and hazmat suit image
background = Image.open('/content/pexels-matreding-12069495.jpg')
car = Image.open('/content/BrokenCar.jpg')
fire = Image.open('/content/Fire.jpg')
smoke = Image.open('/content/Smoke.jpg')
hazmat = Image.open('/content/DudeInHazmat.jpg')

# Darken the background by applying a semi-transparent black overlay
background = background.convert("RGBA")
overlay = Image.new("RGBA", background.size, (0, 0, 0, 100))  # 100 is the alpha for transparency
background.paste(overlay, (0, 0), overlay)

# Convert car image to RGBA mode to support transparency and remove the white background
car = car.convert("RGBA")
datas = car.getdata()
new_data = []
for item in datas:
    if item[0] > 200 and item[1] > 200 and item[2] > 200:  # Threshold for white pixels
        new_data.append((255, 255, 255, 0))  # Transparent
    else:
        new_data.append(item)
car.putdata(new_data)

# Resize the car image to make it 5 times bigger
car_resized = car.resize((car.width * 5, car.height * 5))

# Resize the fire to 120% of the car's height and make it 90% opaque
fire_resized = fire.resize((car_resized.width, int(car_resized.height * 1.2)))
fire_resized_with_alpha = fire_resized.convert("RGBA")
fire_data = fire_resized_with_alpha.getdata()
new_fire_data = [(item[0], item[1], item[2], int(item[3] * 0.9)) for item in fire_data]  # 90% opacity
fire_resized_with_alpha.putdata(new_fire_data)

# Remove the white background from the smoke image and adjust opacity to 50%
smoke = smoke.convert("RGBA")
smoke_data = smoke.getdata()
new_smoke_data = []
for item in smoke_data:
    if item[0] > 200 and item[1] > 200 and item[2] > 200:  # Threshold for white pixels
        new_smoke_data.append((255, 255, 255, 0))  # Transparent
    else:
        new_smoke_data.append(item)
smoke.putdata(new_smoke_data)
smoke_resized = smoke.resize((fire_resized.width, int(fire_resized.height * 2)))  # 200% height
smoke_resized_with_alpha = smoke_resized.convert("RGBA")
smoke_data = smoke_resized_with_alpha.getdata()
new_smoke_data = [(item[0], item[1], item[2], int(item[3] * 0.5)) for item in smoke_data]  # 50% opacity
smoke_resized_with_alpha.putdata(new_smoke_data)

# Remove the green background from the hazmat suit image
hazmat = hazmat.convert("RGBA")
hazmat_data = hazmat.getdata()
new_hazmat_data = []
for item in hazmat_data:
    # Threshold for green pixels
    if item[0] < 100 and item[1] > 200 and item[2] < 100:
        new_hazmat_data.append((255, 255, 255, 0))  # Make green pixels transparent
    else:
        new_hazmat_data.append(item)
hazmat.putdata(new_hazmat_data)

# Resize the hazmat suit image to make it larger by an additional 800 pixels (1200 pixels total increase)
hazmat_resized = hazmat.resize((hazmat.width + 1200, hazmat.height + 1200))

# Calculate the position to place the car at the bottom-right of the background
background_width, background_height = background.size
car_width, car_height = car_resized.size
bottom_right_position = (background_width - car_width - 30 + 200, background_height - car_height + 50)

# Calculate position for hazmat figure on the left
hazmat_position = (50, background_height - hazmat_resized.height - 50)  # Position on left side

# Paste the car onto the new background
background.paste(car_resized, bottom_right_position, car_resized)

# Position and paste the fire image
fire_position = (bottom_right_position[0], bottom_right_position[1] - fire_resized_with_alpha.height + 10 + 1200)
background.paste(fire_resized_with_alpha, fire_position, fire_resized_with_alpha)

# Position and paste the smoke image
smoke_position = (fire_position[0], fire_position[1] - smoke_resized_with_alpha.height + 2000)
background.paste(smoke_resized_with_alpha, smoke_position, smoke_resized_with_alpha)

# Create an animated GIF with snow effect falling from top to bottom
frames = []
num_frames = 60  # Keep number of frames to 60 for smoother animation
snowflakes = [(random.randint(0, background_width), random.randint(-background_height, 0)) for _ in range(50)]  # Reduced snowflakes

falling_speed = 80  # Increased falling speed for faster snow

for frame_number in range(num_frames):
    # Create a copy of the background for each frame
    frame = background.copy()
    draw = ImageDraw.Draw(frame)
    
    # Paste the hazmat figure on the left side of the frame
    frame.paste(hazmat_resized, hazmat_position, hazmat_resized)
    
    # Update snowflake positions and draw them
    new_snowflakes = []
    for x, y in snowflakes:
        y += falling_speed  # Move snowflake down faster
        if y > background_height:
            y = random.randint(-40, 0)  # Reset snowflake to the top
        new_snowflakes.append((x, y))
        draw.ellipse((x, y, x + 40, y + 40), fill="white")  # Large snowflakes (40x40 pixels)
    snowflakes = new_snowflakes
    
    frames.append(frame)
    
    # Clear memory and collect garbage
    del draw
    gc.collect()

# Save the frames as an animated GIF with a total duration of 20 seconds
output_path = '/content/FasterSnowEffectWithHazmat20Seconds.gif'
frames[0].save(output_path, format='GIF', save_all=True, append_images=frames[1:], duration=333, loop=0)

print(f"The optimized 20-second GIF with the larger hazmat figure and faster snow has been saved to {output_path}")
