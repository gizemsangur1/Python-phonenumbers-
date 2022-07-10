from time import timezone
import phonenumbers
from test import pnumber

from phonenumbers import geocoder

ch_number= phonenumbers.parse(pnumber,"CH")
print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier
service_nmber=phonenumbers.parse(pnumber,"RO")
print(carrier.name_for_number(service_nmber,"en"))

from phonenumbers import timezone

tmezone=phonenumbers.parse(pnumber,"en")
tz=timezone.time_zones_for_number(tmezone)
print(tz)