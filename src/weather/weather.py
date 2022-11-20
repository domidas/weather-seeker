import requests, json

class WeatherSeeker:

    def data_fetch(self, complete_url):
        response = requests.get(complete_url)
        x = response.json()

        if x["cod"] != "404":

            # define json coord key
            c = x["coord"]

            # pull coordinates
            longitude = c["lon"]
            latitude = c["lat"]

            # define json "main" key
            y = x["main"]

            # store the value corresponding
            # to the "temp" key of y
            current_temperature = y["temp"]

            # convert from K to F
            temp_fahrenheit = (((current_temperature - 273.15)*9)/5)+32

            # round to one decimal place
            temp_fahrenheit = str(round(temp_fahrenheit, 1))

            # store the value corresponding
            # to the "pressure" key of y
            current_pressure = y["pressure"]

            # store the value corresponding
            # to the "humidity" key of y
            current_humidity = y["humidity"]

            # store the value of "weather"
            # key in variable z
            z = x["weather"]

            # store the value corresponding
            # to the "description" key at
            # the 0th index of z
            weather_description = z[0]["description"]

            # print following values
            print(" longitude = " +
                            str(longitude) +
                "\n latitude = " +
                            str(latitude) +
                "\n temperature (in Fahreinheit) = " +
                            str(temp_fahrenheit) +
                "\n atmospheric pressure (in hPa unit) = " +
                            str(current_pressure) +
                "\n humidity = " +
                            str(current_humidity) + "%" +
                "\n description = " +
                            str(weather_description))
        else:
            print(" City Not Found ")

    def code_fetch(country_name):
        o = open('countrycodes.json')
        codes = json.load(o)
        print(list(codes.keys())[list(codes.values()).index(country_name)])
