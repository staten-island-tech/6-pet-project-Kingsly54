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
    def __init__(self, name, happiness, hunger):
        self.name=name
        self.happiness=happiness
        self.hunger=hunger
    def feed(self, pettreat):
        z=pettreat*2+self.hunger
        if z>10:
            self.hunger=10
        elif z<10:
            self.hunger=z
    def play(self,timeplay):
        hgain=timeplay*.5
        hloss=timeplay*.1
        g=self.hunger-hloss
        y=self.happiness+hgain
        if y>10:
            self.happiness=10
        if g>0 and y<10:
            self.happiness+=hgain
            self.hunger-=hloss
        elif g<0:
            print("Not enough hunger. Feed your pet!")
    def checkstat(self):
        print(self.happiness)
        print(self.hunger)
    
Daniel=Pet("Daniel", 0, 0) 
Daniel.feed(5)
Daniel.play(4)
Daniel.checkstat()