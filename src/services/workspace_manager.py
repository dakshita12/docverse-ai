from pathlib import Path

UPLOAD_FOLDER = Path("data/uploads")

def save_uploaded_file(uploaded_file):
    """
    Saves an uploaded document to the uploads folder.
    """
    UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

    file_path = UPLOAD_FOLDER / uploaded_file.name

    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    return True
