from PIL import Image
import math

def add_white_space(image_path, padding_percentage):
    # Open the image using Pillow
    image = Image.open(image_path)
    
    # Calculate the padding based on the percentage
    width, height = image.size
    padding_x = int(width * padding_percentage / 100)
    padding_y = int(height * padding_percentage / 100)
    
    # Calculate the new dimensions with added padding
    new_width = width + 2 * padding_x
    new_height = height + 2 * padding_y
    
    # Create a new blank image with the new dimensions
    new_image = Image.new("RGB", (new_width, new_height), "white")
    
    # Paste the original image onto the new image with padding
    new_image.paste(image, (padding_x, padding_y))
    
    # Save the modified image
    new_image.save("avatar_with_white_space_2023_0620_001.png")
    print("White space added to the image.")

# Specify the path to your PNG file
image_path =  r"C:\Users\clu\OneDrive\图片\Personal\3004057.png"

# Specify the percentage of padding you want to add
value = (1 - math.sqrt(2) / 2) / 2
padding_percentage = value * 2 * 10 # 10% of the image dimensions

# Call the function to add white space
add_white_space(image_path, padding_percentage)