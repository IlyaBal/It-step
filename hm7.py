class Character:
    def init(self, name):
        self.name = name

    def introduce(self):
        print("Character's name is " + self.name)


class Inventory:
    def init(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item} to inventory")

    def iter(self):
        return iter(self.items)


def special_ability(func):
    counter = 0

    def wrapper(self):
        nonlocal counter
        counter += 1
        if counter > 3:
            print("Special ability is not available")
            return
        print(f"Special ability using: {counter} times")
        return func(self)

    return wrapper


class Player(Character):
    def init(self, name):
        super().init(name)
        self.inventory = Inventory()

    def introduce(self):
        print("Player's name is " + self.name)

    def show_inventory(self):
        print("Player's inventory:")
        for item in self.inventory:
            print(item)

    @special_ability
    def special_move(self):
        print("Player's special move")

    def health_manager(self):
        health = 100

        def manage_health(change=0):
            nonlocal health
            health += change
            print(f"Health: {health}")
            return health

        return manage_health


    def find_item(self, item_name):
        found = False
        for item in self.inventory:
            if item == item_name:
                yield item
                found = True
                break
        if not found:
            yield "Item not found"


x = Character("Bob")
x.introduce()

player1 = Player("John")
player1.inventory.add_item("sword")
player1.inventory.add_item("shield")
player1.inventory.add_item("potion")
player1.introduce()
player1.show_inventory()
u = 0
while (u < 6):
 player1.special_move()
 u += 1

player_health_fn = player1.health_manager()
player_health_fn(10)
player_health_fn(-20)


print(next(player1.find_item("sword")))

i2 = player1.find_item("potion")
print(next(i2))

i3 = player1.find_item("gun")
print(next(i3))

myitems = []
myitems.append("sword")
myitems.append("shield")
myitems.append("potion")

for item in myitems:
     print(item)