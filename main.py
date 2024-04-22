import PyPDF2

pdf_files = ["test.pdf", "test2.pdf"]  # Corrected variable name (snake_case)
merger = PyPDF2.PdfMerger()

for filename in pdf_files:
    with open(filename, 'rb') as pdf_file:  # Use context manager for proper file handling
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        merger.append(pdf_reader)

# No need to close pdf_files (it's a list)
merger.write("merged.pdf")  # Corrected filename to avoid overwriting "merger.pdf"
