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
        self.__hunger=hunger
    def feed(self, pettreat):
        self.__hunger+pettreat*2
        if self.__hunger>10:
            self.__hunger=10
        print(pettreat)
        print(self.__hunger)
    def play(self,timeplay):
        if self.happiness+timeplay*.5>10:
            self.happiness=10
        if self.__hunger-timeplay*.1>0:
            self.happiness+timeplay*.5
            self.__hunger-timeplay*.1
        elif self.__hunger-timeplay*.1<0:
            print("Not enough hunger. Feed your pet!")
        print(timeplay)
        print(self.__hunger)
    def checkstat(self):
        print(self.happiness)
        print(self.__hunger)
    
Daniel=Pet("Daniel", 0, 0) 
Daniel.feed(5)
Daniel.play(4)
Daniel.checkstat()