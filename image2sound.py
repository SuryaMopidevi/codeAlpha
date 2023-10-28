from PIL import Image
import pytesseract
from gtts import gTTS
import pygame
import os

# Load an image (replace 'image.png' with your image file)
image = Image.open('codeAlpha/image2.jpg')

# Use pytesseract to extract text from the image
text = pytesseract.image_to_string(image)

# Create a gTTS (Google Text-to-Speech) object
tts = gTTS(text)

# Save the generated speech as an audio file (e.g., 'output.mp3')
tts.save('output.mp3')

# Initialize the pygame mixer
pygame.mixer.init()

# Load and play the generated audio
pygame.mixer.music.load('output.mp3')
pygame.mixer.music.play()

# Wait for the audio to finish
while pygame.mixer.music.get_busy():
    pass

# Clean up by removing the audio file
os.remove('output.mp3')