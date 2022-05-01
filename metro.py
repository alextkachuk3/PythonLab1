from metro_line import MetroLine


class Metro:
    lines = []

    def add_line(self, color: str, id=None):
        if id is None:
            if len(self.lines) == 0:
                id = 'l-0'
            else:
                id = 'l-' + (self.lines[len(self.lines) - 1].id + 1)
        self.lines.append(MetroLine(id, color))

    def delete_line(self, id: str):
        self.lines = list(filter(lambda x: x.id != id, self.lines))

    def update_color(self, id: str, color: str):
        list(filter(lambda x: x.id == id, self.lines))[0].update_color(color)

    def add_station_to_line(self, line_id: str, name: str, open: str, close: str, id=None):
        list(filter(lambda x: x.id == line_id, self.lines))[0].add_station(name, open, close, id)
