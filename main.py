import speech_to_text
import kiosk_backend
import text_to_speech
from tkinter import *
import customtkinter
import os

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.orders = {
            "menu_items": ['milsut shake swamp', 'mil worm forest salads', 'dim island'],
            "quantities": [0,0,0],
            "extra_info": ['','','']
        }

        self.title("my app")
        self.geometry('800x480')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        

        self.checkbox_frame = customtkinter.CTkFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.shake_button = customtkinter.CTkButton(self.checkbox_frame, text="milsut shake swamp", command=lambda: self.order(0))
        self.shake_button.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.salad_button = customtkinter.CTkButton(self.checkbox_frame, text="mil worm forest salads", command=lambda: self.order(1))
        self.salad_button.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.DIMSUM_button = customtkinter.CTkButton(self.checkbox_frame, text="dim island", command=lambda: self.order(2))
        self.DIMSUM_button.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")

        self.orders_frame = customtkinter.CTkFrame(self)
        self.orders_frame.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsew")
        self.shake_name = customtkinter.CTkLabel(self.orders_frame, text='Milsut shake swamp')
        self.shake_name.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
        self.shake_quant = customtkinter.CTkLabel(self.orders_frame, text=str(self.orders['quantities'][0]))
        self.shake_quant.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="ew")
        self.salad_name = customtkinter.CTkLabel(self.orders_frame, text='mil worm forest salads')
        self.salad_name.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ew")
        self.salad_quant = customtkinter.CTkLabel(self.orders_frame, text=str(self.orders['quantities'][1]))
        self.salad_quant.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="ew")
        self.sum_name = customtkinter.CTkLabel(self.orders_frame, text='dim island')
        self.sum_name.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="ew")
        self.sum_quant = customtkinter.CTkLabel(self.orders_frame, text=str(self.orders['quantities'][2]))
        self.sum_quant.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="ew")

        self.button = customtkinter.CTkButton(self, text="Order", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
    def order(self,menu):
        self.orders['quantities'][menu] += 1
        self.sum_quant.configure(text = str(self.orders['quantities'][2]))
        self.salad_quant.configure(text = str(self.orders['quantities'][1]))
        self.shake_quant.configure(text = str(self.orders['quantities'][0]))
        
    def button_callback(self):
        print(self.orders)
        self.orders = {
            "menu_items": ['milsut shake swamp', 'mil worm forest salads', 'dim island'],
            "quantities": [0,0,0],
            "extra_info": ['','','']
        }
        self.sum_quant.configure(text = str(self.orders['quantities'][2]))
        self.salad_quant.configure(text = str(self.orders['quantities'][1]))
        self.shake_quant.configure(text = str(self.orders['quantities'][0]))



app = App()
app.mainloop()
# s = kiosk_backend.start()
# if s != '!P':
#     q = 'k'
#     while q != '':
#         if text_to_speech.gtts_test(s):
#             q = speech_to_text.listen()
#             s = kiosk_backend.get_input(q)
#     print(kiosk_backend.output())
    