class Planet:
    def __init__(self, name, mass, radius) -> None:
        self.name = name
        self.mass = mass
        self.radius = radius
    
    def get_name(self):
        return self.name

    def get_mass(self):
        return self.mass

    def get_radius(self):
        return self.radius
    