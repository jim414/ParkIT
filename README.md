ParkIt is a Python script for parking a telescope to a know azimuth and altitude. This can be used to part the telescope in a vertical position for taking flats or a horizontal position for storage in an observatory shelter or any other position desired as long as the coordinates are not below the horizon. It does this by converting the horizontal coordinates, azimuth and altitude to JNOW equatorial coordinates, RA and DEC, that can be entered into your mount control software such as the ASIAIR. The script should be capable of being run on both Windows and Mac systems that host Python. It has also been tested with the Juno Python app on iOs successfully although the set up is a bit more complicated. It may work on Android devices that have a Python environment that allows the adding of packages.

There are a few simple requirements to use the script

1. You need a PC or Mac with python installed on it. 
2. Your PC or Mac needs to be connected to the internet as the script uses your ip address to find your location.
3. An ASIAIR is the recommended device for entering the generate RA and DEC coordinates but any control software capable of issuing a GOTO using user entered coordinates should work.

Procedure for running the script for ASIAIR.

1. Be sure your scope is in the home position
1. Connect to the ASIAIR
3. Select the preview mode on the ASIAIR
4. Run the script in your python environment
5. On the ASIAIR tap the coordinates frame on the GOTO widget
6. Enter the RA and DEC shown in the scripts results
7. Execute the GOTO

Notes: 

1. The GOTO should be executed as quickly as possible as the coordinates are always changing.
2. You cannot reuse the generated coordinates as they are tied to a specific date/time and your location.
3. The generated coordinates have more accuracy than can be entered into the ASIAIR. This may become noticeable when the altitude is set at zero resulting in a message that the object is below the horizon. The solution is in those rare instances to set the altitude to 1.

Python Packages Required:

1. astropy
2. astropy-iers-data
3. requests
