import random 

# The minimum intensity of the color space 
min = 0

# The maximum intensity of the color space 
max = 255

# Calculating 3 random values for each channel between min & max 
red = random.randint(min, max) 
green = random.randint(min, max) 
blue = random.randint(min, max) 

print("Color Code :", (red, green, blue))
