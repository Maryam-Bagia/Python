import PyPDF2

# Open the original PDF
input_pdf = r"C:\Users\Bagia Maryam Moosaji\Downloads\ST Lab manual (edited).pdf" # notice the 'r' before string
output_pdf = 'ST Lab Manual (removed pages).pdf'  # name for the new PDF

# Pages to remove (subtracting 1 because Python indexing starts from 0)
pages_to_remove = [67, 68, 69, 77, 78, 86, 87, 93, 106, 107, 108, 116, 117, 118, 126, 127, 134, 150, 151, 152, 165, 177]

reader = PyPDF2.PdfReader(input_pdf)
writer = PyPDF2.PdfWriter()

for i in range(len(reader.pages)):
    if i not in pages_to_remove:
        writer.add_page(reader.pages[i])

# Save the new PDF
with open(output_pdf, 'wb') as f:
    writer.write(f)

print(f"Created new PDF without pages: {pages_to_remove}")