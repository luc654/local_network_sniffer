# local_network_sniffer
A small Raspberry PI program that uses nmap to detect devices on your local wifi. 


Requirements:
3 Jumper cables
2 resistors
2 LED's, red and green.

Wiring:
Stick both leds with their anodes (shorter side) on the same axis in the breadboard. Place them on the same axis so that you only need one ground cable.
Stick one of the jumper cables from a ground GPIO into the breadboard on the same axis as the anodes.

Place both resistors on the cathodes of both leds, make sure that the cathodes and resistors of both LED's ARENT on the same axis of the other.

Stick a jumper cable into GPIO 14 and wire it to the resistor that leads to the red LED.

Stick a jumper cable into GPIO 23 and wire it to the resistor that leads to the green LED.



Software:
Make sure NMAP is installed on your raspberry PI, if not, run 'sudo apt install nmap'
Download the main.py file.
Run it via 'python main.py'

The program will first log the IP and hostname of all connected devices, after that each disconnect of connect will be logged and a red / green led will be powered.
