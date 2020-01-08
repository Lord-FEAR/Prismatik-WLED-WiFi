# Prismatik WLED-WiFi plugin
Ambilight via WiFi. Prismatik plugin to support WLED

## Dependencies
* [WLED](https://github.com/Aircoookie/WLED/releases/tag/v0.8.6 "WLED") for ESP8266/ESP32 (checked for 0.8.6)
* [Python 3.7](https://www.python.org/downloads/ "Python 3.7")
* [Prismatik](https://github.com/psieg/Lightpack/releases "Prismatik") (tested on 5.11.2.19)
* [py-lightpack](https://github.com/tremby/py-lightpack "py-lightpack")  
For py-lightpack you need to install the future and boltons  
`pip install future`  
`pip install boltons`


## Installation

Install Python 3.7  
In Prismatik:
- Enable the API
- Enable Expert mode under Profiles
- Check Enable server under Experimental

Download the ZIP from the repository. 
Place the unzipped folder in the Prismatik plugins directory (e.g. C:\Users\LordF\Prismatik\Plugins\WLED-WiFi)  
Adjust settings in the WLED-WiFi.ini file  
Refresh the plugin list in Prismatik  

## Configuration Settings are configured in the WLED-WiFi.ini file.

- Main
	- Execute -  path to python.exe or python exe from system path
- WLED
	- UDP_IP_ADDRESS - Exact ip or x.x.x.255 for broadband (convenient with dynamic ip on the device)
	- UDP_PORT_NO - Port on the WLED device (default 21324) Settings -> Sync Interfaces -> UDP Port
	- FPS - Frames per second
