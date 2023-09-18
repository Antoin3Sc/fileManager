from geopy.geocoders import Nominatim
from src.domain.geolocation.value_objects.gps_data import GPSData


def get_locations_info_from_coordinates(latitude: str, longitude: str):
    geolocator = Nominatim(user_agent="geoapiExercises")
    coordinates = f"{latitude},{longitude}"

    try:
        location = geolocator.reverse(coordinates, exactly_one=True)
        country = location.raw.get("address", {}).get("country")
        city = location.raw.get("address", {}).get("city")
        state = location.raw.get("address", {}).get("state")

        return GPSData(country, state, city)
    except Exception as e:
        print("Error:", e)
        return None
