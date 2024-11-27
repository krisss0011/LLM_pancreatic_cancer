import fitz  # PyMuPDF
import os

def extract_text_from_pdfs(pdf_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through all PDFs in the folder
    for file_name in os.listdir(pdf_folder):
        if file_name.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, file_name)
            output_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.txt")

            try:
                # Open the PDF and extract text
                with fitz.open(pdf_path) as pdf:
                    text = ""
                    for page in pdf:
                        text += page.get_text()

                # Save the extracted text to a .txt file
                with open(output_path, "w", encoding="utf-8") as text_file:
                    text_file.write(text)
                print(f"Extracted text from {file_name} to {output_path}")
            except Exception as e:
                print(f"Error processing {file_name}: {e}")

# Example usage
if __name__ == "__main__":
    pdf_folder = "./projektnaNaloga/arxiv_papers"
    output_folder = "./projektnaNaloga/text_data"

    extract_text_from_pdfs(pdf_folder, output_folder)
