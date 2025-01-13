from PIL import Image

# Load the base image and the image to insert
base_image_path = r"C:\Users\User\Desktop\School\ISE\DesertManShack.png"
insert_image_path = r"C:\Users\User\Desktop\School\ISE\BackGround_Removed\RustyCar2.png"

base_image = Image.open(base_image_path).convert("RGBA")
insert_image = Image.open(insert_image_path).convert("RGBA")

# Define the position where the insert image will be placed
position = (30, 600)  # Adjust as needed

new_width = 450  # Define the desired width for the insert image
width_percent = (new_width / float(insert_image.size[0]))  # Calculate the width percentage
new_height = int((float(insert_image.size[1]) * float(width_percent)))  # Adjust height to maintain aspect ratio

# Resize the insert image using LANCZOS filter (formerly known as ANTIALIAS)
insert_image_resized = insert_image.resize((new_width, new_height), Image.Resampling.LANCZOS)

# Extract the alpha channel (transparency mask) from the resized insert image
alpha_mask = insert_image_resized.split()[-1]  # Get the alpha channel as a mask

# Paste the resized insert image onto the base image using the alpha mask for transparency
base_image.paste(insert_image_resized, position, alpha_mask)

# Save or display the result
output_path = r"C:\Users\User\Desktop\School\ISE\DesertManShack2.png"
base_image.save(output_path)

base_image.show()  # Optional
print(f"Image saved at: {output_path}")
