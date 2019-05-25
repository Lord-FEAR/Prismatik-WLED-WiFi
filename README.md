# Prismatik WLED-WiFi plugin
Adds WARLS protocol for WLED

## Dependencies
* [Python 3.7](https://www.python.org/downloads/ "Python 3.7")
* [Prismatik](https://github.com/psieg/Lightpack/releases "Prismatik") (tested on 5.11.2.19)
* [py-lightpack](https://github.com/tremby/py-lightpack "py-lightpack")

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
	- These are used by Prismatik to identify the plugin
	- Execute -  path to python.exe or python exe from system path
- WLED
	- FPS - frames per second
