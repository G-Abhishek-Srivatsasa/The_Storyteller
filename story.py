import pyttsx3
import PyPDF2

# -------- STEP 1: Initialize Text-to-Speech engine --------
speaker = pyttsx3.init()

# -------- STEP 2: List available voices --------
voices = speaker.getProperty('voices')
print("\nAvailable Voices: 0, 1")
for index, voice in enumerate(voices):
    print(f"{index}: {voice.name} ({voice.languages})")

# -------- STEP 3: Let user choose a voice --------
voice_choice = int(input("\nEnter the voice number you want: "))
speaker.setProperty('voice', voices[voice_choice].id)

#  Adjust speech rate
speaker.setProperty('rate', 125)

# -------- STEP 4: Read PDF file --------
pdf = open('story.pdf', 'rb')  # replace with your file
pdf_reader = PyPDF2.PdfReader(pdf)

full_text = ""
for page in pdf_reader.pages:
    text = page.extract_text()
    if text:
        full_text += text + "\n"

pdf.close()

# -------- STEP 5: Speak the text --------
speaker.say(full_text)
speaker.runAndWait()
