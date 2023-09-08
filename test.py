
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Define the path to your "assignment" folder
assignment_folder = "/content/drive/MyDrive/Assignment/Assignment"

# Function to list all image files in a directory
def list_image_files(directory):
    image_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
                image_files.append(os.path.join(root, file))
    return image_files

# Iterate through the subfolders
for subdir in os.listdir(assignment_folder):
    subdir_path = os.path.join(assignment_folder, subdir)

    # Check if it's a directory
    if os.path.isdir(subdir_path):
        print(f"Images in folder '{subdir}':")

        # List image files in the subfolder
        image_files = list_image_files(subdir_path)

        # Display each image with its corresponding label (subfolder name)
        for image_file in image_files:
            label = subdir

            # Load and display the image
            img = mpimg.imread(image_file)
            plt.imshow(img)
            plt.title(f"Label: {label}")
            plt.axis('off')  # Turn off axes
            plt.show()
