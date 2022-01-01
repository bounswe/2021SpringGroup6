import requests
import geopy.distance

def get_address(latitude, longitude):

    URI = f'https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={str(latitude)}&lon={str(longitude)}'

    try:
        headers = {"Accept-Language": "en-US,en;q=0.5"}
        res = requests.get(URI, headers=headers)

        if res.status_code != 200:
            return 500
        if not "address" in res.json().keys():
            return 400
        return res.json()['address']
        
    except:
        return 500

def _get_distance(coordinate1, coordinate2):
    return geopy.distance.distance(coordinate1, coordinate2).m

def sort_by_distance(item1,item2):
    event1,user1 = item1
    event2,user2 = item2
    dist1 = _get_distance((event1.latitude, event1.longitude), (user1.latitude, user1.longitude))
    dist2 = _get_distance((event2.latitude, event2.longitude), (user2.latitude, user2.longitude))
    
    if dist1 < dist2:
        return -1
    elif dist1 > dist2:
        return 1
    else:
        return 0