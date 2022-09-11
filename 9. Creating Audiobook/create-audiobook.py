# import Python Modules

import PyPDF2
import pyttsx3

pdf_dir = "pdf/"

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
PDF_Reader = PyPDF2.PdfFileReader(open(f"{pdf_dir}sample.pdf", "rb"))
for i in range(PDF_Reader.numPages):
    Text = PDF_Reader.getPage(i).extractText()
    engine.say(Text)
    engine.runAndWait()