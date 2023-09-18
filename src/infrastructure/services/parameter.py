import yaml


class Parameter:
    def __init__(self):
        self.parameters = {}

    def load_parameter(self, yaml_file_path) -> None:
        try:
            with open(yaml_file_path) as file:
                self.parameters = yaml.load(file, Loader=yaml.SafeLoader)
        except FileNotFoundError:
            print("Yaml file not found")
        except Exception as e:
            print(f"Error: {e}")

    def get_projects_by_dates(self) -> list:
        return self.parameters.get('projects', None)
