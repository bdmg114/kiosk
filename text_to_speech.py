from playsound import playsound
from gtts import gTTS
import os
import pygame
import time

pygame.mixer.init()
def gtts_test(text: str):
    tts = gTTS(text)
    fn = text.replace(" ", "").replace('<', "").replace(">","")
    tts.save(f"{fn[0:8]}.mp3")
    saying = pygame.mixer.Sound(f"{fn[0:8]}.mp3")
    saying.play()
    time.sleep(saying.get_length())
    os.remove(f"{fn[0:8]}.mp3") 
    return True