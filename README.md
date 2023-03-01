# <p align="center">SoftwareMaterialSciences.py<p>

The files included within this repository is documentation of my time as a research intern for Texas A&M's material sciences department. 

Components that were connected to the computer were:

1. DAQ board (3-4 thermocouples)Thermocouples (input as voltage-mV)
2. Temperature display from omegaThermocouple (input) with a 4-20mA secondary output
connected to the generator (refer Creep-Fatigue documentation/Chapter 2/Instruction Manual-
page 36)
3. Hydraulic frame (already connected; will send you pdf of the documentation)
4. Extensometer (refer desktop: C:\\Program Files (x86)\MTS 793\Help in the 793 Tuning and
Calibration handbook)

Dataq’s proprietary software to read the values from a thermocouple is already installed and works as
expected. However, that gives us no flexibility and is rather cumbersome to log the temperatures
separate to the other values-namely force/stress applied by the hydraulic frame and the stain or
elongation of the stain gauge measured by the extensometer.

Within the Dataq software there was a way to get the temperature readings directly, but I was not sure if
they provide drivers that would enable us to directly read the temperature.


Putting it all together:
A. I had to figure out how to program either a Python program to read and store values from
the DAQ (temperature), Display (temperature), and the extensometer in a single file along with
the system time using the same program. The main challenge here would be the fact that they
all have different sampling rate that need to be accounted for/averaged to record at a set rate.
B. Incorporate the input from the load cell in the hydraulic frame (force readings) into the same
program.
C. Being able use the desktop to remotely program the generator to have certain temperature-
time values (aka ‘recipes’ in Fives Celes terminology) without using the touchscreen input of the
generator.
D. Being able to program stress-time or force-time inputs to the frame and logging the values
without using their proprietary software (refer to screenshot on drive titled MTS reply)

This way, the final program will be one where we can set the temperature and force values with respect
to time and have the all the pieces work cohesively to follow it.
