import os
import deepl

# Function to translate a document
def translate_document(input_path, output_path):
    try:
        # Using translate_document_from_filepath() with file paths
        translator.translate_document_from_filepath(
            input_path,
            output_path,
            target_lang="EN-US",  # Translate to English
            source_lang="HU",  # Hungarian is detected automatically
            formality="default"  # You can adjust the formality level as needed
        )
    except deepl.DocumentTranslationException as error:
        # If an error occurs during document translation after the document was
        # already uploaded, a DocumentTranslationException is raised. The
        # document_handle property contains the document handle that may be used to
        # later retrieve the document from the server, or contact DeepL support.
        doc_id = error.document_handle.id
        doc_key = error.document_handle.key
        print(f"Error after uploading ${error}, id: ${doc_id} key: ${doc_key}")
    except deepl.DeepLException as error:
        # Errors during upload raise a DeepLException
        print(error)


# Input and output directories
input_directory = "/Users/X/Documents/deepl_file"
output_directory = "/Users/X/Documents/deepl_file/translated"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

auth_key="9X2XaX8X-X6X5-XaX0-X5X6-X0X8XeX4XcX4:fx"

# Initialize the DeepL translator
translator = deepl.Translator(auth_key)  # Replace "YOUR_AUTH_KEY" with your DeepL API key

# Loop through each document and translate it
for i in range(1, 114):  # Assuming you have 113 documents named as part-1.docx to part-113.docx
    input_path = os.path.join(input_directory, f"part-{i}.docx")
    output_path = os.path.join(output_directory, f"part-{i}_translated.docx")
    translate_document(input_path, output_path)
