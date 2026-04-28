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
import random
class Pet:
    def __init__(self, name, happiness, hunger, health, strength, level, numpettreat):
        self.name=name
        self.happiness=happiness
        self.hunger=hunger
        self.health=health
        self.strength=strength
        self.level=level
        self.numpettreat=numpettreat
    def feed(self, pettreat):
        ggg=self.numpettreat-pettreat
        if ggg>=0:
            g=self.hunger+pettreat*2
            if g>10:
                g=10
        else:
            print("Not enough pettreats")
    def play(self,timeplay):
        hgain=self.happiness+timeplay*3
        huloss=self.hunger-timeplay
        if huloss>=0:
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
                self.happiness=hgain%10      
            elif lev=="No":
                self.happiness=hgain
        elif huloss<0:
            print("Not enough hunger. Feed your pet!")
    def fishing(self, timesfished):
        for i in range(timesfished):
            fish=random.randint(0,2)
            if fish==2:
                print("You fished 2 pet treats!")
                yj=self.numpettreat+2
                self.numpettreat=yj
            elif fish==1:
                print("You fished 1 pet treat!")
                yj=self.numpettreat+1
                self.numpettreat=yj
            elif fish==0:
                print("You fished absolutely nothing")
    def checkstat(self):
        print(f"Happiness: {self.happiness}")
        print(f"Hunger: {self.hunger}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Level: {self.level}")
        print(f"Pet treats: {self.numpettreat}")
    
Daniel=Pet("Daniel", 0, 0, 20, 1, 1, 0) 
Daniel.fishing(100)
Daniel.feed(5)
Daniel.play(15)
Daniel.checkstat()