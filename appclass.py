import tkinter
import tkinter.messagebox
import customtkinter
import pyvisa
import time 

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__() 
     # configure window
       
        self.title("GUI for function generator and scope")
        self.geometry(f"{1920}x{1080}")
     
     # configure grid in total 

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
     
     # create tabview

        self.tabview = customtkinter.CTkTabview(self, width=760) 
        self.tabview.grid(row=0, column=0, padx=(20, 0), pady=(40, 0), sticky="nsew")
        self.tabview.add("SINUS")
        self.tabview.add("BLOK")
        self.tabview.add("RAMP")
        self.tabview.add("PULSE")
        self.tabview.add("NOISE")
        self.tabview.add("ARB")
        self.tabview.add("SWEEP MODE")
        self.tabview.add("AUTOMATED MODE")
          
    # set grid level for each tab view    

        self.tabview.tab("SINUS").grid_columnconfigure(0, weight=1) 
        self.tabview.tab("BLOK").grid_columnconfigure(0, weight=1)
        self.tabview.tab("RAMP").grid_columnconfigure(0, weight=1) 
        self.tabview.tab("PULSE").grid_columnconfigure(0, weight=1)
        self.tabview.tab("NOISE").grid_columnconfigure(0, weight=1) 
        self.tabview.tab("ARB").grid_columnconfigure(0, weight=1)
        self.tabview.tab("NOISE").grid_columnconfigure(0, weight=1) 
        self.tabview.tab("ARB").grid_columnconfigure(0, weight=1)
        self.tabview.tab("SWEEP MODE").grid_columnconfigure(0, weight=1) 
        self.tabview.tab("AUTOMATED MODE").grid_columnconfigure(0, weight=1)
        
    # setup the config modules 
        
        self.config_sinus()
        self.config_blok()
        self.config_ramp()




    def get_values_sinus(self):
        try:
            amp = float(self.sentryamplitude.get())
            fre = float(self.sentryfrequenctie.get())
            phase = float(self.sentryphase.get())
            offset = float(self.sentryoffset.get())
            self.set_value_sinus(amp,fre,phase,offset)
            print("De waardes die zijn ingevuld zijn .. " , amp, " ", fre, " ", phase," " ,offset)
        except:
            print("error with reading values of enterd values of sinus")

    def get_values_blok(self):
        try:
            amp = float(self.bentryamplitude.get())
            fre = float(self.bentryfrequenctie.get())
            phase = float(self.bentryphase.get())
            offset = float(self.bentryoffset.get())
            low = float(self.bentrylowlevel.get())
            high = float(self.bentryhighlevel.get())
            duty = float(self.bentrydutycycle.get())
            print("De waardes die zijn ingevuld zijn .. " , amp, " ", fre, " ", phase," " ,offset, " ", duty, " ", low, " ", high)
        except:
            print("error with reading values of enterd values of blok")
    
    def get_values_ramp(self):
        try:
            amp = float(self.rentryamplitude.get())
            fre = float(self.rentryfrequenctie.get())
            phase = float(self.rentryphase.get())
            offset = float(self.rentryoffset.get())
            print("De waardes die zijn ingevuld zijn .. " , amp, " ", fre, " ", phase," " ,offset)
        except:
            print("error with reading values of enterd values of blok")
    def set_value_sinus(self,amp,fre,phase,offset):
        try:
            print("de ontvange waardes zijn ....")
            print(amp,"\n",fre,"\n",phase,"\n",offset)

            functie_generator = self.config_functie_generator()
            print("dit is de waarde van de functie generator" , functie_generator)
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
               print("kies een frequency lager of gelijk aan 10Mhz")
            
            functie_generator.write('C1:BSWV WVTP,SINE')   
            functie_generator.write(f'C1:BSWV FRQ,{fre}')
            functie_generator.write(f'C1:BSWV AMP,{amp}')
            functie_generator.write(f'C1:BSWV OFST,{offset}')
            functie_generator.write(f'C1:BSWV PHSE,{phase}')
            print("De ingevulde waarde zijn ", "amp ", amp, " freq", fre)
        except:
            print("an error accured during set function of the function generator")
       # setup the function generator
    def config_sinus(self):
    # CONFIGURATION OF THE SINUS SIGNAL 
     # default values 
        alling_x_for_buttons = 0.1
        alling_x_for_entries = 0.45
     # frequency
        self.labelfrequenctie = customtkinter.CTkLabel(self.tabview.tab("SINUS"),text="Vul hier de Ferquentie in ")
        self.labelfrequenctie.place(relx = alling_x_for_buttons, rely = 0.12)

        self.sentryfrequenctie = customtkinter.CTkEntry(self.tabview.tab("SINUS"))
        self.sentryfrequenctie.place(relx = alling_x_for_entries, rely = 0.12)

     # amplitude 

        self.labelamplitude = customtkinter.CTkLabel(self.tabview.tab("SINUS"),text="Vul hier de amplitude in ")
        self.labelamplitude.place(relx = alling_x_for_buttons, rely = 0.20)

        self.sentryamplitude = customtkinter.CTkEntry(self.tabview.tab("SINUS"))
        self.sentryamplitude.place(relx = alling_x_for_entries, rely = 0.20)
     # offset 
        self.labeloffset = customtkinter.CTkLabel(self.tabview.tab("SINUS"),text="Vul hier de offset in ")
        self.labeloffset.place(relx = alling_x_for_buttons, rely = 0.28)

        self.sentryoffset = customtkinter.CTkEntry(self.tabview.tab("SINUS"))
        self.sentryoffset.place(relx = alling_x_for_entries, rely = 0.28)

     # phase 

        self.labelphase = customtkinter.CTkLabel(self.tabview.tab("SINUS"),text="Vul hier de fase in ")
        self.labelphase.place(relx = alling_x_for_buttons, rely = 0.36)

        self.sentryphase = customtkinter.CTkEntry(self.tabview.tab("SINUS"))
        self.sentryphase.place(relx = alling_x_for_entries, rely = 0.36)
        
     # accept changes 

        self.checkbutton = customtkinter.CTkButton(self.tabview.tab("SINUS"), text = "Check", command = self.get_values_sinus)
        self.checkbutton.place(relx = alling_x_for_entries, rely = 0.54)

    def config_blok(self):
    # CONFIGURATION OF THE BLOK SIGNAL 
     # default values 
        alling_x_for_buttons = 0.1
        alling_x_for_entries = 0.45
     # frequency
        self.labelfrequenctie = customtkinter.CTkLabel(self.tabview.tab("BLOK"),text="Vul hier de Ferquentie in ")
        self.labelfrequenctie.place(relx = alling_x_for_buttons, rely = 0.12)

        self.bentryfrequenctie = customtkinter.CTkEntry(self.tabview.tab("BLOK"))
        self.bentryfrequenctie.place(relx = alling_x_for_entries, rely = 0.12)

     # amplitude 

        self.labelamplitude = customtkinter.CTkLabel(self.tabview.tab("BLOK"),text="Vul hier de amplitude in ")
        self.labelamplitude.place(relx = alling_x_for_buttons, rely = 0.20)

        self.bentryamplitude = customtkinter.CTkEntry(self.tabview.tab("BLOK"))
        self.bentryamplitude.place(relx = alling_x_for_entries, rely = 0.20)
     # high level
        self.labelhighlevel = customtkinter.CTkLabel(self.tabview.tab("BLOK"),text="Vul hier de high level in ")
        self.labelhighlevel.place(relx = alling_x_for_buttons, rely = 0.28)

        self.bentryhighlevel = customtkinter.CTkEntry(self.tabview.tab("BLOK"))
        self.bentryhighlevel.place(relx = alling_x_for_entries, rely = 0.28)

     # low level
        self.labellowlevel = customtkinter.CTkLabel(self.tabview.tab("BLOK"),text="Vul hier de low level in ")
        self.labellowlevel.place(relx = alling_x_for_buttons, rely = 0.36)

        self.bentrylowlevel = customtkinter.CTkEntry(self.tabview.tab("BLOK"))
        self.bentrylowlevel.place(relx = alling_x_for_entries, rely = 0.36)
     
     # offset 
        self.labeloffset = customtkinter.CTkLabel(self.tabview.tab("BLOK"),text="Vul hier de offset in ")
        self.labeloffset.place(relx = alling_x_for_buttons, rely = 0.44)

        self.bentryoffset = customtkinter.CTkEntry(self.tabview.tab("BLOK"))
        self.bentryoffset.place(relx = alling_x_for_entries, rely = 0.44)

     # phase 

        self.labelphase = customtkinter.CTkLabel(self.tabview.tab("BLOK"),text="Vul hier de fase in ")
        self.labelphase.place(relx = alling_x_for_buttons, rely = 0.52)

        self.bentryphase = customtkinter.CTkEntry(self.tabview.tab("BLOK"))
        self.bentryphase.place(relx = alling_x_for_entries, rely = 0.52)
     # duty cycle

        self.labeldutycycle = customtkinter.CTkLabel(self.tabview.tab("BLOK"),text="Vul hier de duty cycle in")
        self.labeldutycycle.place(relx = alling_x_for_buttons, rely = 0.60)

        self.bentrydutycycle = customtkinter.CTkEntry(self.tabview.tab("BLOK"))
        self.bentrydutycycle.place(relx = alling_x_for_entries, rely = 0.60)
        
     # accept changes 

        self.checkbutton = customtkinter.CTkButton(self.tabview.tab("BLOK"), text = "Check", command = self.get_values_blok)
        self.checkbutton.place(relx = alling_x_for_entries, rely = 0.68)

    def config_ramp(self):
    # CONFIGURATION OF THE RAMP 
       # default values 
        alling_x_for_buttons = 0.1
        alling_x_for_entries = 0.45
       # frequency
        self.labelfrequenctie = customtkinter.CTkLabel(self.tabview.tab("RAMP"),text="Vul hier de Ferquentie in ")
        self.labelfrequenctie.place(relx = alling_x_for_buttons, rely = 0.12)

        self.rentryfrequenctie = customtkinter.CTkEntry(self.tabview.tab("RAMP"))
        self.rentryfrequenctie.place(relx = alling_x_for_entries, rely = 0.12)

     # amplitude 

        self.labelamplitude = customtkinter.CTkLabel(self.tabview.tab("RAMP"),text="Vul hier de amplitude in ")
        self.labelamplitude.place(relx = alling_x_for_buttons, rely = 0.20)

        self.rentryamplitude = customtkinter.CTkEntry(self.tabview.tab("RAMP"))
        self.rentryamplitude.place(relx = alling_x_for_entries, rely = 0.20)
     # offset 
        self.labeloffset = customtkinter.CTkLabel(self.tabview.tab("RAMP"),text="Vul hier de offset in ")
        self.labeloffset.place(relx = alling_x_for_buttons, rely = 0.28)

        self.rentryoffset = customtkinter.CTkEntry(self.tabview.tab("RAMP"))
        self.rentryoffset.place(relx = alling_x_for_entries, rely = 0.28)

     # phase 

        self.labelphase = customtkinter.CTkLabel(self.tabview.tab("RAMP"),text="Vul hier de fase in ")
        self.labelphase.place(relx = alling_x_for_buttons, rely = 0.36)

        self.rentryphase = customtkinter.CTkEntry(self.tabview.tab("RAMP"))
        self.rentryphase.place(relx = alling_x_for_entries, rely = 0.36)
        
     # accept changes 

        self.checkbutton = customtkinter.CTkButton(self.tabview.tab("RAMP"), text = "Check", command = self.get_values_ramp)
        self.checkbutton.place(relx = alling_x_for_entries, rely = 0.54)
    def config_functie_generator(self):
          try:
            rm = pyvisa.ResourceManager() 
            functie_generator = rm.open_resource('USB0::0xF4ED::0xEE3A::SDG08CBC7R0184::0::INSTR') 
            return functie_generator
          except:
            print("functie_generator not found -> error try check_connection.py or search_connection.py on the github page")
