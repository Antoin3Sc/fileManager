import src.domain.geolocation.services.gps_metadata as metadata
from src.domain.geolocation.services.osm import get_locations_info_from_coordinates
from src.domain.geolocation.services.store_location import StoreLocationService
from src.infrastructure.services.manage_files import ManageFilesService


class Geolocation:
    def __init__(self, config, parameter, logs):
        self.config = config
        self.parameter = parameter
        self.logs = logs

    def action(self, path: str) -> None:
        files_service = ManageFilesService(self.config, self.parameter, self.logs)
        files = files_service.get_files_list(path)

        store_location_service = StoreLocationService(self.config)
        number_locations_found = 0
        for file in files:
            gps_coord = metadata.get_gps_metadata(file)
            if gps_coord:
                gps_data = get_locations_info_from_coordinates(gps_coord.lat, gps_coord.long)
                store_location_service.add_location(file, gps_data)
                number_locations_found += 1

        print(f'Number of location(s) found : {number_locations_found}')
