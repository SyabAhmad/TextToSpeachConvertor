import PyPDF3
import pdfplumber
import pyttsx3
file = "TTS.txt"

book = open(file, 'rb')
PdfReader = PyPDF3.PDFReader(book)
pages = pdfReader.numPages
finaltxt = ""
with pdfplumber.open(file) as dpf:
    for i in range(pages):
        pages = pdf.pages[i]
        text = pages.extract_text()
        finaltxt = finaltxt + text


        engine = pyttsx3.init()
        engine.runAndWait()


