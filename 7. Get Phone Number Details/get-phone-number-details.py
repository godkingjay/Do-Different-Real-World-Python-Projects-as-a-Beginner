# import phonenumbers module
import phonenumbers as ph
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

number = input("Phone Number: ")
number = ph.parse(number)
country = geocoder.description_for_number(number, "en")
sim_card_provider = carrier.name_for_number(number, "en")
time_zone = timezone.time_zones_for_number(number)

print(f"Country: {country}")
print(f"Sim Card Provider: {sim_card_provider}")
print(f"Time Zone: {time_zone}")