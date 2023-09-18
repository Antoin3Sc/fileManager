from src.infrastructure.services.manage_files import ManageFilesService
from src.infrastructure.services.manage_folders import ManageFoldersService
from src.infrastructure.services.manage_volumes import ManageVolumesService


class Backup:
    def __init__(self, config, parameter, logs):
        self.config = config
        self.parameter = parameter
        self.logs = logs

    def get_volume_backup(self, volumes: list) -> str:
        backup_name = self.config.get_backup_name()
        if backup_name in volumes:
            return backup_name

        error_message = 'Backup storage not found'
        self.config.add_error_log(error_message)
        raise Exception(error_message)

    def get_external_volumes_to_save(self, volumes: list) -> list:
        backup_name = self.get_volume_backup(volumes)
        if backup_name in volumes:
            volumes.remove(backup_name)

        return volumes

    def action(self):
        volumes_service = ManageVolumesService(self.config)
        folders_service = ManageFoldersService(self.config)
        files_service = ManageFilesService(self.config, self.parameter, self.logs)

        volumes = volumes_service.get_external_volumes()
        volumes_to_save = self.get_external_volumes_to_save(volumes)
        files_moved = 0

        for volume_to_save in volumes_to_save:
            base_data_path_folders = folders_service.get_volume_data_paths(volume_to_save)

            for base_data_path_folder in base_data_path_folders:
                data_path_folders = folders_service.folders_list(base_data_path_folder)

                for data_path_folder in data_path_folders:
                    print(f'processing folder: {data_path_folder}')
                    files = files_service.get_files_list(data_path_folder)
                    total_files = len(files)
                    files_managed = 0

                    for file in files:
                        file_info = files_service.set_file_info(file)
                        if file_info:
                            destination_folder = files_service.get_destination_folder(file_info)
                            is_file_moved = files_service.move_file_to_new_folder(file_info, destination_folder)
                            files_managed += 1
                            if is_file_moved:
                                files_moved += 1
                            print(f'{files_managed}/{total_files} file(s) managed')

        print(f'{files_moved} file(s) moved')
