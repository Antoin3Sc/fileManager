import os


class ManageVolumesService:
    def __init__(self, config):
        self.config = config

    def get_external_volumes(self) -> list:
        external_volumes = []
        volumes_connected = os.listdir(self.config.get_base_volume_path())

        for volume_connected in volumes_connected:
            if volume_connected != self.config.get_local_disc():
                external_volumes.append(volume_connected)

        return external_volumes
