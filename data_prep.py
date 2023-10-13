import json
import traceback
filep = open("/Users/apple/Desktop/car-resale/cars23.json", encoding = "utf")
filew = open("/Users/apple/Desktop/car-resale/cars23_new.json", 'w', encoding= "utf")

data = json.load(filep)
for item in data:
    try: 
        info = item.get("carDetails")
        for car_details in info:
            car_year = car_details.get('year')
            fuel_type = car_details.get('fuelType')
            # distance_driven = car_details.get("kilometerDriven")
            # price = car_details.get("price")
            # city = car_details.get("city")
            # views = car_details.get("views")
            # body_type = car_details.get("bodyType")
            # transmission = car_details.get("transmission")
            # is_top_selling = item.get("data").get("content").get("isTopSelling")
            # car_make = car_details.get("make")
            # car_model = item.get("data").get("content").get("model")
            # num_owners = item.get("data").get("content").get("ownerNumber")
        
            obj = {}
            obj["car_year"] = car_year
            obj["fuel_type"] = fuel_type
            
        filew.write(json.dumps(obj))   
        #filew.write(json.dumps(item.get('carDetails').get('content') + '\n')
        
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())
        
filew.close()   
        #set variables into dict
        
        
        
        
