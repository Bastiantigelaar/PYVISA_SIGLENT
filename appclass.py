#import tkinter
#import tkinter.messagebox
import customtkinter
#from functools import partial 
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

        self.tabview = customtkinter.CTkTabview(self, width=860) 
        self.tabview.grid(row=0, column=0, padx=(20, 0), pady=(40, 0), sticky="nsew")
        self.tabview.add("SINUS")
        self.tabview.add("BLOK")
        self.tabview.add("RAMP")
        self.tabview.add("PULSE")
        self.tabview.add("NOISE")
        self.tabview.add("AUTOMATED MODE")
    # set grid level for each tab view    
        self.tabview.tab("SINUS").grid_columnconfigure(0, weight=1) 
        self.tabview.tab("BLOK").grid_columnconfigure(0, weight=1)
        self.tabview.tab("RAMP").grid_columnconfigure(0, weight=1) 
        self.tabview.tab("PULSE").grid_columnconfigure(0, weight=1)
        self.tabview.tab("NOISE").grid_columnconfigure(0, weight=1) 
        self.tabview.tab("AUTOMATED MODE").grid_columnconfigure(0, weight=1)
        
    # setup the config modules 
        
        self.config_sinus()
        self.config_blok()
        self.config_ramp()
        self.config_noise()
        self.config_pulse()

    def get_values_sinus(self):
        try:
            amp = float(self.sentryamplitude.get())
            fre = float(self.sentryfrequenctie.get())
            phase = float(self.sentryphase.get())
            offset = float(self.sentryoffset.get())
            self.set_value_sinus(amp,fre,phase,offset)
            time.sleep(0.5)
            self.set_value_sinus(amp,fre,phase,offset)
            print("De waardes die zijn ingevuld zijn .. " , amp, " ", fre, " ", phase," " ,offset)
        except:
            print("error with reading values of enterd values of sinus")

    def get_values_blok(self):
        try:
            #amp = float(self.bentryamplitude.get())
            fre = float(self.bentryfrequenctie.get())
            phase = float(self.bentryphase.get())
            offset = float(self.bentryoffset.get())
            low = float(self.bentrylowlevel.get())
            high = float(self.bentryhighlevel.get())
            duty = float(self.bentrydutycycle.get())
            self.set_value_blok(fre,phase,offset,low,high,duty)
            time.sleep(0.5)
            self.set_value_blok(fre,phase,offset,low,high,duty)
            print("De waardes die zijn ingevuld zijn .. " ,  " ", fre, " ", phase," " ,offset, " ", duty, " ", low, " ", high)
        except:
            print("error with reading values of enterd values of blok")
    
    def get_values_ramp(self):
        try:
            fre = float(self.rentryfrequenctie.get())
            phase = float(self.rentryphase.get())
            offset = float(self.rentryoffset.get())
            low = float(self.rentrylowlevel.get())
            high = float(self.rentryhighlevel.get())
            sym = float(self.rentrysymmetry.get())
            self.set_value_ramp(fre,phase,offset,low,high,sym)
            print("de waardes zijn ", fre," ", offset," ",  high," ", low, " ", sym)
        except:
            print("error with reading values of enterd values of blok")

    def get_values_sweep(self):
      try:
          sweep_time = float(self.swentrytime.get())
          sweep_stop = float(self.swentrystop.get())
          sweep_start = float(self.swentrystart.get())
          print("the values of the sweep are " , sweep_time , " ", sweep_stop, " ", sweep_start)
          self.set_value_sweep(sweep_time,sweep_stop,sweep_start)
          time.sleep(0.5)
          self.set_value_sweep(sweep_time,sweep_stop,sweep_start)
      except:
          print("an error occured reading values of enterd values of sweep")
    def get_values_noise(self):
        try:
            stdev = float(self.nentrysd.get())
            mean = float(self.nentrymean.get())
            print("the value of the sweeps are : ", stdev, " " , mean)
            self.set_value_noise(stdev,mean)
        except:
            print("an error occured reading values of enterd values of noise")      
    def get_values_pulse(self):
         try: 
            fre = float(self.pentryfrequenctie.get())
            offset = float(self.pentryoffset.get())
            low = float(self.pentrylowlevel.get())
            high = float(self.pentryhighlevel.get())
            duty = float(self.pentrydutycycle.get())
            width  = float(self.pentrywidth.get())
            fall = float(self.pentryfall.get())
            print("this are the values of the pulse inserted signal " , fre, " " ,offset, " ",low," ",high," ", width, " ", fall)
            self.set_values_pulse(fre,offset,low,high,width,fall)

         except:
             print("an error occured reading values of enterd values of the pulse") 

    def set_value_sinus(self,amp,fre,phase,offset):
        try:
            print("de ontvange waardes zijn ....")
            print(amp,"\n",fre,"\n",phase,"\n",offset)

            functie_generator = self.config_functie_generator()
            print("dit is de waarde van de functie generator" , functie_generator)
            functie_generator.write('C1:BSWV WVTP,SINE')   
            functie_generator.write(f'C1:BSWV FRQ,{fre}')
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV AMP,{amp}')
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV OFST,{offset}')
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV PHSE,{phase}')
            time.sleep(0.2)
            functie_generator.write('C1:OUTP ON')

            
            print("De ingevulde waarde zijn ", "amp ", amp, " freq", fre)
        except:
            print("an error accured during set function of the function generator")
    def set_value_blok(self,fre,phase,offset,low,high,duty):
         try:   
            functie_generator = self.config_functie_generator()
            print("dit is de waarde van de functie generator" , functie_generator)
            amp = high - low
            functie_generator.write('C1:BSWV WVTP,SQUARE')
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV FRQ,{fre}')
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV HLEV,{high}')
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV LLEV,{low}') 
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV AMP,{amp}')
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV OFST,{offset}')
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV PHSE,{phase}')
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV DUTY,{duty}')
            time.sleep(0.2)
            functie_generator.write('C1:OUTP ON')
         except:
             print("the blok waveform could not be set properly")     
    def set_value_ramp(self,fre,phase,offset,low,high,sym ):
            functie_generator = self.config_functie_generator()
            print("dit is de waarde van de functie generator" , functie_generator)
            amp = high - low
            functie_generator.write('C1:BSWV WVTP,RAMP')
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV FRQ,{fre}')
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV HLEV,{high}')
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV LLEV,{low}') 
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV AMP,{amp}')
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV OFST,{offset}')
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV PHSE,{phase}')
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV SYM,{sym}') 
            time.sleep(0.2)
            functie_generator.write('C1:OUTP ON')

    def set_value_noise(self,stdev,mean):
           try:
               functie_generator = self.config_functie_generator()
               functie_generator.write('C1:BSWV WVTP,NOISE')
               time.sleep(0.2)
               functie_generator.write(f'C1:BSWV STDEV,{stdev}')
               time.sleep(0.2)
               functie_generator.write(f'C1:BSWV MEAN,{mean}')
               time.sleep(0.2)
               functie_generator.write('C1:OUTP ON')
           except:
               print("an error occurred while setting up the noise signal...")
    def set_value_sweep(self,sweep_time,sweep_stop,sweep_start):
           try:
               functie_generator = self.config_functie_generator()
               functie_generator.write(f'C1:SWWV TIME,{sweep_time}')
               time.sleep(0.2) 
               functie_generator.write(f'C1:SWWV STOP,{sweep_stop}')
               time.sleep(0.2) 
               functie_generator.write(f'C1:SWWV START,{sweep_start}')  
               time.sleep(0.2)
               functie_generator.write('C1:SWWV STATE,ON')
               time.sleep(0.2)
               functie_generator.write('C1:OUTP ON')
               print("set is called")
           except:
               print("an error occured during set")
    def set_values_pulse(self,fre,offset,low,high,width,fall):
        try:   
            functie_generator = self.config_functie_generator()
            print("dit is de waarde van de functie generator" , functie_generator)
            amp = high - low
            functie_generator.write('C1:BSWV WVTP,PULSE')
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV FRQ,{fre}')
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV HLEV,{high}')
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV LLEV,{low}') 
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV AMP,{amp}')
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV OFST,{offset}')
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV WIDTH,{width}')
            time.sleep(0.2)
            functie_generator.write(f'C1:BSWV FALL,{fall}')
            time.sleep(0.2)
            functie_generator.write('C1:OUTP ON')
        except:
             print("the pulse waveform could not be set properly") 
    
       # setup the function generator
    def config_sinus(self):
    # CONFIGURATION OF THE SINUS SIGNAL 
     # sweep on or off 
        self.naam = customtkinter.StringVar(value="SINUS")
        self.switch_var1 = customtkinter.StringVar(value="off")
        self.switch1 = customtkinter.CTkSwitch(self.tabview.tab("SINUS"), text="sweep mode", command=self.sweep_on,
                                 variable=self.switch_var1, onvalue="on", offvalue="off")
        self.switch1.place(relx = 0, rely = 0)
     # default values 
        alling_x_for_buttons = 0.1
        alling_x_for_entries = 0.28
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
     # sweep on or off 
        self.naam = customtkinter.StringVar(value="BLOK")
        self.switch_var2 = customtkinter.StringVar(value="off")
        self.switch2 = customtkinter.CTkSwitch(self.tabview.tab("BLOK"), text="sweep mode", command=self.sweep_on,
                                 variable=self.switch_var2, onvalue="on", offvalue="off")
        self.switch2.place(relx = 0, rely = 0)
     # default values 
        alling_x_for_buttons = 0.1
        alling_x_for_entries = 0.28
     # frequency
        self.labelfrequenctie = customtkinter.CTkLabel(self.tabview.tab("BLOK"),text="Vul hier de Ferquentie in ")
        self.labelfrequenctie.place(relx = alling_x_for_buttons, rely = 0.12)

        self.bentryfrequenctie = customtkinter.CTkEntry(self.tabview.tab("BLOK"))
        self.bentryfrequenctie.place(relx = alling_x_for_entries, rely = 0.12)

     # amplitude 

    #    self.labelamplitude = customtkinter.CTkLabel(self.tabview.tab("BLOK"),text="Vul hier de amplitude in ")
     #   self.labelamplitude.place(relx = alling_x_for_buttons, rely = 0.20)

      #  self.bentryamplitude = customtkinter.CTkEntry(self.tabview.tab("BLOK"))
       # self.bentryamplitude.place(relx = alling_x_for_entries, rely = 0.20)
     # high level
        self.labelhighlevel = customtkinter.CTkLabel(self.tabview.tab("BLOK"),text="Vul hier de high level in ")
        self.labelhighlevel.place(relx = alling_x_for_buttons, rely = 0.20)

        self.bentryhighlevel = customtkinter.CTkEntry(self.tabview.tab("BLOK"))
        self.bentryhighlevel.place(relx = alling_x_for_entries, rely = 0.20)

     # low level
        self.labellowlevel = customtkinter.CTkLabel(self.tabview.tab("BLOK"),text="Vul hier de low level in ")
        self.labellowlevel.place(relx = alling_x_for_buttons, rely = 0.28)

        self.bentrylowlevel = customtkinter.CTkEntry(self.tabview.tab("BLOK"))
        self.bentrylowlevel.place(relx = alling_x_for_entries, rely = 0.28)
     
     # offset 
        self.labeloffset = customtkinter.CTkLabel(self.tabview.tab("BLOK"),text="Vul hier de offset in ")
        self.labeloffset.place(relx = alling_x_for_buttons, rely = 0.36)

        self.bentryoffset = customtkinter.CTkEntry(self.tabview.tab("BLOK"))
        self.bentryoffset.place(relx = alling_x_for_entries, rely = 0.36)

     # phase 

        self.labelphase = customtkinter.CTkLabel(self.tabview.tab("BLOK"),text="Vul hier de fase in ")
        self.labelphase.place(relx = alling_x_for_buttons, rely = 0.44)

        self.bentryphase = customtkinter.CTkEntry(self.tabview.tab("BLOK"))
        self.bentryphase.place(relx = alling_x_for_entries, rely = 0.44)
     # duty cycle

        self.labeldutycycle = customtkinter.CTkLabel(self.tabview.tab("BLOK"),text="Vul hier de duty cycle in")
        self.labeldutycycle.place(relx = alling_x_for_buttons, rely = 0.52)

        self.bentrydutycycle = customtkinter.CTkEntry(self.tabview.tab("BLOK"))
        self.bentrydutycycle.place(relx = alling_x_for_entries, rely = 0.52)
        
     # accept changes 

        self.checkbutton = customtkinter.CTkButton(self.tabview.tab("BLOK"), text = "Check", command = self.get_values_blok)
        self.checkbutton.place(relx = alling_x_for_entries, rely = 0.60)

    def config_ramp(self):
   # CONFIGURATION OF THE RAMP SIGNAL 
     # sweep on or off 
        self.naam = customtkinter.StringVar(value="off")
        self.switch_var3 = customtkinter.StringVar(value="off")
        self.switch3 = customtkinter.CTkSwitch(self.tabview.tab("RAMP"), text="sweep mode", command=self.sweep_on,
                                 variable=self.switch_var3, onvalue="on", offvalue="off")
        self.switch3.place(relx = 0, rely = 0)
     # default values 
        alling_x_for_buttons = 0.1
        alling_x_for_entries = 0.28
     # frequency
        self.labelfrequenctie = customtkinter.CTkLabel(self.tabview.tab("RAMP"),text="Vul hier de Ferquentie in ")
        self.labelfrequenctie.place(relx = alling_x_for_buttons, rely = 0.12)

        self.rentryfrequenctie = customtkinter.CTkEntry(self.tabview.tab("RAMP"))
        self.rentryfrequenctie.place(relx = alling_x_for_entries, rely = 0.12)
     # high level
        self.labelhighlevel = customtkinter.CTkLabel(self.tabview.tab("RAMP"),text="Vul hier de high level in ")
        self.labelhighlevel.place(relx = alling_x_for_buttons, rely = 0.20)

        self.rentryhighlevel = customtkinter.CTkEntry(self.tabview.tab("RAMP"))
        self.rentryhighlevel.place(relx = alling_x_for_entries, rely = 0.20)

     # low level
        self.labellowlevel = customtkinter.CTkLabel(self.tabview.tab("RAMP"),text="Vul hier de low level in ")
        self.labellowlevel.place(relx = alling_x_for_buttons, rely = 0.28)

        self.rentrylowlevel = customtkinter.CTkEntry(self.tabview.tab("RAMP"))
        self.rentrylowlevel.place(relx = alling_x_for_entries, rely = 0.28)
     
     # offset 
        self.labeloffset = customtkinter.CTkLabel(self.tabview.tab("RAMP"),text="Vul hier de offset in ")
        self.labeloffset.place(relx = alling_x_for_buttons, rely = 0.36)

        self.rentryoffset = customtkinter.CTkEntry(self.tabview.tab("RAMP"))
        self.rentryoffset.place(relx = alling_x_for_entries, rely = 0.36)

     # phase 

        self.labelphase = customtkinter.CTkLabel(self.tabview.tab("RAMP"),text="Vul hier de fase in ")
        self.labelphase.place(relx = alling_x_for_buttons, rely = 0.44)

        self.rentryphase = customtkinter.CTkEntry(self.tabview.tab("RAMP"))
        self.rentryphase.place(relx = alling_x_for_entries, rely = 0.44)
     # duty cycle

        self.labelsymmetry = customtkinter.CTkLabel(self.tabview.tab("RAMP"),text="Vul hier de symmerty in")
        self.labelsymmetry.place(relx = alling_x_for_buttons, rely = 0.52)

        self.rentrysymmetry = customtkinter.CTkEntry(self.tabview.tab("RAMP"))
        self.rentrysymmetry.place(relx = alling_x_for_entries, rely = 0.52)
        
     # accept changes 

        self.checkbutton = customtkinter.CTkButton(self.tabview.tab("RAMP"), text = "Check", command = self.get_values_ramp)
        self.checkbutton.place(relx = alling_x_for_entries, rely = 0.60)
    def config_noise(self):
   # CONFIGURATION OF THE NOISE SIGNAL 
     # default values 
        alling_x_for_buttons = 0.1
        alling_x_for_entries = 0.28
     # standaard deviation 
        self.labelsd = customtkinter.CTkLabel(self.tabview.tab("NOISE"),text="Vul hier de STdev in ")
        self.labelsd.place(relx = alling_x_for_buttons, rely = 0.12)

        self.nentrysd = customtkinter.CTkEntry(self.tabview.tab("NOISE"))
        self.nentrysd .place(relx = alling_x_for_entries, rely = 0.12)
     # mean 
        self.labelmean = customtkinter.CTkLabel(self.tabview.tab("NOISE"),text="Vul hier de mean in ")
        self.labelmean.place(relx = alling_x_for_buttons, rely = 0.20)

        self.nentrymean  = customtkinter.CTkEntry(self.tabview.tab("NOISE"))
        self.nentrymean.place(relx = alling_x_for_entries, rely = 0.20)
     # check box 
        self.checkbutton = customtkinter.CTkButton(self.tabview.tab("NOISE"), text = "Check", command = self.get_values_noise)
        self.checkbutton.place(relx = alling_x_for_entries, rely = 0.28) 
    def config_pulse(self):
      # CONFIGURATION OF THE PULSE SIGNAL 
     # default values 
        alling_x_for_buttons = 0.1
        alling_x_for_entries = 0.28
     # frequency
        self.labelfrequenctie = customtkinter.CTkLabel(self.tabview.tab("PULSE"),text="Vul hier de Ferquentie in ")
        self.labelfrequenctie.place(relx = alling_x_for_buttons, rely = 0.12)

        self.pentryfrequenctie = customtkinter.CTkEntry(self.tabview.tab("PULSE"))
        self.pentryfrequenctie.place(relx = alling_x_for_entries, rely = 0.12)

     # amplitude 

    #    self.labelamplitude = customtkinter.CTkLabel(self.tabview.tab("BLOK"),text="Vul hier de amplitude in ")
     #   self.labelamplitude.place(relx = alling_x_for_buttons, rely = 0.20)

      #  self.bentryamplitude = customtkinter.CTkEntry(self.tabview.tab("BLOK"))
       # self.bentryamplitude.place(relx = alling_x_for_entries, rely = 0.20)
     # high level
        self.labelhighlevel = customtkinter.CTkLabel(self.tabview.tab("PULSE"),text="Vul hier de high level in ")
        self.labelhighlevel.place(relx = alling_x_for_buttons, rely = 0.20)

        self.pentryhighlevel = customtkinter.CTkEntry(self.tabview.tab("PULSE"))
        self.pentryhighlevel.place(relx = alling_x_for_entries, rely = 0.20)

     # low level
        self.labellowlevel = customtkinter.CTkLabel(self.tabview.tab("PULSE"),text="Vul hier de low level in ")
        self.labellowlevel.place(relx = alling_x_for_buttons, rely = 0.28)

        self.pentrylowlevel = customtkinter.CTkEntry(self.tabview.tab("PULSE"))
        self.pentrylowlevel.place(relx = alling_x_for_entries, rely = 0.28)
     
     # offset 
        self.labeloffset = customtkinter.CTkLabel(self.tabview.tab("PULSE"),text="Vul hier de offset in ")
        self.labeloffset.place(relx = alling_x_for_buttons, rely = 0.36)

        self.pentryoffset = customtkinter.CTkEntry(self.tabview.tab("PULSE"))
        self.pentryoffset.place(relx = alling_x_for_entries, rely = 0.36)
     # duty cycle

        self.labeldutycycle = customtkinter.CTkLabel(self.tabview.tab("PULSE"),text="Vul hier de duty cycle in ")
        self.labeldutycycle.place(relx = alling_x_for_buttons, rely = 0.44)

        self.pentrydutycycle = customtkinter.CTkEntry(self.tabview.tab("PULSE"))
        self.pentrydutycycle.place(relx = alling_x_for_entries, rely = 0.44)
     
     # pulse width
        self.labelwidth = customtkinter.CTkLabel(self.tabview.tab("PULSE"),text="Vul hier de pulsewidth in ")
        self.labelwidth.place(relx = alling_x_for_buttons, rely = 0.52)

        self.pentrywidth = customtkinter.CTkEntry(self.tabview.tab("PULSE"))
        self.pentrywidth.place(relx = alling_x_for_entries, rely = 0.52)  
     # pulse fall 
        self.labelfall = customtkinter.CTkLabel(self.tabview.tab("PULSE"),text="Vul hier de fall time in")
        self.labelfall.place(relx = alling_x_for_buttons, rely = 0.60)

        self.pentryfall = customtkinter.CTkEntry(self.tabview.tab("PULSE"))
        self.pentryfall.place(relx = alling_x_for_entries, rely = 0.60)

        
     # accept changes 

        self.checkbutton = customtkinter.CTkButton(self.tabview.tab("PULSE"), text = "Check", command = self.get_values_pulse)
        self.checkbutton.place(relx = alling_x_for_entries, rely = 0.68)





    def config_functie_generator(self):
          try:
            
            rm = pyvisa.ResourceManager() 
            functie_generator = rm.open_resource('USB0::0xF4ED::0xEE3A::SDG08CBC7R0184::0::INSTR') 
            return functie_generator
          except:
            print("functie_generator not found -> error try check_connection.py or search_connection.py on the github page")

    def sweep_on(self):
        print("switch1 was toggled: ", self.switch_var1.get())
        print("switch2 was toggled: ", self.switch_var2.get())
        print("switch3 was toggled: ", self.switch_var3.get())
        print("the current tab" , self.tabview.get())
        name = self.tabview.get()
        print(" dit is switcgh 1 ", self.switch_var1.get())
        print(" dit is switcgh 2 ", self.switch_var2.get())
        
        match name:
               case "SINUS":
                   #self.switch_var1.get()
                   #self.switch_var2 = customtkinter.StringVar(value="off")
                   #self.switch_var3 = customtkinter.StringVar(value="off")
                   self.configure_sweep_sinus()
               case "BLOK":
                   #self.switch_var1 = customtkinter.StringVar(value="off")
                   #self.switch_var3 = customtkinter.StringVar(value="off")
                   #print("swutcg2 ", self.switch_var2.get())
                   self.configure_sweep_blok()
               case "RAMP":
                    #self.switch_var1 = customtkinter.StringVar(value="off")
                    #self.switch_var2 = customtkinter.StringVar(value="off")
                    self.configure_sweep_ramp()
               case _: 
                    print("invalid cases /// unknown")
        
        
    
    
    def configure_sweep_sinus(self):
            #print( "dit is de naam meegeven", naam)
            
            if self.switch_var1.get() == "on": 
               temp =  self.tabview.get()
               print("ik kom in de if")
               alling_x_for_buttons = 0.50
               alling_x_for_entries = 0.78
            # time value 
               self.labeltime = customtkinter.CTkLabel(self.tabview.tab(temp),text="Vul hier de tijd in")
               self.labeltime.place(relx = alling_x_for_buttons, rely = 0.12)

               self.swentrytime = customtkinter.CTkEntry(self.tabview.tab(temp))
               self.swentrytime.place(relx = alling_x_for_entries, rely = 0.12)

            # start frequency
               self.labelstart = customtkinter.CTkLabel(self.tabview.tab(temp),text="Vul hier de start frequentie in")
               self.labelstart.place(relx = alling_x_for_buttons, rely = 0.20)

               self.swentrystart = customtkinter.CTkEntry(self.tabview.tab(temp))
               self.swentrystart.place(relx = alling_x_for_entries, rely = 0.20)
            # stop frequency
               self.labelstop = customtkinter.CTkLabel(self.tabview.tab(temp),text="Vul hier de stop frequentie in")
               self.labelstop.place(relx = alling_x_for_buttons, rely = 0.28)

               self.swentrystop = customtkinter.CTkEntry(self.tabview.tab(temp))
               self.swentrystop.place(relx = alling_x_for_entries, rely = 0.28)

               self.checkbutton2 = customtkinter.CTkButton(self.tabview.tab(temp), text = "Check", command = self.get_values_sweep)
               self.checkbutton2.place(relx = alling_x_for_entries, rely = 0.54)     
            else: 
               print("ïk kom in de else ")
               self.labeltime.place_forget()
               self.swentrytime.place_forget()
               
               self.labelstop.place_forget()
               self.swentrystop.place_forget()
               
               self.labelstart.place_forget()
               self.swentrystart.place_forget()
               self.checkbutton2.place_forget()
    def configure_sweep_blok(self):
            #print( "dit is de naam meegeven", naam)
           
            if self.switch_var2.get() == "on": 
               temp =  self.tabview.get()
               print("ik kom in de if")
               alling_x_for_buttons = 0.50
               alling_x_for_entries = 0.78
            # time value 
               self.labeltime = customtkinter.CTkLabel(self.tabview.tab(temp),text="Vul hier de tijd in")
               self.labeltime.place(relx = alling_x_for_buttons, rely = 0.12)

               self.swentrytime = customtkinter.CTkEntry(self.tabview.tab(temp))
               self.swentrytime.place(relx = alling_x_for_entries, rely = 0.12)

            # start frequency
               self.labelstart = customtkinter.CTkLabel(self.tabview.tab(temp),text="Vul hier de start frequentie in")
               self.labelstart.place(relx = alling_x_for_buttons, rely = 0.20)

               self.swentrystart = customtkinter.CTkEntry(self.tabview.tab(temp))
               self.swentrystart.place(relx = alling_x_for_entries, rely = 0.20)
            # stop frequency
               self.labelstop = customtkinter.CTkLabel(self.tabview.tab(temp),text="Vul hier de stop frequentie in")
               self.labelstop.place(relx = alling_x_for_buttons, rely = 0.28)

               self.swentrystop = customtkinter.CTkEntry(self.tabview.tab(temp))
               self.swentrystop.place(relx = alling_x_for_entries, rely = 0.28)

               self.checkbutton2 = customtkinter.CTkButton(self.tabview.tab(temp), text = "Check", command = self.get_values_sweep)
               self.checkbutton2.place(relx = alling_x_for_entries, rely = 0.60)     
            else: 
               print("ïk kom in de else ")
               self.labeltime.place_forget()
               self.swentrytime.place_forget()
               
               self.labelstop.place_forget()
               self.swentrystop.place_forget()
               
               self.labelstart.place_forget()
               self.swentrystart.place_forget()
               self.checkbutton2.place_forget()
    def configure_sweep_ramp(self):
         #print( "dit is de naam meegeven", naam)
            print("====",self.switch_var3.get())
            if self.switch_var3.get() == "on": 
               temp =  self.tabview.get()
               print("ik kom in de if")
               alling_x_for_buttons = 0.50
               alling_x_for_entries = 0.78
            # time value 
               self.labeltime = customtkinter.CTkLabel(self.tabview.tab(temp),text="Vul hier de tijd in")
               self.labeltime.place(relx = alling_x_for_buttons, rely = 0.12)

               self.swentrytime = customtkinter.CTkEntry(self.tabview.tab(temp))
               self.swentrytime.place(relx = alling_x_for_entries, rely = 0.12)

            # start frequency
               self.labelstart = customtkinter.CTkLabel(self.tabview.tab(temp),text="Vul hier de start frequentie in")
               self.labelstart.place(relx = alling_x_for_buttons, rely = 0.20)

               self.swentrystart = customtkinter.CTkEntry(self.tabview.tab(temp))
               self.swentrystart.place(relx = alling_x_for_entries, rely = 0.20)
            # stop frequency
               self.labelstop = customtkinter.CTkLabel(self.tabview.tab(temp),text="Vul hier de stop frequentie in")
               self.labelstop.place(relx = alling_x_for_buttons, rely = 0.28)

               self.swentrystop = customtkinter.CTkEntry(self.tabview.tab(temp))
               self.swentrystop.place(relx = alling_x_for_entries, rely = 0.28)

               self.checkbutton2 = customtkinter.CTkButton(self.tabview.tab(temp), text = "Check", command = self.get_values_sweep)
               self.checkbutton2.place(relx = alling_x_for_entries, rely = 0.60)     
            else: 
               print("ïk kom in de else ")
               self.labeltime.place_forget()
               self.swentrytime.place_forget()
               
               self.labelstop.place_forget()
               self.swentrystop.place_forget()
               
               self.labelstart.place_forget()
               self.swentrystart.place_forget()
               self.checkbutton2.place_forget()
    
