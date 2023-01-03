class PlanetRepository:

    def __init__(self):
        self.planets = []

    def add(self, planet):
        self.planets.append(planet)

    def remove(self, planet):
        self.planets.remove(planet)

    def find_by_name(self, name: str):
        for el in self.planets:
            if el.name == name:
                return el

