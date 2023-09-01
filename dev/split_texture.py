from PIL import Image

# Open the image file
img = Image.open("img/TX Tileset Grass.png")  # Replace with your image file name

# Image dimensions
img_width, img_height = img.size

# Block dimensions
block_width = 64
block_height = 64

# Initialize counters
x1, y1 = 0, 0
x2, y2 = block_width, block_height

# Loop through the image to create 16x16 blocks
for i in range(0, img_height, block_height):
    for j in range(0, img_width, block_width):
        # Crop the image based on calculated coordinates
        block = img.crop((x1, y1, x2, y2))
        
        # Save the cropped image
        block.save(f"block_{x1}_{y1}.png")
        
        # Update x coordinates for the next block
        x1 += block_width
        x2 += block_width
    
    # Update y coordinates for the next row of blocks
    y1 += block_height
    y2 += block_height
    
    # Reset x coordinates for the next row
    x1 = 0
    x2 = block_width
