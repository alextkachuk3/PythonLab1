from station import Station

import string


class MetroLine:

    def __int__(self, id: int, color: string):
        self.id = id
        self.color = color

    stations = []

    def add_station(self, station: Station, index=None):
        if index is None:
            return self.stations.append(station)
        else:
            return self.stations.insert(station, index)

    def remove_station(self, index):
        return self.stations.remove(index)

    def update_color(self, color):
        self.color = color
