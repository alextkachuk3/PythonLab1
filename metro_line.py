from station import Station


class MetroLine:

    def __init__(self, id: str, color: str):
        if type(id) != str:
            raise ValueError("id value should be string")
        if type(color) != str:
            raise ValueError("color value should be string")
        self.stations = []
        self.id = id
        self.color = color

    def add_station(self, name: str, open: str, close: str, id=None, index=None):

        if id is None:
            if len(self.stations) == 0:
                id = 's-' + self.id[1:] + '-1'
            else:
                id = 's-' + self.id[1:] + '-' + (self.stations[len(self.stations) - 1].id + 1)

        if index is None:
            self.stations.append(Station(id, name, open, close))
        else:
            self.stations.insert(index, Station(id, name, open, close))

    def remove_station(self, id: str):
        self.stations = list(filter(lambda x: x.id != id, self.stations))

    def update_color(self, color):
        if type(color) != str:
            raise ValueError("color value should be string")
        self.color = color
