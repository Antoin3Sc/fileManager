import os


class ManageFoldersService:
    def __init__(self, config):
        self.config = config

    def get_volume_data_paths(self, volume: str) -> list:
        volume_data_paths = []
        data_folders = self.config.get_data_folders()

        for data_folder in data_folders:
            folder_path = os.path.join(self.config.get_base_volume_path(), volume, data_folder)
            if os.path.isdir(folder_path):
                volume_data_paths.append(folder_path)

        return volume_data_paths

    def folders_list(self, dir_path: str) -> list:
        folders = []

        for item in os.listdir(dir_path):
            item_path = os.path.join(dir_path, item)

            if os.path.isdir(item_path):
                if os.path.basename(item_path) not in self.config.get_excluded_folders():
                    folders.append(item_path)

        return folders
