### ✏️ Activity 1 – Create Your Own Hero

###Make your own hero object with a name, starting money, and one item.

###Then, use `.buy()` to add another item to your inventory.
""" class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
Johnny=Hero("Johnny", 67, ["Potion"])
Johnny.buy("Sword") """
#✏️ Activity 2 – Add Encapsulation
#Create a class Pet that has:
#A name
#A private variable for happiness level (e.g., __happiness)
#A method to play() that increases happiness
#A method to show_status() that prints how happy the pet is
class Pet:
    def __init__(self, name, happiness, hunger, health, strength, level, xp):
        self.name=name
        self.happiness=happiness
        self.hunger=hunger
        self.xp=xp
        self.health=health
        self.strength=strength
        self.level=level
    def feed(self, pettreat):
        g=self.hunger+pettreat*2
        if g>10:
            g=10
        self.hunger=g
    def play(self,timeplay):
        hgain=self.happiness+timeplay*3
        huloss=self.hunger-timeplay*1
        if hgain>10:
            hgain=10
            self.happiness=hgain
        if huloss>0:
            self.happiness=hgain
            self.hunger=huloss
            self.xp+1
        elif huloss<0:
            print("Not enough hunger. Feed your pet!")
    def power(level, strength):
        powerup=level*1.2
        u=powerup*strength

    def checkstat(self):
        print(f"Happiness: {self.happiness}")
        print(f"Hunger: {self.hunger}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"XP: {self.xp}")
        print(f"Level: {self.level}")
    
Daniel=Pet("Daniel", 0, 0, 20, 1, 1, 0) 
Chicken=Pet("DanielKiller", 0, 0, 100000000, 5000, 100, 0)
Daniel.feed(5)
Daniel.play(4)
Daniel.checkstat()