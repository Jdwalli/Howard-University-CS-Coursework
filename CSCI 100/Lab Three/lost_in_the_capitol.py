#Extra Credit Included
# Capitol Maps: Find your way around D.C.!


Places = {
    "K St" : {"Lat" : 38.902649, "Long" : None},
    "the White House" : {"Lat" : 38.897789, "Long" : -77.036562},
    "Downing Hall" : {"Lat" : 38.921669, "Long" : -77.021361},
    "Dupont Circle" : {"Lat" : 38.909760, "Long" : -77.043479},
    "Union Station" : {"Lat" : 38.897698, "Long" : -77.007200}
}


Longitude_Rate = 53 #1:53 mi
Latitude_Rate = 69  #1:69 mi


def Distance_From_Downing_Hall(Lat, Long):
   #pythagorean theorem?
   
   a = (abs(Long) - abs(Places["Downing Hall"]["Long"])) * Longitude_Rate
   b = (abs(Lat) - abs(Places["Downing Hall"]["Lat"])) * Latitude_Rate
   legs = a ** 2 + b ** 2
   Hypotenuse = (legs) ** (0.5)
   
   print(f"You are {round(Hypotenuse,1)} miles from Downing Hall")


#Ask the user to input their lat and long
Lat = float(input("Insert your latitude: "))
Long = float(input("Insert your longitude: "))


for place, value in Places.items():
    if value["Lat"] != None:
        if Lat > value["Lat"]:
            print(f"You are north of {place}")
        else:
            print(f"You are south of {place}")
    
    if value["Long"] != None:
        if Long > value["Long"]:
            print(f"You are east of {place}")
        else:
            print(f"You are west of {place}")

Distance_From_Downing_Hall(Lat, Long)

   
   