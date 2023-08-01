**Deepl-docx-Batch-Translation**

The DeepL Document Translator is a Python script designed to streamline the translation of multiple .docx documents. Leveraging the power of the DeepL API, this script automates the translation process, converting documents from a source language (e.g., Hungarian) to English (EN-US) with ease.

**Key Features:**

- **Efficient Batch Translation:** The script efficiently handles a batch of .docx files in a specified input directory, automatically translating each document using the DeepL API.

- **User-friendly Configuration:** Users can easily customize the source and target languages as needed. Additionally, the script allows users to adjust the formality level of the translation.

- **Output Directory:** Translated documents are saved in a specified output directory, keeping the translated versions separate from the originals.

**Requirements:**

- Python 3.x
- [deepl](https://pypi.org/project/deepl/) Python package
- DeepL API key

**How to Use:**

1. Clone the repository to your local machine.
2. Install the required Python packages using `pip install deepl`.
3. Replace `YOUR_AUTH_KEY` with your DeepL API key in the script.
4. Set the `input_directory` variable to the path containing the .docx files you want to translate.
5. Set the `output_directory` variable to the path where you want to save the translated .docx files.
6. Run the script using `python script.py`.
7. Sit back and let the script handle the translation process for you!

**License:**

This project is licensed under the MIT License, ensuring its open-source nature and granting users the freedom to use, modify, and distribute the code.

**Acknowledgments:**

- DeepL: A special thanks to DeepL for providing the powerful translation API, enabling seamless language translation for users worldwide.

Empower your document translation workflow with the DeepL Document Translator and save time and effort in the translation process. Whether you're a language enthusiast or a professional needing accurate translations, this script is your gateway to effortless document translation.
