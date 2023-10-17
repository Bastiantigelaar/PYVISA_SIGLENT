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
# sweep
def select_sweep():
    try:
        hide_before_sweep()
        sweeplabelentries.grid(row = 0, column=0)
        
        functie_generator.write('C1:SWWV STATE,ON')
    except:
        print("an error occurred")

# hide buttons....
def hide_boxes():
    try:
        labeldutycycle.grid_forget()
        entrydutycycle.grid_forget()
    except:
        print("an error occurred")
def hide_before_sweep():
    try: 
        frame_labels_entries.grid_forget()
    except:
        print("an error occurred")
def hide_after_sweep():
    try:
        sweeplabelentries.grid_forget()
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
def set_sweep():
    try:
        sweep_time = float(entrie_sweep_time.get())
        sweep_stop = float(entrie_sweep_stopfrequenctie.get())
        sweep_start = float(entrie_sweep_startfrequenctie.get())

        print("dit is de sweep time ", sweep_time, " dit is de sweep stop",sweep_stop," dit is de start ",sweep_start)
        if(sweep_time < 0):
            print("vul een tijd groter dan 0 in")
            sweep_time = 0.001
        
        functie_generator.write(f'C1:SWWV TIME,{sweep_time}') 
        functie_generator.write(f'C1:SWWV STOP,{sweep_stop}') 
        functie_generator.write(f'C1:SWWV START,{sweep_start}')  
        functie_generator.write('C1:SWWV STATE,ON')    
    except:
        print("an error occurred")


# Open a resource manager..
# the devices connected to it, now only function generator works..
#scope = rm.open_resource('USB0::0x049F::0x505E::CN2210029021121::INSTR')
rm = pyvisa.ResourceManager()
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
button_sinus.grid(row = 7, column = 0, sticky=tk.W)
# button blok
button_blok = tk.Button(window, text = "blok", command=select_blok)
button_blok.grid(row = 7, column = 1, sticky=tk.W)
# button ramp 
button_ramp = tk.Button(window, text = "ramp", command=select_ramp)
button_ramp.grid(row = 7, column = 2, sticky=tk.W)
# button pulse 
button_pulse = tk.Button(window, text = "pulse", command=select_pulse)
button_pulse.grid(row = 7, column = 3, sticky=tk.W)
# button noise
button_noise = tk.Button(window, text = "noise", command=select_noise)
button_noise.grid(row = 7, column = 4, sticky=tk.W)
#button arb
button_arb = tk.Button(window, text = "arb", command=select_arb)
button_arb.grid(row = 7, column = 5, sticky=tk.W)
# sweep / eigen functie bepalen 
button_sweep = tk.Button(window, text = "sweep", command=select_sweep)
button_sweep.grid(row = 7, column = 6, sticky=tk.W)





frame_labels_entries = tk.Frame(window)
frame_labels_entries.grid(row = 0,column=0)
# invul informatie over de sinus format...
# frequency 
labelfrequenctie = tk.Label(frame_labels_entries,text="Vul hier de Ferquentie in ")
labelfrequenctie.grid(row = 1, column = 0, sticky=tk.W)

entryfrequenctie = tk.Entry(frame_labels_entries)
entryfrequenctie.grid(row = 1, column=1,sticky=tk.W)

#amplitude 

labelamplitude = tk.Label(frame_labels_entries,text="Vul hier de amplitude in ")
labelamplitude.grid(row = 2, column = 0, sticky=tk.W)

entryamplitude = tk.Entry(frame_labels_entries)
entryamplitude.grid(row = 2, column=1,sticky=tk.W)
# offset 
labeloffset = tk.Label(frame_labels_entries,text="Vul hier de offset in ")
labeloffset.grid(row = 3, column = 0, sticky=tk.W)

entryoffset = tk.Entry(frame_labels_entries)
entryoffset.grid(row = 3, column=1,sticky=tk.W)

# phase 

labelphase = tk.Label(frame_labels_entries,text="Vul hier de fase in ")
labelphase.grid(row = 4, column = 0, sticky=tk.W)

entryphase = tk.Entry(frame_labels_entries)
entryphase.grid(row = 4, column=1,sticky=tk.W)

# duty cycle 

labeldutycycle = tk.Label(frame_labels_entries,text="vul hier de duty cycle in ")
labeldutycycle.grid(row = 5, column = 0, sticky=tk.W)

entrydutycycle = tk.Entry(frame_labels_entries)
entrydutycycle.grid(row = 5, column=1,sticky=tk.W)
# ACCEPT CHANGES BUTTON 

checkbutton = tk.Button(window, text = "Check", command = set_values)
checkbutton.grid(row = 6, column = 0, sticky=tk.W)

hide_boxes() 

sweeplabelentries = tk.Frame(window)
sweeplabelentries.grid(row = 0,column=0)

# sweep time
label_sweep_time = tk.Label(sweeplabelentries,text="vul hier de sweep time in")
label_sweep_time.grid(row = 1,column= 0)
entrie_sweep_time = tk.Entry(sweeplabelentries)
entrie_sweep_time.grid(row = 1,column= 1)

# start frequenctie 

label_sweep_startfrequenctie = tk.Label(sweeplabelentries,text="vul hier de start frequentie in")
label_sweep_startfrequenctie.grid(row = 2,column= 0)
entrie_sweep_startfrequenctie = tk.Entry(sweeplabelentries)
entrie_sweep_startfrequenctie.grid(row = 2,column= 1)

# stop frequentie

label_sweep_stopfrequenctie = tk.Label(sweeplabelentries,text="vul hier de stop frequentie in")
label_sweep_stopfrequenctie.grid(row = 3,column= 0)
entrie_sweep_stopfrequenctie = tk.Entry(sweeplabelentries)
entrie_sweep_stopfrequenctie.grid(row = 3,column= 1)

# check button for sweeep 
checkbutton_sweep = tk.Button(window, text = "Check", command = set_sweep)
checkbutton_sweep.grid(row = 6, column = 0, sticky=tk.W)

hide_after_sweep()





start_frequency = 1

#functie_generator.write('C1:BSWV WVTP,SINE')
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
