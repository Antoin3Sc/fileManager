import os, datetime
import shutil
from src.infrastructure.value_objects.file import File


class ManageFilesService:
    def __init__(self, config, parameter, logs_service):
        self.config = config
        self.parameter = parameter
        self.logs_service = logs_service

    def get_files_list(self, dir_path: str) -> list:
        files = []

        for item in os.listdir(dir_path):
            item_path = os.path.join(dir_path, item)

            if os.path.isfile(item_path):
                if os.path.basename(item_path) not in self.config.get_excluded_folders():
                    files.append(item_path)

        return files

    def set_file_info(self, file: str) -> File:
        file_path = os.path.dirname(file)

        file_fullname = os.path.basename(file)
        file_name, file_extension = os.path.splitext(file)
        file_extension = file_extension.replace(".", "")

        file_object = open(file, 'rb')
        file_content = file_object.read()

        creation_timestamp = os.path.getctime(file)
        creation_datetime = datetime.datetime.fromtimestamp(creation_timestamp)
        formatted_datetime = creation_datetime.strftime('%d/%m/%Y')

        return File(file_fullname, file_extension, file_path, formatted_datetime, file_content)

    def get_destination_folder(self, file: File) -> str:
        base_volume_path = self.config.get_base_volume_path()
        backup_name = self.config.get_backup_name()
        project_name = self.get_project_name(file.created_at)
        extension = file.extension

        return os.path.join(base_volume_path, backup_name, project_name, extension)

    def get_project_name(self, date: str) -> str:
        projects_by_dates = self.parameter.get_projects_by_dates()
        date_to_test = datetime.datetime.strptime(date, '%d/%m/%Y')

        for entry in projects_by_dates:
            for project, date_ranges in entry.items():
                start = datetime.datetime.strptime(date_ranges[0], '%d/%m/%Y')
                end = datetime.datetime.strptime(date_ranges[1], '%d/%m/%Y')

                if start <= date_to_test <= end:
                    return project

        error_message = 'Country not found in date ranges with date project :' + str(date_to_test)
        self.logs_service.add_error_log(error_message)
        raise Exception(error_message)

    def move_file_to_new_folder(self, file: File, destination_folder: str) -> bool:
        try:
            os.makedirs(destination_folder, exist_ok=True)
            old_path = os.path.join(file.path, file.filename)
            new_path = os.path.join(destination_folder, file.filename)

            if os.path.exists(new_path):
                self.logs_service.add_duplicated_log(old_path)
                return False
            else:
                shutil.copy(old_path, new_path)
                return True

        except Exception as e:
            self.logs_service.add_error_log(e)
            print(f"Error while moving the file: {e}")
