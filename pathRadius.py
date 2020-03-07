import math
import jsonify as jsonify
import requests


def getDestination(a, r):
    # lat = float(input("Enter Lat"))
   # lat = 12.9555775
    lat = 12.9119453
    b = a * math.pi / 180
    latB = lat * math.pi / 180  # Converting to Radians;
    cosA = math.cos(b)
    sinA = math.sin(b)
    cosLat = math.cos(latB)
    # Printing The Value
    print("Cos A is ", cosA)
    print("Sin A is ", sinA)
    print("Cos(Lat) is", cosLat)
    print("Distance in Meter", r)
    print("Current Degree", a)
    east = r * sinA / cosLat / 111111
    north = r * cosA / 111111
    origin = "12.9119453,77.6381901"
    desLat = str(12.9119453 + east)
    desLong = str(77.6381901 + north)
    destination = desLat, desLong
    destination = ','.join(destination)
    print(destination)
    print(type(destination))
    # originF = float(origin)
    # destinationF = float (destination)
    # 12.9555775,77.637092
    # 12.9119453,77.6381901
    print()
    print("Origin Equal to ", origin)
    print("Destination Equal to ", destination)
    data = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins=" + origin + "&destinations=" + destination + "&key=YOUR_API_KEY"
    print(data)
    return origin, destination, data



#a = float(input("Enter Degree"))
# r=int(input("Enetr distance in meter"))
#a=45 #Degree
list_of_coordinate = []
FinalResult = ""
for a in range (0,359,10):
    r = 3000 #distance in Meters
    #r = r -300
    orig,dest,datum = getDestination(a,r)
    response = requests.get(datum)
    #response = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins=12.9555775,77.637092&destinations=12.9555775%2C77.65509201800002&key=YOUR_API_KEY").json()
    response = response.json()
    print(response)
    currentDistance = response["rows"][0]["elements"][0]["distance"]["text"]
    currentDistance = currentDistance [:-3]
    currentDistance = float(currentDistance)
    print(currentDistance)
    print("___________________________________________________________________________")


    while currentDistance > 3 :
        if r > 101 :
            r = r-100
            origins,destinations,newURL = getDestination(a,r)
            Aresponse=requests.get(newURL)
            Aresponse=Aresponse.json()
            if  Aresponse["rows"][0]["elements"][0]["status"] == "OK" :
                newDistance = Aresponse["rows"][0]["elements"][0]["distance"]["text"]
                newDistance = newDistance [:-3]
                print("welcome")
                print("distance",newDistance)
                if newDistance is not None:
                    newDistance = float(newDistance)
                    currentDistance = newDistance
                    if currentDistance <= 3.0 :
                        Aorigin = origins
                        Adestination = destinations
                        print("the Final Destination is",Adestination)
                        FinalResult =  FinalResult +"\n"+ Adestination
                        list_of_coordinate.append(Adestination)
            else:
                continue
        else:
            break


print(list_of_coordinate)










