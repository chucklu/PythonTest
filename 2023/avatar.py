from PIL import Image,ImageDraw
import hashlib

# Define the input string and hash it using SHA1
input_string = "hello"
hash_value = hashlib.sha1(input_string.encode('utf-8')).hexdigest()

# Extract the first 15 characters of the hash
short_hash = hash_value[:15]

# Initialize the size of the image and the size of each square
image_size = 420
square_size = image_size // 7

# Initialize the image and fill it with a light gray color
image = Image.new('RGB', (image_size, image_size), (240, 240, 240))

# Define the color for the foreground squares based on the hash value
color = (
    int(short_hash[0:2], 16),
    int(short_hash[2:4], 16),
    int(short_hash[4:6], 16)
)

# Loop through the hash and draw the squares
for i, char in enumerate(short_hash):
    # Calculate the position of the square
    x = (i % 5) * square_size
    y = (i // 5) * square_size

    # If the character is odd, draw the square
    if int(char, 16) % 2 == 1:
        draw = ImageDraw.Draw(image)
        draw.rectangle((x, y, x + square_size, y + square_size), fill=color)

# Show the image
image.show()