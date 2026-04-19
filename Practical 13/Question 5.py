import PyPDF2

# Open the original PDF
input_pdf = r"C:\Users\Bagia Maryam Moosaji\Downloads\SL - Lab Activities (all).pdf"  # replace with your actual file name
output_pdf = 'SL - Lab activities (all).pdf'     # name for the new PDF

# Pages to remove (subtracting 1 because Python indexing starts from 0)
pages_to_remove = [0, 4, 6, 9, 12, 16, 21, 24, 26, 29, 31, 33, 36, 39, 42]

reader = PyPDF2.PdfReader(input_pdf)
writer = PyPDF2.PdfWriter()

for i in range(len(reader.pages)):
    if i not in pages_to_remove:
        writer.add_page(reader.pages[i])

# Save the new PDF
with open(output_pdf, 'wb') as f:
    writer.write(f)

print(f"Created new PDF without pages: {pages_to_remove}")
