class character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def atack(self):
        print("atack")
class Hero(character):
    def __init__(self, weapon):
        self.weapon = weapon
class Enemy(character):
    def __init__(self, damage):
        self.damage = damage
