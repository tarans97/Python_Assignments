'''class Animal():
    def animal_attribute():
        print("I am base class Attribute")
class Tiger(Animal):
    Animal.animal_attribute()
t=Tiger()
t.animal_attribute()
print("**********************Q U E S T I O N-3***************************")
class Cop():
    def __init__(self,name,age,exp):
        self.name=name
        self.age=age
        self.exp=exp
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Experience:",self.exp)
    def update(self):
        self.name=input("Update Name:")
        self.age=int(input("Update Age:"))
        self.exp=int(input("Update Experience"))
class Mission(Cop):
    def __init__(self):
        super.__init__(self)
    def add_mission_details(self):
        super().display()
        super().update()
c=Mission()
c.add_mission_details()
        '''
class Shape():
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area():
        return self.l*self.b
class Rectangle(Shape):
    def area():
        self.area()
r=Rectangle(5,6)
r.area()
    
        
