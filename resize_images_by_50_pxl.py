import os
from PIL import Image

# List of image file paths
filepaths = [
    "original_images/image_10-20_kg.png",
    "original_images/image_20+_kg.png",
    "original_images/rot90_image_10-20_kg.png",
    "original_images/rot90_image_20+_kg.png"
]

# Base output directory
output_base_dir = "resized_images"

# Loop through each image
for image_path in filepaths:
    # Open the image
    img = Image.open(image_path)
    width, height = img.width, img.height

    # Get the image name without directory
    image_name = os.path.basename(image_path)

    # Perform resizing 20 times
    for i in range(1, 21):
        # Calculate the new dimensions
        reduce_by = i * 50
        new_width = max(1, width - reduce_by)  # Ensure dimensions don't go below 1
        new_height = max(1, height - reduce_by)

        # Resize the image
        resized_img = img.resize((new_width, new_height))

        # Create the output directory
        target_name = f"minus_{reduce_by}_pxl"
        output_dir = os.path.join(output_base_dir, target_name)
        os.makedirs(output_dir, exist_ok=True)

        # Extract the file name without extension and the extension
        file_name, file_extension = os.path.splitext(image_name)

        # Save the resized image
        target_image_name = f"{image_name}_{target_name}{file_extension}"
        output_path = os.path.join(output_dir, target_image_name)
        resized_img.save(output_path)

        print(f"Saved resized image to: {output_path}")
