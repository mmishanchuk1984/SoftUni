class AstronautRepository:

    def __init__(self):
        self.astronauts = []

    def add(self, astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        for el in self.astronauts:
            if el.name == name:
                return el







