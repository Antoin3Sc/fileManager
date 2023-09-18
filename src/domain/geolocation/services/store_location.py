import os, csv
from src.domain.geolocation.value_objects.gps_data import GPSData


class StoreLocationService:
    def __init__(self, config):
        self.config = config
        self.create_stored_location_file()

    def create_stored_location_file(self):
        stored_location_file_path = self.config.get_stored_location_file()
        if not os.path.exists(stored_location_file_path):
            header = ['Filename', 'Country', 'State', 'City']
            with open(stored_location_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)

    def get_location_file_path(self):
        return self.config.get_stored_location_file()

    def is_file_already_located(self, filename):
        with open(self.get_location_file_path(), mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and len(row) > 0 and row[0] == filename:
                    return True
        return False

    def add_location(self, file: str, gps_data: GPSData) -> bool:
        filename = os.path.basename(file)
        if self.is_file_already_located(filename):
            return False

        with open(self.get_location_file_path(), mode='a', newline='') as location_file:
            writer = csv.writer(location_file)
            writer.writerow([filename, gps_data.country, gps_data.state, gps_data.city])
        return True
