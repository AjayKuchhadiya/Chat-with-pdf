import os
from modules.store import create_db

def process_uploaded_files(files):
    folder_path = os.path.join("data/uploads")
    os.makedirs(folder_path, exist_ok=True)
    
    # Save all uploaded files
    for file in files:
        file_path = os.path.join(folder_path, file.name)
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())

    # Process and create a single database from all files
    create_db(folder_path)
