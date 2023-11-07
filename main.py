import speech_to_text
import kiosk_backend
import text_to_speech
from tkinter import *
import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.tk.config(menu=self.blank_menu) 
        self.attributes('-fullscreen',True)
        self.title("my app")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        

        self.checkbox_frame = customtkinter.CTkFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")
        self.checkbox_1 = customtkinter.CTkCheckBox(self.checkbox_frame, text="checkbox 1")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self.checkbox_frame, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("button pressed")
app = App()
app.mainloop()
s = kiosk_backend.start()
if s != '!P':
    q = 'k'
    while q != '':
        if text_to_speech.gtts_test(s):
            q = speech_to_text.listen()
            s = kiosk_backend.get_input(q)
    print(kiosk_backend.output())
    