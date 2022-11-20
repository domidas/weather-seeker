#!/usr/bin/env python3

from .weather import WeatherSeeker

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
