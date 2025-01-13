import cv2
import numpy as np
import imageio

# Load the background image
image_path = r"C:\Users\User\Desktop\School\ISE\FinalImage\DesertManShack3.png"  
background = cv2.imread(image_path)

# Resize background for consistent dimensions if needed
height, width = background.shape[:2]

# Parameters for the particles
num_particles = 50
particle_color = (0, 255, 255)  # Yellow in BGR format
particle_size = 3
num_frames = 100  # Length of the animation
max_particles = 100  # Maximum particles on screen at any time

# Initialize particle list
particles = []

def spawn_particle():
    """Spawn a new particle anywhere along the top edge, but falling to the left."""
    return {"x": np.random.randint(0, width), "y": np.random.randint(0, height // 3)}

# Frames list for the GIF
frames = []

for frame_idx in range(num_frames):
    # Create a copy of the background for this frame
    frame = background.copy()

    # Add new particles if the total is below max_particles
    while len(particles) < max_particles:
        particles.append(spawn_particle())

    # Update and draw particles
    new_particles = []  # Store particles still on screen
    for particle in particles:
        # Draw the particle
        cv2.circle(frame, (particle["x"], particle["y"]), particle_size, particle_color, -1)

        # Move the particle diagonally leftward and down
        particle["x"] -= np.random.randint(1, 5)
        particle["y"] += np.random.randint(1, 5)

        # Keep the particle if it's still on screen
        if 0 <= particle["x"] < width and 0 <= particle["y"] < height:
            new_particles.append(particle)

    # Update particle list
    particles = new_particles

    # Convert frame to RGB (for saving with imageio)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frames.append(frame_rgb)

# Save the frames as a GIF
output_path = r"C:\Users\User\Desktop\School\ISE\FinalImage\Desert.gif"
imageio.mimsave(output_path, frames, fps=20)

print(f"GIF saved at: {output_path}")
