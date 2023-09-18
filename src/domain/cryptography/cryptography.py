import os
from src.infrastructure.services.manage_files import ManageFilesService
from src.infrastructure.value_objects.file import File
from cryptography.fernet import Fernet


class Cryptography:
    def __init__(self, config, logs):
        self.config = config
        self.logs = logs
        self.key = self.get_key()

    def generate_key(self):
        key = Fernet.generate_key()
        with open(self.config.get_encryption_key_path(), 'wb') as file_key:
            file_key.write(key)
            pass

    def get_key(self) -> Fernet:
        if not os.path.exists(self.config.get_encryption_key_path()):
            self.generate_key()

        with open(self.config.get_encryption_key_path(), 'rb') as filekey:
            key = filekey.read()
            return Fernet(key)

    def encrypt(self, file: File) -> None:
        if not file.filename.endswith('.encrypted'):
            file_name_encrypted = self.key.encrypt(file.filename.encode())
            file_content_encrypted = self.key.encrypt(file.content)
            new_file_path = os.path.join(file.path, file_name_encrypted.decode() + '.encrypted')

            with open(new_file_path, 'wb') as encrypted_file:
                encrypted_file.write(file_content_encrypted)

            old_file = os.path.join(file.path, file.filename)
            os.remove(old_file)

    def decrypt(self, file: File) -> None:
        if file.filename.endswith('.encrypted'):
            file_name = file.filename[:-10]
            file_name_decrypted = self.key.decrypt(file_name)
            file_content_decrypted = self.key.decrypt(file.content)

            new_file_path = os.path.join(file.path, file_name_decrypted.decode())
            with open(new_file_path, 'wb') as decrypted_file:
                decrypted_file.write(file_content_decrypted)

            old_file = os.path.join(file.path, file.filename)
            os.remove(old_file)

    def action(self, path: str, action: str):
        files_service = ManageFilesService(self.config, None, self.logs)
        files = files_service.get_files_list(path)

        files_encrypted = 0
        for file_path in files:
            files_encrypted += 1
            file = files_service.set_file_info(file_path)
            if action == 'encrypt':
                self.encrypt(file)
            elif action == 'decrypt':
                self.decrypt(file)
            else:
                raise Exception('Unknown action')

        print(f'{files_encrypted} file(s) encrypted')
