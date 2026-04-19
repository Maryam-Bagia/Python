import PyPDF2

# Open the original PDF
input_pdf = r"C:\Users\Bagia Maryam Moosaji\Downloads\Cloud Computing.pdf"  # notice the 'r' before string
output_pdf = 'CC Lab Manual (removed blank pages).pdf'  # name for the new PDF

# Pages to remove (subtracting 1 because Python indexing starts from 0)
pages_to_remove = [0, 7, 13, 18, 26, 34, 41, 45, 53, 56, 63, 68, 77]

reader = PyPDF2.PdfReader(input_pdf)
writer = PyPDF2.PdfWriter()

for i in range(len(reader.pages)):
    if i not in pages_to_remove:
        writer.add_page(reader.pages[i])

# Save the new PDF
with open(output_pdf, 'wb') as f:
    writer.write(f)

print(f"Created new PDF without pages: {pages_to_remove}")