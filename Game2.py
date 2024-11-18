class InvalidValueEnergy(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Character:
    def __init__(self, name, health, energy, weapon):
        self.name = name
        self.__health = health
        self.__energy = energy
        self.__weapon = weapon
    def atack(self, energy):
        if energy >= 10:
         self.__energy -= 10
        elif self.__energy < 10:
            raise InvalidValueEnergy("you don't have energy")
    def take_damage(self, damage):
        self.__health -= damage
        if self.__health <= 0:
            return f"Character {self.name} is dead"
    def equip_weapon(self, weapon):
        items = ["sword", "axe", "bread"]
        c = 0
        while c != len(items):
            c += 1
            print("selected:", items[c])
            if c == len(items):
                c = 0
    def get_status(self):
        print(f"health:{self.__health}|energy:{self.__energy}|weapon equiped:{self.__weapon}")










try:
 vasya = Character("vasya", 100, 100, "sword")

 vasya.atack(energy=10)
except InvalidValueEnergy as e:
    print(e)