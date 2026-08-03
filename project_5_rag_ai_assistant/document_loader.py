# Create a function to load text documents
def load_document(file_path):

    # Open the file in read mode
    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        # Read all text from the file
        text = file.read()

    # Return the document content
    return text