class File:
    def __init__(self, filename, extension, path, created_at, content):
        self._filename = filename
        self._extension = extension
        self._path = path
        self._created_at = created_at
        self._content = content

    @property
    def filename(self):
        return self._filename

    @property
    def extension(self):
        return self._extension

    @property
    def path(self):
        return self._path

    @property
    def created_at(self):
        return self._created_at

    @property
    def content(self):
        return self._content
