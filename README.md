# Basic GUI with PYVISA for scope and function generator
made by: Bastian Tigelaar (student)
# The function generator GUI
![image](https://github.com/basktanios/PYVISA_SIGLENT/assets/108866346/6659647c-a9b3-4b3d-a9be-a50931a64af1)



# The scope GUI
## important:

- the main.py runs the gui-
- the magic is placed in appclass.py

# currently working on 
- automated mode
- better structure of code, (oop)
- when finished --> scope with automated mode...

# documentation
All customertkinter code comes from the documantation of the [github of TomSchimansky](https://github.com/TomSchimansky/CustomTkinter)
the programming guides:
## [programming guide siglent](https://siglentna.com/USA_website_2014/Documents/Program_Material/SDG_ProgrammingGuide_PG_E03B.pdf)
## [programming guide tektronix](https://www.tek.com/en/oscilloscope/tds1000-manual)

# supported devices:
## scopes:
TDS200,TDS1000, TDS2000, and TPS2000 Series Digital Oscilloscopes, (working on the hantek scope)
## function generators: 
all siglent generators
note:
not every function has been tested.

# installs that are needed 
Keep in mind that pip and python are needed before the install work.

## first install
first install:
```bash
pip install pyvisa
```
## second install
second install:
```bash
pip install numpy 
```
## third install
third install: 
```bash
pip install customertkinter 
```

