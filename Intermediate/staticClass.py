#Static and Class Methods
class Person(object):
    population = 50
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, "is", self.age, "Years Old")

newPerson = Person("Chris",33)

#do not need an object for class methods
print(Person.getPopulation())
#static method called here
print(Person.isAdult(21))
#print display for newPerson
newPerson.display()