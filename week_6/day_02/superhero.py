
class Superhero():
    def __init__(self, real_name, superhero_identity, super_power, arch_enemy):
        self.name = real_name
        self.identity = superhero_identity
        self.power = super_power
        self.enemy = arch_enemy


    def introduce(self):
        print(f"My name is {self.name} but my Superhero name is {self.identity}.")
        print(f"My superpower is {self.power} and my enemy is {self.enemy}")






