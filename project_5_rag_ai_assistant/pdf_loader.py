# Import PDF reader library
from pypdf import PdfReader


# Create function to extract text from PDF
def load_pdf(file_path):

    # Open PDF file
    reader = PdfReader(
        file_path
    )


    # Create empty text storage
    text = ""


    # Loop through every PDF page
    for page in reader.pages:

        # Extract text from current page
        page_text = page.extract_text()

        # Add page text to full document
        text += page_text


    # Return extracted PDF text
    return text