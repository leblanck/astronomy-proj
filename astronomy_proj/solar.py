#!/usr/bin/env python3
"""
find the sun
"""

import datetime as dt
import requests
from requests.auth import HTTPBasicAuth
from astro_keys import ASTRONOMY_ID, ASTRONOMY_SECRET


def get_observer_location():
    """
    this will get loc
    """
    response = requests.get("http://ip-api.com/json/")
    data = response.json()

    lat = data["lat"]
    lon = data["lon"]
    city = data["city"]
    state = data["region"]

    local = f"From {city}, {state}:"

    return lat, lon, local


def get_sun_position(lat, lon):
    """
    get sun loc
    """
    date = dt.date.today()
    now = dt.datetime.now()
    time = now.strftime("%H:%M:%S")
    basic = HTTPBasicAuth(ASTRONOMY_ID, ASTRONOMY_SECRET)
    payload = {
        "latitude": lat,
        "longitude": lon,
        "elevation": "0",
        "from_date": date,
        "to_date": date,
        "time": time,
    }
    response = requests.get(
        "https://api.astronomyapi.com/api/v2/bodies/positions/sun",
        auth=basic,
        params=payload,
    )
    data = response.json()
    azi = data["data"]["table"]["rows"][0]["cells"][0]["position"]["horizontal"][
        "azimuth"
    ]["string"]

    alt = data["data"]["table"]["rows"][0]["cells"][0]["position"]["horizontal"][
        "altitude"
    ]["string"]

    return azi, alt


def print_position(azi, alt, loc):
    """
    print to console
    """
    print(
        f"{loc}\n The Sun is currently at: {azi} degress azimuth and {alt} degress altitude."
    )


if __name__ == "__main__":
    latitude, longitude, location = get_observer_location()
    azimuth, altitude = get_sun_position(latitude, longitude)
    print_position(azimuth, altitude, location)
