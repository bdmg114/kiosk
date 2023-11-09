import speech_recognition as sr
import threading
import pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
print(sr.__version__)

def get_ready_to_listen():
    r = sr.Recognizer()

    names = sr.Microphone.list_microphone_names()
    print(names)

    target_microphone_index = None
    target_microphone_name = '마이크 (USB PnP Sound Device)'
    
    for idx, name in enumerate(names):
        if target_microphone_name in name:
            target_microphone_index = idx
            break

    mic = sr.Microphone(device_index = 1)
    with mic as source:
        r.adjust_for_ambient_noise(source)
        return True

# Create an event to signal the completion of speech recognition
speech_recognition_complete = threading.Event()
def speech_recognition_thread(n):
    try:
        r = sr.Recognizer()
        names = sr.Microphone.list_microphone_names()
        print(names)

        target_microphone_index = None
        target_microphone_name = '마이크 (USB PnP Sound Device)'
        
        for idx, name in enumerate(names):
            if target_microphone_name in name:
                target_microphone_index = idx
                print(idx)
                break
        mic = sr.Microphone()

        with mic as source:
            r.adjust_for_ambient_noise(source)
            ding = pygame.mixer.Sound("ding.mp3")
            ding.play()
            audio = r.listen(source)
        result = r.recognize_google(audio, language="en-US")
        print(result)
        return result
    except:
        return ''

def start_speech_recognition():
    global speech_recognition_result
    speech_recognition_result = None  # Reset result variable
    speech_recognition_complete.clear()  # Clear the event flag
    speech_thread = threading.Thread(target=speech_recognition_thread)
    speech_thread.start()
    # Wait for the event to be set (speech recognition completion)
    speech_recognition_complete.wait()
    return speech_recognition_result