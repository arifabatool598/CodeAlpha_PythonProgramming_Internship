# Astronomical Image File Organizer

import os
import shutil

source_folder = "space_images"
destination_folder = "organized_space_images"

# Create destination folder if it does not exist
os.makedirs(destination_folder, exist_ok=True)

moved_files = 0

# Check that the source folder exists
if not os.path.exists(source_folder):
    print(f"Source folder '{source_folder}' was not found.")
else:
    for filename in os.listdir(source_folder):

        source_path = os.path.join(source_folder, filename)

        # Select JPG image files
        if os.path.isfile(source_path) and filename.lower().endswith(".jpg"):

            destination_path = os.path.join(
                destination_folder, filename
            )

            shutil.move(source_path, destination_path)

            print(f"Moved astronomical image: {filename}")
            moved_files += 1

    print(f"\nDone! {moved_files} JPG image(s) organized.")
    print(f"Destination folder: {destination_folder}")