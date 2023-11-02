
#this script will look for devices that are connected with your pc.
import pyvisa
rm = pyvisa.ResourceManager()
print(rm.list_resources())
