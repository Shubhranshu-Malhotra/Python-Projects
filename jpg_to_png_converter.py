import sys
import os
from PIL import Image

# grab the first and second command line arguments
image_path = sys.argv[1]
save_folder = sys.argv[2]

# check if the given folder exists or not, else create it
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Loop through pokedex and convert all images in it to png
# Save the images to the new folder

for img in os.listdir(image_path):
    image = Image.open(image_path+img)
    clean_name = img.split('.')[-2]
    image.save(f'{save_folder}{clean_name}.png','png')
    print(image)

