from geopy.geocoders import Nominatim

def pegar_endereco(endereco):
    geolocator = Nominatim(user_agent="api_endereco")
    location = geolocator.geocode(endereco)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None
