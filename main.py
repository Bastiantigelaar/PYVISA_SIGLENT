import tkinter
import tkinter.messagebox
import customtkinter
from appclass import *
#from field import *
# -------------------- fucnties ------------------------
# selection .....
# sinus_butto
customtkinter.set_appearance_mode("dark") # set the color mode / dark mode
customtkinter.set_default_color_theme("dark-blue") # set all widget color themes
# function                
# runs the main loop        
#rm = pyvisa.ResourceManager()
#functie_generator = rm.open_resource('USB0::0xF4ED::0xEE3A::SDG08CBC7R0184::0::INSTR') 
if __name__ == "__main__":
    app = App()
    app.mainloop()
