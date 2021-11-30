import requests

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
