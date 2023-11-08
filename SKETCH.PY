
# version 1 - can be deleted  !!!!!!!11

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
import customtkinter
# -------------------- fucnties ------------------------
# selection .....
# sinus_button
customtkinter.set_appearance_mode("dark")

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
root = customtkinter.CTk()
root.geometry('1920x1080')
# een prachtige titel voor deze GUI 
input_header = customtkinter.CTkLabel(master=root,text="Een GUI voor de SIGLENT functie generator en TEKTRONIS scope ",font=("Helvetica",22))
input_header.place(relx = 0.4 , rely = 0.012)

frame_labels_buttons = customtkinter.CTkFrame(master=root, width= 1860,height=50)
frame_labels_buttons.place(relx = 0.015, rely = 0.05)

allingbar_y = 0.2 # for buttons // 
# button sinus 
button_sinus = customtkinter.CTkButton(master=frame_labels_buttons, text = "sinus", command=select_sinus)
button_sinus.place(relx =0.10, rely =allingbar_y )
# button blok
button_blok = customtkinter.CTkButton(master=frame_labels_buttons, text = "blok", command=select_blok)
button_blok.place(relx = 0.22, rely = allingbar_y )
# button ramp 
button_ramp = customtkinter.CTkButton(master=frame_labels_buttons, text = "ramp", command=select_ramp)
button_ramp.place(relx = 0.35, rely = allingbar_y )
# button pulse 
button_pulse = customtkinter.CTkButton(master=frame_labels_buttons, text = "pulse", command=select_pulse)
button_pulse.place(relx = 0.47, rely = allingbar_y )
# button noise
button_noise = customtkinter.CTkButton(master=frame_labels_buttons, text = "noise", command=select_noise)
button_noise.place(relx = 0.60, rely = allingbar_y)
#button arb
button_arb = customtkinter.CTkButton(master=frame_labels_buttons, text = "arb", command=select_arb)
button_arb.place(relx = 0.72, rely = allingbar_y)
# sweep / eigen functie bepalen 
button_sweep = customtkinter.CTkButton(master=frame_labels_buttons, text = "sweep", command=select_sweep)
button_sweep.place(relx = 0.85, rely = allingbar_y)

# max x is now 0.50 !!!!!!!!!! 
# max y is now 0.02 !!!!!!!
# test y += 0.10 so 0.12??
alling_x_for_buttons = 0.1
alling_x_for_entries = 0.45

frame_labels_entries = customtkinter.CTkFrame(master=root, width= 510,height=510)
frame_labels_entries.place(relx = 0.5, rely = 0.4,anchor=CENTER)

# header for frame/ info to the user 

input_header = customtkinter.CTkLabel(frame_labels_entries,text="Hier kunt u de gewenste parameters invullen",font=("Helvetica",22))
input_header.place(relx = 0.10, rely = 0.008)


# invul informatie over de sinus format...
# frequency 
labelfrequenctie = customtkinter.CTkLabel(frame_labels_entries,text="Vul hier de Ferquentie in ")
labelfrequenctie.place(relx = alling_x_for_buttons, rely = 0.12)

entryfrequenctie = customtkinter.CTkEntry(frame_labels_entries)
entryfrequenctie.place(relx = alling_x_for_entries, rely = 0.12)

#amplitude 

labelamplitude = customtkinter.CTkLabel(frame_labels_entries,text="Vul hier de amplitude in ")
labelamplitude.place(relx = alling_x_for_buttons, rely = 0.20)

entryamplitude = customtkinter.CTkEntry(frame_labels_entries)
entryamplitude.place(relx = alling_x_for_entries, rely = 0.20)
# offset 
labeloffset = customtkinter.CTkLabel(frame_labels_entries,text="Vul hier de offset in ")
labeloffset.place(relx = alling_x_for_buttons, rely = 0.28)

entryoffset = customtkinter.CTkEntry(frame_labels_entries)
entryoffset.place(relx = alling_x_for_entries, rely = 0.28)

# phase 

labelphase = customtkinter.CTkLabel(frame_labels_entries,text="Vul hier de fase in ")
labelphase.place(relx = alling_x_for_buttons, rely = 0.36)

entryphase = customtkinter.CTkEntry(frame_labels_entries)
entryphase.place(relx = alling_x_for_entries, rely = 0.36)

# duty cycle 

labeldutycycle = customtkinter.CTkLabel(frame_labels_entries,text="vul hier de duty cycle in ")
labeldutycycle.place(relx = alling_x_for_buttons, rely = 0.44)

entrydutycycle = customtkinter.CTkEntry(frame_labels_entries)
entrydutycycle.place(relx = alling_x_for_entries, rely = 0.44)
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
root.mainloop()
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
