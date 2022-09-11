# import Python Modules

import PyPDF2
import pyttsx3

pdf_dir = "pdf/"
audio_dir = "audio/"

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
PDF_Reader = PyPDF2.PdfFileReader(open(f"{pdf_dir}sample.pdf", "rb"))
for i in range(PDF_Reader.numPages):
    Text = PDF_Reader.getPage(i).extractText()
    engine.save_to_file(Text, f"{audio_dir}audio{i}.mp3")
    engine.runAndWait()