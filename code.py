import requests
# import time
from playsound import playsound
pin = 110051
date = '06-10-2021'
URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(
    pin, date)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}


def findAvailability():
    counter = 0
    result = requests.get(URL, headers=header)
    response_json = result.json()
    data = response_json["sessions"]
    for each in data:
        if((each["available_capacity_dose1"] > 0) & (each["min_age_limit"] >= 18) & (each["fee_type"] == "Free")):
            counter += 1
            print(each["name"])
            print(each["address"])
            print(each["pincode"])
            print(each["center_id"])
            print(each["vaccine"])
            print(each["fee_type"])
            print(each["available_capacity"])
            playsound('C:/Users/Avinash/PycharmProjects/pythontut1/ding-sound.mp3')
            return True
    if(counter == 0):
        print(f"No Available Slots --{i}")
        return False
i = 1
while(findAvailability() != True):
    # time.sleep(2)
    findAvailability()
    i = i + 1

