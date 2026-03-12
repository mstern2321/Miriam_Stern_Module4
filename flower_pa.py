class Flower:
    def __init__(self, name, petals, color, height):
        self.name = name
        self.petals = petals
        self.color = color
        self.height = height
    def describe(self):
        print(f"{self.name} is {self.color}, has {self.petals} petals and is {self.height} cm tall.")
    def grow(self, amount):
        self.height += amount
rose = Flower("rose", 5, "red", 5)
tulip = Flower("tulip", 2, "blue", 7)
daisy = Flower("daisy", 8, "yellow", 8)
lily = Flower("lily", 6, "Purple", 6)

rose.describe()
tulip.describe()
daisy.describe()
lily.describe()
rose.grow(5)
tulip.grow(2)
daisy.grow(3)
lily.grow(4)

print("-------AFTER GROWTH-------")
rose.describe()
tulip.describe()
daisy.describe()
lily.describe()

print("-------GARDEN LOOP-------")
garden = [rose, tulip, daisy, lily]
for flower in garden:
    flower.grow(1)
    flower.describe()


