import pyvisa
import time
import numpy as np
# ================================================
def TIME_SCALE(x):
    arr = np.array([2e-9, 5e-9, 10e-9, 20e-9, 50e-9, 100e-9, 200e-9,500e-9,1e-6,2e-6,5e-6,10e-6,20e-6,50e-6,100e-6,200e-6,500e-6,1e-3,2e-3,5e-3,10e-3,20e-3,50e-3,100e-3,200e-3,500e-3,1,2,5,1020,50,100])
    difference_array = np.absolute(arr-x)
    index = difference_array.argmin()
    print("Nearest element to the given values is : ", arr[index])
    return (arr[index])

# =================================================
rm = pyvisa.ResourceManager() 
try:
    scope = rm.open_resource('USB0::0x049F::0x505E::CN2210029021121::INSTR') # chang to the current scope rm...
    time.sleep(0.2)
    functie_generator = rm.open_resource('USB0::0xF4ED::0xEE3A::SDG08CBC7R0184::0::INSTR') 
    time.sleep(0.2)
    print(scope.query('*IDN?'))
except:
    print("scope not found, checl rm.open_resource function or connection")
# ===================================================

list_frequency_gen = []
list_amplitude_gen = []

list_frequency_mes = []
list_amplitude_mes = []


# measurement turned on for CH1
scope.write("MEASure:ENABle ON")
scope.write("MEASure:SOURce CHANnel1")

# checken of measure mode enabeled ...
print("de Measure optie is enabled, status is " + scope.query(":MEASure:ENABle?"))

begin_frequency = 1
begin_amplitude = 2
test = 0.005
i = 0
scope.write(f"TIMebase:SCALe {test}")
# the scale values arry ..




# checken parameter of CH1, test with sin waveform...
while begin_frequency < 700:
    
    # write frequency and amplitude to function generator
    functie_generator.write(f'C1:BSWV FRQ,{begin_frequency}')
    functie_generator.write(f'C1:BSWV AMP,{begin_amplitude}')
    
    # get frequency and amplitude oof measured waveform
   
    fre = scope.query("MEASure:CHANnel1:ITEM? FREQuency")
    amp = scope.query("MEASure:CHANnel1:ITEM? VPP")
    print("Dit is de frequentie van de waveform " + fre)
    print("Dit is de VPP waarde " + amp)
   
    # to list 
    list_frequency_gen.append(begin_frequency)
    list_amplitude_gen.append(begin_amplitude)
    list_frequency_mes.append(float(fre))
    list_amplitude_mes.append(float(amp))

    
    begin_frequency = begin_frequency + 1
    test = TIME_SCALE((1/begin_frequency)/3)
    scope.write(f"TIMebase:SCALe {test}")


print(list_frequency_gen)
print(list_amplitude_gen)
print(list_frequency_mes)
print(list_amplitude_mes)



    # lets go to write it to a file







#print("Dit is de periode " + scope.query("MEASure:CHANnel1:ITEM? PERiod"))
    #print("Dit is de RMS waarde" + scope.query("MEASure:CHANnel1:ITEM? RMS"))
    
    
    #print("Dit is VAMP waarde" + scope.query("MEASure:CHANnel1:ITEM? VAMP"))
