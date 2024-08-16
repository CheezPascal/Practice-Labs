class Person:
    """A simple method to learn about classes"""
    def __init__(self, name, age):
        """initialize the attributes of this class """
        self.name = name
        self.age = age

    def walk(self):
        """Simulates the person which was created now walking... """
        print (f"{self.name} is now walking ")
        print (" ")

    def stand(self):
        """Simulates the person standing still... """
        print (f"{self.name} is now standing ")
        print (" ")

    def planking(self):
        """Simulates the created person doing the viral cringe plank challenge lol ... """
        print (f"{self.name} is now planking, very cringe ")   
        print (" ")

    def Avoiding_the_authorities(self):
        """Simulates the now running away from the local authorities becausee they created a henous crime... """
        print (f"{self.name} Has now stolen a cop car,they are running away, they will not make it...")    
        print (" ")
        
my_person1 = Person('Pablo', 45)
my_person2 = Person('CJ', 12)
my_person3 = Person('Myles', 90)
my_person4 = Person('MrGreen', 36)

my_person1.walk()
my_person1.stand()
my_person1.planking()        
my_person1.Avoiding_the_authorities()

my_person2.walk()
my_person2.stand()
my_person2.planking()
my_person2.Avoiding_the_authorities()

my_person3.walk()
my_person3.stand()
my_person3.planking()
my_person3.Avoiding_the_authorities()

my_person4.walk()
my_person4.stand()
my_person4.planking()
my_person4.Avoiding_the_authorities()