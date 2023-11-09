from gtts import gTTS
import os
import pygame
import time
from threading import Timer


def gtts_test(text: str):
    tts = gTTS(text)
    fn = text.replace(" ", "").replace('<', "").replace(">","")
    tts.save(f"{fn[0:8]}.mp3")
    saying = pygame.mixer.Sound(f"{fn[0:8]}.mp3")
    saying.play()
    t = Timer(saying.get_length(), fin(fn))
    pygame.mixer.music.stop()  # Adjust the value inside tick() to control the speed of the loop
    return t
    

def fin(fn):
    os.remove(f"{fn[:8]}.mp3") 
    return True
