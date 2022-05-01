from metro_line import MetroLine


class Metro:
    lines = []

    def add_line(self, line: MetroLine):
        if type(line) != MetroLine:
            raise ValueError("line param should be MetroLine")
        self.lines.append(line)

    def delete_line(self, id: str):
        self.lines = list(filter(lambda x: x.id != id, self.lines))

    def update_color(self, id: str, color: str):
        list(filter(lambda x: x.id == id, self.lines))[0].update_color(color)

