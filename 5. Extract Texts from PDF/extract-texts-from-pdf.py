# import PyPdf2
import PyPDF2

pdf_dir = "pdf/"

pdf_file = open(f"{pdf_dir}dummy.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

text = pdf_reader.getPage(0).extractText()
print(text)