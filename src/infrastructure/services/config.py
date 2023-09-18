import yaml


class Config:
    def __init__(self):
        self.config = {}

    def load_config(self, yaml_file_path) -> None:
        try:
            with open(yaml_file_path) as file:
                self.config = yaml.load(file, Loader=yaml.SafeLoader)
        except FileNotFoundError:
            print("Yaml file not found")
        except Exception as e:
            print(f"Error: {e}")

    def get_logs_path(self) -> str:
        return self.config.get('logs_path')

    def get_duplicated_logs_file(self) -> str:
        return self.get_logs_path() + self.config.get('duplicated_logs_file')

    def get_error_logs_file(self) -> str:
        return self.get_logs_path() + self.config.get('error_logs_file')

    def get_backup_name(self) -> str:
        return self.config.get('storage_disc_name', None)

    def get_data_folders(self) -> list:
        return self.config.get('data_folders', None)

    def get_excluded_folders(self) -> list:
        return self.config.get('excluded_folders', None)

    def get_local_disc(self) -> str:
        return self.config.get('local_disc')

    def get_base_volume_path(self) -> str:
        return self.config.get('base_volume_path')

    def get_stored_location_file(self) -> str:
        return self.config.get('stored_locations_file')

    def get_encryption_key_path(self) -> str:
        return self.config.get('key_path')
