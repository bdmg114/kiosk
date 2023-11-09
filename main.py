import speech_to_text
import kiosk_backend
import text_to_speech
from tkinter import *
from tkinter import messagebox
import customtkinter
import os
import time
import pygame
from tkinter.simpledialog import askstring
import argparse
import socket_sender

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

parser = argparse.ArgumentParser()

parser.add_argument('--voiceRecog',type=bool,default=False)
parser.add_argument('--micN',type=int,default=1)
parser.add_argument('--IP',type=str,default='172.16.5.106')

args = parser.parse_args()

voiceRecognization = args.voiceRecog
n = args.micN
ip = args.IP

socket_sender.init(ip)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.orders = {
            "menu_items": ['milsut shake swamp', 'mil worm forest salads', 'dim island'],
            "quantities": [0,0,0],
            "extra_info": ['','','']
        }

        self.title("my app")
        self.attributes("-fullscreen", True)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        

        self.checkbox_frame = customtkinter.CTkFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.shake_button = customtkinter.CTkButton(self.checkbox_frame, text="milsut shake swamp", command=lambda: self.order(0))
        self.shake_button.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.salad_button = customtkinter.CTkButton(self.checkbox_frame, text="mil worm forest salads", command=lambda: self.order(1))
        self.salad_button.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.DIMSUM_button = customtkinter.CTkButton(self.checkbox_frame, text="dim island", command=lambda: self.order(2))
        self.DIMSUM_button.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="ew")


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

        self.AIbutton = customtkinter.CTkButton(self, text="Order with AI", command=self.AI_Button)
        self.AIbutton.grid(row=3, column=0, padx=10, pady=5, sticky="ew", columnspan=2)
        self.button = customtkinter.CTkButton(self, text="Order", command=self.button_callback)
        self.button.grid(row=4, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
    
    def set_quatity_text(self):
        self.sum_quant.configure(text = str(self.orders['quantities'][2]))
        self.salad_quant.configure(text = str(self.orders['quantities'][1]))
        self.shake_quant.configure(text = str(self.orders['quantities'][0]))
        
    def order(self,menu):
        self.orders['quantities'][menu] += 1
        self.set_quatity_text()
    
    def button_callback(self):
        print(self.orders)
        socket_sender.send_order(self.orders)
        self.orders = {
            "menu_items": ['milsut shake swamp', 'mil worm forest salads', 'dim island'],
            "quantities": [0,0,0],
            "extra_info": ['','','']
        }

        main_window_width = self.winfo_width()
        main_window_height = self.winfo_height()

        # Calculate the position to center the modal dialog
        modal_width = int(main_window_width/3) # Width of the modal dialog
        modal_height = int(main_window_height/3)  # Height of the modal dialog
        x_position = (main_window_width - modal_width) // 2
        y_position = (main_window_height - modal_height) // 2

        self.set_quatity_text()
        modal_dialog = Toplevel(self)
        modal_dialog.title("")
        modal_dialog.overrideredirect(1)  # Remove window decorations (including title bar)
        modal_dialog.geometry(f"{modal_width}x{modal_height}+{x_position}+{y_position}")
        modal_dialog.grab_set()  # Grab focus and block interactions with other windows
        
        modal_dialog.grid_columnconfigure(0, weight=1)
        modal_dialog.grid_rowconfigure(0, weight=1)

        # Add a label to the modal dialog
        processing_label = customtkinter.CTkLabel(modal_dialog, text="Order completed")
        processing_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.update()

        time.sleep(2)

        modal_dialog.destroy()

    def AI_Button(self):
        main_window_width = self.winfo_width()
        main_window_height = self.winfo_height()

        # Calculate the position to center the modal dialog
        modal_width = int(main_window_width/3) # Width of the modal dialog
        modal_height = int(main_window_height/3)  # Height of the modal dialog
        x_position = (main_window_width - modal_width) // 2
        y_position = (main_window_height - modal_height) // 2

        # Create a modal dialog window without a title bar and center it
        modal_dialog = Toplevel(self)
        modal_dialog.title("")
        modal_dialog.overrideredirect(1)  # Remove window decorations (including title bar)
        modal_dialog.geometry(f"{modal_width}x{modal_height}+{x_position}+{y_position}")
        modal_dialog.grab_set()  # Grab focus and block interactions with other windows

        # Add a label to the modal dialog
        processing_label = Label(modal_dialog, text="Getting ready...")
        processing_label.pack(padx=20, pady=20)

        self.update()

        try:
            # Call the backend processing functions
            s = kiosk_backend.start()
            if s != '!P':
                q = 'k'
                while q != '':
                    print(s)
                    if text_to_speech.gtts_test(s):
                        print("said")
                        if voiceRecognization:
                            q = speech_to_text.speech_recognition_thread(n)
                        else:
                            q = askstring('Give answer', s)
                        s = kiosk_backend.get_input(q)
                out = kiosk_backend.output()
                print(out)
                for x in range(len(out['quantities'])):
                    self.orders['quantities'][self.orders['menu_items'].index(out['menu_items'][x].lower())] += out['quantities'][x]
                self.sum_quant.configure(text = str(self.orders['quantities'][2]))
                self.salad_quant.configure(text = str(self.orders['quantities'][1]))
                self.shake_quant.configure(text = str(self.orders['quantities'][0]))
        except Exception as e:
            print(e)
            self.after(0, lambda err=e: self.show_error_message(str(err)))
        # Close the modal dialog after processing or displaying error
        finally:
            modal_dialog.destroy()
    def show_error_message(self, error_message):
        messagebox.showerror("Error", error_message)
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
    