import phonenumbers
import opencage
import folium
from myphone import number
from phonenumbers import geocoder
pepnumber= phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
print(location) #to print country name
from phonenumbers import carrier
service_pro=phonenumbers.parse(number) #to print service provider name
print(carrier.name_for_number(service_pro,"en"))

from opencage.geocoder import OpenCageGeocode

key='6bac9a62f99449cca803069df9fd5842'
geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
#print(results)
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)

myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)

#saving the map
myMap.save("mylocation.html") #Just a file name.html




