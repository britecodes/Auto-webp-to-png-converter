from PIL import Image
import os

files = os.listdir()  # We list all of the files and folders using os.listdir()
print("Auto .webp convert, base code by James Phoenix. modified by Britecodes")
print(f"These are all of the files in our current working directory: {files}")
images = [file for file in files if file.endswith('webp')]
print(f"These are all of the images in our current working directory {images}")


# Defining a Python user-defined exception
class Error(Exception):
    pass


def convert_image(image_path, image_type):
    # 1. Opening the image:
    im = Image.open(image_path)
    # 2. Converting the image to RGB colour:
    im = im.convert('RGB')
    # 3. Spliting the image path (to avoid the .webp being part of the image name):
    image_name = image_path.split('.')[0]
    print(f"This is the image name: {image_name}")

    # Saving the images based upon their specific type:
    if image_type == 'webp':
        im.save(f"{image_name}.png", 'png')
    else:
        # Raising an error if we didn't get a webp file type!
        raise Error


for image in images:
    if image.endswith('webp'):
        convert_image(image, image_type='webp')
    else:
        raise Error
