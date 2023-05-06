# pip install pdfplumber
# pip install gtts

import os
import pdfplumber
from gtts import gTTS

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

def convert_text_to_audio(text, audio_path):
    tts = gTTS(text=text, lang='en')
    tts.save(audio_path)

def main():
    pdf_path = input('Enter the path to the PDF file: ')
    if not os.path.exists(pdf_path) or not pdf_path.endswith('.pdf'):
        print("Invalid PDF file path.")
        return

    audio_path = os.path.splitext(pdf_path)[0] + '.mp3'
    text = extract_text_from_pdf(pdf_path)
    
    if text.strip():
        convert_text_to_audio(text, audio_path)
        print(f"Audio file created: {audio_path}")
    else:
        print("The PDF file does not contain any extractable text.")

if __name__ == '__main__':
    main()
