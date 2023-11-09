from gtts import gTTS
import os
import pygame
import time


def gtts_test(text: str):
    tts = gTTS(text)
    fn = text.replace(" ", "").replace('<', "").replace(">","")
    tts.save(f"{fn[0:8]}.mp3")
    saying = pygame.mixer.Sound(f"{fn[0:8]}.mp3")
    saying.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Adjust the value inside tick() to control the speed of the loop
    
    pygame.mixer.music.stop()
    os.remove(f"{fn[:8]}.mp3") 
    return True