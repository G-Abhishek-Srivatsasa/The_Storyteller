import pyttsx3 
import PyPDF2

# Open the pdf file
book = open("story.pdf","rb")
pdf_reader = PyPDF2.PdfReader(book)
# Initialising the speaker
speaker = pyttsx3.init()

for page_num in range(len(pdf_reader.pages)):
    text  = pdf_reader.pages[page_num].extract_text()
    speaker.say(text)
    speaker.runAndWait()
    speaker.stop()
    rate = speaker.getProperty("rate")
    speaker.setProperty("rate",150) # for slower voice

    voices = speaker.getProperty("voices")
    speaker.setProperty("voice",voices[1])

speaker.stop()