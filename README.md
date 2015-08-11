# Tactile_Reader
Python and arduino tactile output 

Basic premise is, I have an array of electric rotating mass motors connected to an arduino mega 2560. 
The array is strapped around a persons waist, so they can feel when different vibrating motors are activated.
When finished, the codecode read raw data or text, and translate this into patterns of vibrations that I'll send to the array.

I'm trying to make the code as reusable as possible, and friendly to adding new patterns for unrecognised characters,
modifying the timing and patterns, or redefining how some data should be sent.

To run, install pyserial, and use python 3 interpreter.
The arduino side code is included.

I chose python, because I'm learning python. 
