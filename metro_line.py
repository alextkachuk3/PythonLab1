from station import Station


class MetroLine:

    def __init__(self, id: str, color: str):
        if type(id) != str:
            raise ValueError("id value should be string")
        if type(color) != str:
            raise ValueError("color value should be string")
        self.id = id
        self.color = color

    stations = []

    def add_station(self, station: Station, index=None):
        if index is None:
            return self.stations.append(station)
        else:
            return self.stations.insert(station, index)

    def remove_station(self, id: str):
        self.stations = list(filter(lambda x: x.id != id, self.stations))

    def update_color(self, color):
        if type(color) != str:
            raise ValueError("color value should be string")
        self.color = color
