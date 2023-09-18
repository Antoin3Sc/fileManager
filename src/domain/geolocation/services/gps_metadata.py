import src.infrastructure.services.metadata as metadata
from src.domain.geolocation.value_objects.gps_coord import GPSCoord
from typing import Optional


def calc_degrees_minute_to_degrees_decimal(coord: dict, ref: str):
    decimal_degrees = coord[0] + \
                      coord[1] / 60 + \
                      coord[2] / 3600
    if ref == "S" or ref == "W":
        decimal_degrees = -decimal_degrees
    return decimal_degrees


def is_gps_metadata_available(metadata: list) -> bool:
    return ('gps_latitude' in metadata) and ('gps_longitude' in metadata)


def get_gps_metadata(file_path) -> Optional[GPSCoord]:
    image = metadata.get_image(file_path)
    metadata_available = metadata.get_metadata_available(image)
    if not is_gps_metadata_available(metadata_available):
        return None

    lat = calc_degrees_minute_to_degrees_decimal(image.get('gps_latitude'), image.get('gps_latitude_ref'))
    long = calc_degrees_minute_to_degrees_decimal(image.get('gps_longitude'), image.get('gps_longitude_ref'))

    return GPSCoord(lat, long)
