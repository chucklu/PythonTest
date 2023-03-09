from PIL import Image, ImageDraw
import hashlib

def github_identicon(user_id, size=420):
  # Hash the user id with SHA1
  hash = hashlib.sha1(user_id.encode()).hexdigest()
  # Use the first 15 characters as the pixel map
  pixel_map = hash[:15]
  # Use the last 6 characters as the color code
  color = hash[-6:]
  # Create a blank image
  image = Image.new("RGB", (5, 5))
  # Create a draw object
  draw = ImageDraw.Draw(image)
  # Loop through the pixel map
  for i in range(15):
    # Get the row and column of the pixel
    row = i // 3
    col = i % 3
    # Get the character at the index
    char = pixel_map[i]
    # Turn on the pixel if the character is even
    if int(char, 16) % 2 == 0:
      # Draw the pixel with the color
      draw.point((row, col), fill="#" + color)
      # Draw the mirrored pixel
      draw.point((4 - row, col), fill="#" + color)
  # Resize the image
  image = image.resize((size, size), Image.NEAREST)
  # Return the image
  return image

# Test the function
user_id = "chucklu"
image = github_identicon(user_id)
image.save(user_id + ".png")