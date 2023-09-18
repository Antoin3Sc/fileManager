class GPSCoord:
    def __init__(self, lat, long):
        self._lat = lat
        self._long = long

    @property
    def lat(self):
        return self._lat

    @property
    def long(self):
        return self._long
