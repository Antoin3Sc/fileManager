import argparse
from src.infrastructure.services.config import Config
from src.infrastructure.services.parameter import Parameter
from src.infrastructure.services.logs import Logs
from src.domain.backup.backup import Backup
from src.domain.geolocation.geolocation import Geolocation
from src.domain.cryptography.cryptography import Cryptography


def main():
    config = Config()
    config.load_config('./src/infrastructure/config/config.yaml')

    parameter = Parameter()
    parameter.load_parameter('./src/infrastructure/config/parameters.yaml')

    logs = Logs(config)

    parser = argparse.ArgumentParser()
    parser.add_argument('--task', choices=['backup', 'geolocation', 'encrypt', 'decrypt'], required=True)
    parser.add_argument('--path', required=False)
    args = parser.parse_args()

    if args.task == 'backup':
        backup_service = Backup(config, parameter, logs)
        backup_service.action()

    if args.task == 'geolocation':
        geolocation_service = Geolocation(config, parameter, logs)
        geolocation_service.action(args.path)

    if args.task == 'encrypt' or args.task == 'decrypt':
        cryptography_service = Cryptography(config, logs)
        cryptography_service.action(args.path, args.task)


if __name__ == "__main__":
    main()



