import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss.txt","w")
file.write("Tem "+str(result['number'])+" astronautas abordo \n\n")

people = result['people']

for p in people:
    file.write(p['name'] +  "- a bordo" + "\n")

g = geocoder.ip('me')

file.write("\n Latitute/ Longitude : " + str(g.latlng))
file.close()

webbrowser.open("iss.txt")


screen  = turtle.Screen()
screen.setup(1200,665)
screen.setworldcoordinates(-180,-90,180,90)

screen.bgpic("map.gif")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss2 = turtle.Turtle()
iss2.shape("iss.gif")
iss2.setheading(45)
iss2.penup()
iss.setheading(45)
iss.penup()


while True:
    #load the current status of the ISS in real time

    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    
    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']
    #output longitude e latitude para o terminal
    lat = float(lat)
    lon = float(lon)
    print('\n Latitude: ' + str(lat))
    print('\n Longitude: '+ str(lon))
    iss.goto(lon,lat)
    time.sleep(2)
    iss2.goto(90-lon,45-lat)

