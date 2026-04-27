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
    def __init__(self, name, happiness, hunger, health, strength, level):
        self.name=name
        self.happiness=happiness
        self.hunger=hunger
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
        print(huloss)
        if huloss>0:
            self.happiness=hgain
            self.hunger=huloss
        if hgain>10:
            lev=input("Would you like to level up?")
            if lev=="Yes":
                poo=self.level+hgain/10
                self.level=poo
                hegain=self.health+self.level*10
                stre=self.strength+self.level*1
                self.health=hegain
                self.strength=stre
                hgain=hgain%10
            elif lev=="No":
                self.happiness=hgain
        elif huloss<0:
            print("Not enough hunger. Feed your pet!")
    def checkstat(self):
        print(f"Happiness: {self.happiness}")
        print(f"Hunger: {self.hunger}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Level: {self.level}")
    
Daniel=Pet("Daniel", 0, 0, 20, 1, 1) 
Chicken=Pet("DanielKiller", 0, 0, 100000000, 5000, 100)
Daniel.feed(5)
Daniel.play(10)
Daniel.checkstat()