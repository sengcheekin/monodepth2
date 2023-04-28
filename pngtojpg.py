from PIL import Image
import os

# set the path to the folder containing the PNG images
# input_folder = "D:\Documents\Semester 9\Capstone 2\dataset\leftImg8bit\train\aachen"
input_folder = os.path.join("D:\\", "Documents", "Semester 9", "Capstone 2", "dataset", "leftImg8bit", "val")


# set the path to the output folder where the converted JPG images will be saved
# output_folder = "D:\Documents\Semester 9\Capstone 2\dataset\leftImg8bit\train\aachen_jpg"
output_folder = os.path.join("D:\\", "Documents", "Semester 9", "Capstone 2", "dataset", "leftImg8bit", "val_all")


# loop through all the subfolders in the input folder
for subdir, dirs, files in os.walk(input_folder):
    # loop through all the files in the subfolder
    for filename in files:
        # check if the file is a PNG image
        if filename.endswith(".png"):
            # open the PNG image file
            png_image = Image.open(os.path.join(subdir, filename))
            
            # create a new filename for the converted JPG image
            jpg_filename = os.path.splitext(filename)[0] + ".jpg"
            
            # set the path to save the converted JPG image
            jpg_path = os.path.join(output_folder, jpg_filename)
            
            # create the subfolder in the output directory if it doesn't exist
            os.makedirs(os.path.join(output_folder), exist_ok=True)
            
            # convert and save the image as a JPG
            png_image.convert("RGB").save(jpg_path, "JPEG")

            print(jpg_path)
