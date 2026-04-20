### ✏️ Activity 1 – Create Your Own Hero

###Make your own hero object with a name, starting money, and one item.

###Then, use `.buy()` to add another item to your inventory.
class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
Johnny=Hero("Johnny", 67, ["Potion"])
Johnny.buy("Sword")





class Pet:
    def __init__(self, name, happiness, hunger):
        self.name=name
        self.happiness=happiness
        self.hunger=hunger
    def play(self,play)
Daniel=Pet("Daniel", 0, 0)
