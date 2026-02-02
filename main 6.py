#
import astropy.units as u
from astropy.coordinates import EarthLocation, SkyCoord, AltAz
from astropy.time import Time
import requests


def get_equatorial_coords():

    try:
        # Use ip-api.com (free, no API key required for low volume)
        response = requests.get("http://ip-api.com/json/")
        data = response.json()

        if data['status'] == 'success':
            lat = data['lat']
            lon = data['lon']
            city = data['city']
            region = data['regionName']

            # Create the Astropy EarthLocation object
            # Note: height is set to 0 as IP geo usually doesn't provide altitude
            location = EarthLocation(lat=lat * u.deg, lon=lon * u.deg, height=0 * u.m)
    finally:
            print(f"\nDetected Location: {city}, {region}")
            print(f"Coordinates: {lat}, {lon}")
            current_time = Time.now()
            print(f"System Time (UTC): {current_time}")
            print("-" * 27)
#  Request Target Input from User
    try:

        user_az = float(input("Enter azimuth 0.0 to 360.0: "))
        user_alt = float(input("Enter altitude 0.0 to 90.0: "))
        #user_az = 0.0
        #user_alt = 90.0
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return

    #  Create an AltAz frame for the specific time and location
    altaz_frame = AltAz(obstime=current_time, location=location)

    #  Define the target in the AltAz system

    target_altaz = SkyCoord(az=user_az * u.deg, alt=user_alt * u.deg, frame=altaz_frame)
    #  Transform to Equatorial Coordinates (CIRS/JNOW)
    target_icrs = target_altaz.transform_to('cirs')

    print(f"\n--- Results ---\n")
    print(f"Right Ascension (RA): {target_icrs.ra.to_string(unit=u.hour, sep='hms')}")
    print(f"Declination (Dec):    {target_icrs.dec.to_string(unit=u.deg, sep='dms')}")




if __name__ == "__main__":
    get_equatorial_coords()

