print("**********************Q U E S T I O N- 1*******************")
class Circle():
    def __init__(self):
        self.radius=int(input("Enter Radius"))
        self.area=0
    def getArea(self):
        self.area=3.14*self.radius*self.radius
        print("Area of Circle is:",self.area)
    def getCircumference(self):
        circum=2*3.14*self.radius
        print("Circumference of Circle is:",circum)
a=Circle()
a.getArea()
a.getCircumference()
        
print("**********************Q U E S T I O N- 2*******************")
class Student():
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.age=int(input("Enter Age:"))
    def display(self):
        print("Name of student is",self.name)
        print("Roll No. of student is",self.roll)
        print("Age of Student is:",self.age)
s=Student("Taran",9)
s.display()
s1=Student("Jass",3)

s1.display()
print("**********************Q U E S T I O N- 3*******************")
class Temperature():
    def convertFahrenheit(self,c):
        f=(c*1.8)+32
        print("Temperature in farenheit is:",f)
    def convertCelsius(self,f):
        c= (f-32)/1.8
        print("Temperature in Celsius is:",c)
t=Temperature()
c=int(input("Enter Temperature in Celsius:"))
t.convertFahrenheit(c)
f=int(input("Enter temperature in Farenheit:"))
t.convertCelsius(f)
        

        
print("**********************Q U E S T I O N- 4*******************")
class MovieDetails():
    def __init__(self,name,artistname,year,ratings):
        self.name=name
        self.artistname=artistname
        self.year=year
        self.ratings=ratings
    def display(self):
        print("Movie Name:",self.name)
        print("Artist Name:",self.artistname)
        print("Year:",self.year)
        print("Ratings:",self.ratings)
    def update(self):
        self.name=input("Update Name:")
        self.artistname=input("Update Artistname:")
        self.year=int(input("Update Year:"))
        self.ratings=int(input("Ratings:"))
        
m1=MovieDetails("3Idiots","amir",5,9)
m1.display()
m1.update()
m1.display()

print("**********************Q U E S T I O N-5*******************")
class Expenditure():
    def __init__(self):
        self.expenditure=int(input("Expenditure:"))
        self.savings=int(input("Savings:"))
    def display(self):
        print("****Displaying Data*****")
        print("Expenditure:",self.expenditure)
        print("Savings:",self.savings)
    def salary(self):
        self.salary=self.expenditure+self.savings
    def totalsalary(self):
        print("Total Salary:",self.salary)
e=Expenditure()
e.display()
e.salary()
e.totalsalary()
        


