import os

# Define a function to format and clean a drive
def tree_format(drive,sizes):
    # Walk through the directory tree starting from the specified drive
    for folder_name, subfolders, filenames in os.walk(drive):
        # Calculate the depth of the current folder in the directory tree
        depth = folder_name.count(os.sep) - drive.count(os.sep)
        # Create an indentation string based on the depth
        indent = ' ' * 4 * depth
        print(f"{indent}[{folder_name}]")
        
        # Iterate through the files in the current folder
        for filename in filenames:
            # Get the full path of the file
            file_path = os.path.join(folder_name, filename)
            # Calculate the file size in megabytes
            size = os.path.getsize(file_path) / 1024 ** 2
            # Check if the file is larger than 100MB
            if size >= sizes:
                # Print the file name and size, and prompt for deletion
                print(f"{indent} {filename} size (in MB): {size:.2f}")
                deleting_file(file_path)  # Call the deleting_file function
        
        # Iterate through the subfolders in the current folder
        for subfolder in subfolders:
            # Get the full path of the subfolder
            subf_path = os.path.join(folder_name, subfolder)
            # Check if the subfolder is empty
            if not os.listdir(subf_path):
                # Print the name of the empty folder and prompt for deletion
                print(f"Empty folder name: {subfolder}")
                n = input("Enter Y/y if the empty folder needs to be deleted:")
                if n == 'Y' or n == 'y':
                    os.rmdir(subf_path)  # Delete the empty subfolder
                    print(f"Subfolder '{subfolder}' was successfully deleted.")

# Define a function to delete a file
def deleting_file(path):
    n = input("Enter Y/y if the file needs to be deleted:")
    if n == 'Y' or n == 'y':
        os.unlink(path)  # Delete the file
        print("The file was successfully deleted.")

# Prompt the user to enter the drive to be cleaned
drive = input("Enter the drive to be cleaned:")
size=int(input("Enter the size:"))
# Check if the specified root directory exists
if os.path.exists(drive):
    # Call the tree_format function to clean the drive
    tree_format(drive,size)
else:
    print(f"The specified root directory '{drive}' does not exist.")
