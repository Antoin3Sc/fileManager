class Logs:
    def __init__(self, config):
        self.config = config
        self.reset_error_log_file()
        self.reset_duplicated_log_file()

    def reset_error_log_file(self):
        with open(self.config.get_error_logs_file(), 'w') as file:
            pass

    def add_error_log(self, error):
        with open(self.config.get_error_logs_file(), 'a') as file:
            file.write(f"{error}\n")

    def reset_duplicated_log_file(self):
        with open(self.config.get_duplicated_logs_file(), 'w') as file:
            pass

    def add_duplicated_log(self, filename: str):
        with open(self.config.get_duplicated_logs_file(), 'a') as file:
            file.write(f"{filename}\n")