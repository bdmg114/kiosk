import speech_recognition as sr

print(sr.__version__)

def listen():
    r = sr.Recognizer()

    names = sr.Microphone.list_microphone_names()
    print(names)

    mic = sr.Microphone(device_index = 2)
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("listening...")
        audio = r.listen(source)

    result = r.recognize_google(audio, language = "en-US")
    return result