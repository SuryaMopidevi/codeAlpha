import os
import shutil

def organize_files(source_dir, destination_dir):
    # Create destination directories if they don't exist
    for folder_name in ['Images', 'Documents', 'Videos', 'Others']:
        folder_path = os.path.join(destination_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    # Get a list of all files in the source directory
    files = os.listdir(source_dir)

    for file in files:
        file_path = os.path.join(source_dir, file)

        if os.path.isfile(file_path):
            # Determine the type of the file based on its extension
            file_extension = file.split('.')[-1].lower()

            # Define destination directory based on file type
            if file_extension in ['jpg', 'jpeg', 'png', 'gif']:
                dest_folder = 'Images'
            elif file_extension in ['pdf', 'doc', 'docx', 'txt']:
                dest_folder = 'Documents'
            elif file_extension in ['mp4', 'avi', 'mkv']:
                dest_folder = 'Videos'
            else:
                dest_folder = 'Others'

            # Move the file to the corresponding directory
            dest_path = os.path.join(destination_dir, dest_folder, file)
            shutil.move(file_path, dest_path)
            print(f"Moved {file} to {dest_folder} folder.")

if __name__ == "__main__":
    # Specify the source and destination directories
    source_directory = 'sourceDirectory'
    destination_directory = 'destinationDirectory'

    # Call the function to organize files
    organize_files(source_directory, destination_directory)
