# import phonenumbers module
import phonenumbers as ph
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

number = 0
country = ""

while not len(country):
    number = input("Input the number: ")
    if number[0] != '+' or len(number) < 4 or len(number) > 15:
        print("Please input a valid Phone Number!")
        continue;
    number = ph.parse(number)
    country = geocoder.description_for_number(number, "en")

sim_card_provider = carrier.name_for_number(number, "en")
time_zone = timezone.time_zones_for_number(number)

print("\n")

print(number)
print(f"Country: {country}")
print(f"Sim Card Provider: {sim_card_provider}")
print(f"Time Zone: {time_zone}")