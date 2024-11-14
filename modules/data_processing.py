import os
from modules.store import create_db

def process_uploaded_files(file):
    file_path = os.path.join("data/uploads", file.name)
    os.makedirs("data/uploads", exist_ok=True)
    
    # Save uploaded file
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())
    
    folder_path =  os.path.join("data/uploads")
    create_db(folder_path)