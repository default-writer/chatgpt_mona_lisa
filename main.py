from PIL import Image

# Load the Mona Lisa image
mona_lisa = Image.open("mona_lisa_small.jpg")

# Define the ASCII characters to use for the conversion
ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Define the size of each ASCII character in the output image
char_width = 10
char_height = 18

# Calculate the size of the output image
width, height = mona_lisa.size
output_width = char_width * width // (char_height)
output_height = height // (char_height // 4)

# Resize the Mona Lisa image to match the output size
mona_lisa = mona_lisa.resize((output_width, output_height))

# Convert the image to grayscale
mona_lisa = mona_lisa.convert("L")

# Convert the image to ASCII art
ascii_art = ""
for y in range(output_height):
    for x in range(output_width):
        pixel = mona_lisa.getpixel((x, y))
        ascii_index = pixel * (len(ascii_chars) - 1) // 255
        ascii_art += ascii_chars[ascii_index]
    ascii_art += "\n"

# Print the ASCII art to the console
print(ascii_art)
