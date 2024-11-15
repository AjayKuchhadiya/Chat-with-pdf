import os
import json
from modules.store import create_db

# Path to metadata mapping file
METADATA_FILE = "data/metadata.json"

def process_uploaded_files(files):
    folder_path = os.path.join("data/uploads")
    os.makedirs(folder_path, exist_ok=True)
    metadata = {}

    # Load existing metadata if available
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, "r") as f:
            metadata = json.load(f)

    # Save each file and create separate vector store
    for file in files:
        file_path = os.path.join(folder_path, file.name)
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())
        
        # Create a separate database for each PDF
        vector_store_path = create_db(file_path)
        metadata[file.name] = vector_store_path

    # Save metadata back to file
    with open(METADATA_FILE, "w") as f:
        json.dump(metadata, f)
