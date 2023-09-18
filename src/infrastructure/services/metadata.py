from exif import Image


def get_image(file_path: str) -> Image:
    with open(file_path, 'rb') as file:
        return Image(file)


def get_metadata_available(image: Image) -> list:
    return image.list_all()