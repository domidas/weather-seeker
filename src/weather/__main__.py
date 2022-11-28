#!/usr/bin/env python3

from .weather import WeatherSeeker

def getKey():
    from os.path import exists
    import os
    import requests

    key_exists = exists("./.api_key")

    current_dir = os.getcwd()

    if key_exists == True:

        print(".api_key file found in " + current_dir)

        with open('.api_key','r') as key:
            api_key = key.read()

    else:

        api_key = input(
                        "\n"
                        "WARNING: No .api_key file found. Please enter API key now: "
                        )
        
        print("\n"
             "Saving key in " + current_dir + "/.api_key"
            )
        
        f = open(".api_key", "a")
        f.write(api_key)
        f.close()
    
    print("Checking if key is valid...")

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    check_url = base_url + "appid=" + api_key

    reply = requests.get(check_url)

    r = reply.json()

    if r["cod"] == "400":

        print("Server reply 400: Key is valid.")

    else:
        
        error_code = (str(r["cod"]))

        print("Server reply " + error_code + ". Key is invalid.")

def main():

    seeker = WeatherSeeker()
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Get API Key
    with open('.api_key','r') as key:
        api_key = key.read()

    defaultq = input("Are you requesting Athens, GA weather? [Y/N]: ")

    if defaultq == "Y":
        city_id = "4180386"
        complete_url = base_url + "appid=" + api_key + "&id=" + city_id
        seeker.data_fetch(complete_url)

    if defaultq == "N":
        locale = input("Are you requesting weather for a US state? [Y/N]: ")

        if locale == "Y":
            city_id = input("Enter city name: ")
            state_id = input("Enter state postal code: ")
            country_id = "USA"
            complete_url = base_url + "appid=" + api_key + "&q=" + city_id + ",US-" + state_id + "," + country_id
            seeker.data_fetch(complete_url)

        if locale == "N":
            city_id = input("Enter city name: ")
            country_name = input("Enter country name: ")
            code_fetch(country_name)
            complete_url = base_url + "appid=" + api_key + "&q=" + city_id + "," + country_id
            seeker.data_fetch(complete_url)