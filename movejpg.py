import os
import shutil

# set the path to the parent directory
parent_dir = os.path.join("D:\\", "Documents", "Semester 9", "Capstone 2", "dataset", "leftImg8bit", "train")

# set the path to the directory where the JPG files will be moved to
jpg_dir = os.path.join("D:\\", "Documents", "Semester 9", "Capstone 2", "dataset", "leftImg8bit", "train_all")

# loop through all the subdirectories in the parent directory
for subdir, dirs, files in os.walk(parent_dir):
    for file in files:
        # check if the file is a JPG file
        if file.lower().endswith('.jpg'):
            # create the destination directory if it does not exist
            if not os.path.exists(jpg_dir):
                os.makedirs(jpg_dir)
            
            # get the full path of the source and destination files
            src_path = os.path.join(subdir, file)
            dst_path = os.path.join(jpg_dir, file)
            
            # move the file to the destination directory
            shutil.move(src_path, dst_path)
            print(src_path)
            
# print a message indicating the operation is complete
print("JPG files have been moved to", jpg_dir)
