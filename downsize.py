from PIL import Image
import os

def resize_images(input_dir, output_dir, new_size):
    """
    Resize all images in a directory to a new size and save them to a new directory.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            # Open the image
            with Image.open(os.path.join(input_dir, filename)) as img:
                # Resize the image
                resized_img = img.resize(new_size)
                # Save the resized image to the output directory
                resized_img.save(os.path.join(output_dir, filename))
                print(filename)

# Set the input and output directories and the new image size
input_dir = os.path.join("D:\\", "Documents", "Semester 9", "Capstone 2", "dataset", "leftImg8bit", "val_all")
output_dir = os.path.join("D:\\", "Documents", "Semester 9", "Capstone 2", "dataset", "leftImg8bit", "512", "val")
new_size = (512, 512)

# Call the resize_images function with the input directory, output directory, and new size
resize_images(input_dir, output_dir, new_size)
