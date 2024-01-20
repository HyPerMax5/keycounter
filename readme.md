# Keycounter!

Counts your keystrokes and exports them to a csv. The .pkl is a binary file  
to dump the dict to, faster than reparsing the csv.  
I also trust the binary file more than the csv.  

Regardless, binary file, no touchy.  
The csv has the data you want to work with.  

I made this because I wanted to see which keys I press most to design  
a split keyboard with a custom layout.  
I originally intended to include a visualization thing directly in here,  
played around with some heatmaps and decided it was too much of a pain.  
I'll be collecting data for about a month, then I'll visualize the data  
in libre office.

I doubt anyone but me will ever use this.  
But if you ever need a keylogger that would suck at being used for malicious  
purposes, then this is the one.  
Carefully crafted to be practically useless when trying to steal someone's  
data!

## Usage
Currently only works on windows due to the tray icon and admin check.  
It's recommended to have this start using the task scheduler.  

Anyhow, clone the repo, then:  
``pip install -r requirements.txt``  
After that you simply run the script.  
Close out of it by right clicking on the tray icon and selecting "Exit".

I doubt you could even achieve anything malicious with this, but technically  
this is still a keylogger, so don't do evil shit.  
Use this responsibly and only with mutual consent if you're involving another  
participant.

This tool was written to help design custom keyboards and layouts.


## License
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>