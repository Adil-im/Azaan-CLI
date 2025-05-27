import requests
import datetime
import pytz

# Create a variable to store the base url of the API 
base_url = "https://api.aladhan.com/v1"

#fetch the current date and time from the system and format it to fit the API formats
x = datetime.datetime.now()



'''
TODO; 
- Make it international, so that people can just enter the name of their country 
and (or) the Method(calculation method but just the country is enough since it defaults to the nearest closest
authority based on the location, still give users the option to change the Method MAXIMUM FREEDOM!)
- implement Code to get the local timezone of the user(using PYTZ library) and update it to the timezonestring variable. 
''' 

def get_adhan_timings():

    #Create a var url to store the API GET request link with base_url with all the required data.
    url = f"{base_url}/timingsByCity/{x}?city=chennai&country=India&timezonestring=Asia/Kolkata"
    global response
   
    #the get() method send a GET request to the specified URL.
    response = requests.get(url)

    if response.status_code == 200:
        adhan_data = response.json()
        return adhan_data
    else:
        print(f"failed to retrieve data {response.status_code}")


adhan =  get_adhan_timings()

# will get an error if you change Timezonestring to some other format. FOLLOW THE FORMAT BIG BOI!
print(adhan['data']['timings'])

cmd = str(input("Enter a Command: "))
Timings = adhan ['data']['timings']


if(cmd == "Fajr"):
    print("Fajr -", Timings["Fajr"])
elif(cmd == "Dhuhr"):
    print("Dhuhr -", Timings["Dhuhr"])
elif(cmd == "Asr"):
    print("Asr - ", Timings["Asr"])
elif(cmd == "Maghrib"):
    print("Maghrib -", Timings['Maghrib'])
elif(cmd == "Isha"):
    print("Isha - ", Timings['Isha'])
else:
    print("invalid Command")
    print("Available commands are:  Fajr, Dhuhr, Asr, Maghrib, Isha")











