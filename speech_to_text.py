import speech_recognition as sr
import threading
import pygame

print(sr.__version__)

def get_ready_to_listen():
    r = sr.Recognizer()

    names = sr.Microphone.list_microphone_names()
    print(names)

    mic = sr.Microphone(device_index = 2)
    with mic as source:
        r.adjust_for_ambient_noise(source)
        return True

# Create an event to signal the completion of speech recognition
speech_recognition_complete = threading.Event()
def speech_recognition_thread():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=2)
    with mic as source:
        r.adjust_for_ambient_noise(source)
        ding = pygame.mixer.Sound("ding.mp3")
        ding.play()
        audio = r.listen(source)
    result = r.recognize_google(audio, language="en-US")
    # Process the recognized speech result
    speech_recognition_result = result
    # Set the event to signal completion
    speech_recognition_complete.set()

def start_speech_recognition():
    global speech_recognition_result
    speech_recognition_result = None  # Reset result variable
    speech_recognition_complete.clear()  # Clear the event flag
    speech_thread = threading.Thread(target=speech_recognition_thread)
    speech_thread.start()
    # Wait for the event to be set (speech recognition completion)
    speech_recognition_complete.wait()
    return speech_recognition_result