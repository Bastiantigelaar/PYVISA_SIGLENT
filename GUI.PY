# simpele GUI voor een functie generator 
# gemaakt door Bastian Tigelaar
# pyvisa related stuff
import pyvisa
import time
import numpy as np
# GUI for function generator stuff
import tkinter as tk
import json
from tkinter import *
from tkinter import ttk
from tkinter import END

# -------------------- fucnties ------------------------
# selection .....
# sinus_button
def select_sinus():
    try:
        labeldutycycle.grid_forget()
        entrydutycycle.grid_forget()
        functie_generator.write('C1:BSWV WVTP,SINE')
    except:
        print("an error occurred")
# blokgolf
def select_blok():
    try:
        functie_generator.write('C1:BSWV WVTP,SQUARE')
        labeldutycycle.grid(row=5,column=0)
        entrydutycycle.grid(row=5, column=1)
    except:
        print("an error occurred")
#ramp 
def select_ramp():
    try:
        functie_generator.write('C1:BSWV WVTP,RAMP')
    except:
        print("an error occurred")
#pulse 
def select_pulse():
    try:
        functie_generator.write('C1:BSWV WVTP,PULSE')
    except:
        print("an error occurred")
#noise
def select_noise():
    try:
        functie_generator.write('C1:BSWV WVTP,NOISE')
    except:
        print("an error occurred")
#arb
def select_arb():
    try:
        functie_generator.write('C1:BSWV WVTP,ARB')
    except:
        print("an error occurred")
# hide buttons....
def hide_boxes():
    try:
        labeldutycycle.grid_forget()
        entrydutycycle.grid_forget()
    except:
        print("an error occurred")


# set to function generator
def set_values():
    try:
        amp = float(entryamplitude.get())
        fre = float(entryfrequenctie.get())
        phase = float(entryphase.get())
        offset = float(entryoffset.get())
        dutycycle = float(entrydutycycle.get())
        if(offset > 4.5):
            print("kies een offset lager of gelijk aan 4.5")
            offset = 4.5
        elif(phase > 360):
            phase = 360
            print("kies een phase kleiner of gelijk aan 360")
        elif(amp > 20):
            amp = 20
            print("kies een amplitude lager of gelijk aan 20")
        elif(fre > 10000000):
            fre = 10e6
        elif(dutycycle < 20):
             dutycycle = 20
             print("vul groter in dan 230 %")   
        
        print("kies een frequency lager of gelijk aan 10Mhz")
        functie_generator.write(f'C1:BSWV FRQ,{fre}')
        functie_generator.write(f'C1:BSWV AMP,{amp}')
        functie_generator.write(f'C1:BSWV OFST,{offset}')
        functie_generator.write(f'C1:BSWV PHSE,{phase}')
        print("De ingevulde waarde zijn ", "amp ", amp, " freq", fre)
        try:
            functie_generator.write(f'C1:BSWV DUTY,{dutycycle}') 
        except:
            print("fault dutycycle")
    except:
        print("error occurred")


# Open a resource manager..
rm = pyvisa.ResourceManager()
# the devices connected to it, now only function generator works..
#scope = rm.open_resource('USB0::0x049F::0x505E::CN2210029021121::INSTR')
functie_generator = rm.open_resource('USB0::0xF4ED::0xEE3A::SDG08CBC7R0184::0::INSTR') #functie generator thuis 
#test IDN 
#print(scope.query("*IDN?"))

# GUI 

window = tk.Tk()
window.geometry('1000x900')
style = ttk.Style()
style.theme_use("clam")
style.configure('Treeview.Heading', background="#008ae6", font=('Arial', 15))
window.configure(bg="#99d6ff") 


# button sinus 
button_sinus = tk.Button(window, text = "sinus", command=select_sinus)
button_sinus.grid(row = 0, column = 0, sticky=tk.W)
# button blok
button_sinus = tk.Button(window, text = "blok", command=select_blok)
button_sinus.grid(row = 0, column = 1, sticky=tk.W)
# button ramp 
button_sinus = tk.Button(window, text = "ramp", command=select_ramp)
button_sinus.grid(row = 0, column = 2, sticky=tk.W)
# button pulse 
button_sinus = tk.Button(window, text = "pulse", command=select_pulse)
button_sinus.grid(row = 0, column = 3, sticky=tk.W)
# button noise
button_sinus = tk.Button(window, text = "noise", command=select_noise)
button_sinus.grid(row = 0, column = 4, sticky=tk.W)
#button arb
button_sinus = tk.Button(window, text = "arb", command=select_arb)
button_sinus.grid(row = 0, column = 5, sticky=tk.W)

# invul informatie over de sinus format...
# frequency 
labelfrequenctie = tk.Label(window,text="Vul hier de Ferquentie in ")
labelfrequenctie.grid(row = 1, column = 0, sticky=tk.W)

entryfrequenctie = tk.Entry(window)
entryfrequenctie.grid(row = 1, column=1,sticky=tk.W)

#amplitude 

labelamplitude = tk.Label(window,text="Vul hier de amplitude in ")
labelamplitude.grid(row = 2, column = 0, sticky=tk.W)

entryamplitude = tk.Entry(window)
entryamplitude.grid(row = 2, column=1,sticky=tk.W)
# offset 
labeloffset = tk.Label(window,text="Vul hier de offset in ")
labeloffset.grid(row = 3, column = 0, sticky=tk.W)

entryoffset = tk.Entry(window)
entryoffset.grid(row = 3, column=1,sticky=tk.W)

# phase 

labelphase = tk.Label(window,text="Vul hier de fase in ")
labelphase.grid(row = 4, column = 0, sticky=tk.W)

entryphase = tk.Entry(window)
entryphase.grid(row = 4, column=1,sticky=tk.W)

# duty cycle 

labeldutycycle = tk.Label(window,text="vul hier de duty cycle in ")
labeldutycycle.grid(row = 5, column = 0, sticky=tk.W)

entrydutycycle = tk.Entry(window)
entrydutycycle.grid(row = 5, column=1,sticky=tk.W)
hide_boxes() 

# ACCEPT CHANGES BUTTON 

checkbutton = tk.Button(window, text = "Check", command = set_values)
checkbutton.grid(row = 6, column = 0, sticky=tk.W)




start_frequency = 1

functie_generator.write('C1:BSWV WVTP,SINE')
window.mainloop()
#while start_frequency != 460:
 #   functie_generator.write(f'C1:BSWV FRQ,{start_frequency}')
  #  functie_generator.write('C1:BSWV AMP,1')
   # start_frequency = start_frequency+ 1
   # time.sleep(0.2)

# Set measurement type to frequency
# main loop 
# Close the connection to all devices.
functie_generator.close()
rm.close()