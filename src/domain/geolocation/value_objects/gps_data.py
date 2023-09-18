class GPSData:
    def __init__(self, country, state, city):
        self._country = country
        self._state = state
        self._city = city

    @property
    def country(self):
        return self._country

    @property
    def state(self):
        return self._state

    @property
    def city(self):
        return self._city