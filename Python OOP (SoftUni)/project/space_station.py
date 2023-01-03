from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        for ast in self.astronaut_repository.astronauts:
            if ast.name == name:
                return f"{name} is already added."

        if astronaut_type == "Biologist":
            self.astronaut_repository.astronauts.append(Biologist(name))
        elif astronaut_type == "Geodesist":
            self.astronaut_repository.astronauts.append(Geodesist(name))
        elif astronaut_type == "Meteorologist":
            self.astronaut_repository.astronauts.append(Meteorologist(name))
        else:
            raise Exception("Astronaut type is not valid!")

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        for p in self.planet_repository.planets:
            if p.name == name:
                return f"{name} is already added."
        p = Planet(name)
        p.items = items.split(", ")
        self.planet_repository.planets.append(p)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self,name: str):
        for ast in self.astronaut_repository.astronauts:
            if ast.name == name:
                self.astronaut_repository.astronauts.remove(ast)
                return f"Astronaut {name} was retired!"
            else:
                raise Exception(f"Astronaut {name} doesn't exists!")

    def recharge_oxygen(self):
        for ast in self.astronaut_repository.astronauts:
            ast.oxygen += 10

    def send_on_mission(self, planet_name: str):
        for p in self.planet_repository.planets:
            if not p.name == planet_name:
                raise Exception(f"Invalid planet name!")
        needed_ast = [ast for ast in self.astronaut_repository.astronauts if ast.oxygen > 30]
        if not needed_ast:
            raise Exception("You need at least one astronaut to explore the planet!")
        return "Mission is not completed."


    def report(self):
        pass