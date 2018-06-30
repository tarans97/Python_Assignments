Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #print anything on screen
>>> print("TARANVIR KAUR")
TARANVIR KAUR
>>> #join two strings using '+'
>>> a="Taranvir"
>>> b="Kaur"
>>> print(a+'\t'+b)
Taranvir	Kaur
>>> #Take input of 3 variables x,y, and z.Print their values on screen
>>> x=input("Enter First Variable:")
Enter First Variable:Taran
>>> y=input("Enter Second Variable:")
Enter Second Variable:Vir
>>> z=input("Enter Third Variable:")
Enter Third Variable:20
>>> print(x,y,z,sep='\n')
Taran
Vir
20
>>> #Print the following values using placeholders
>>> s="Acadview"
>>> course="Python"
>>> fees=500
>>> print((%s %s %d)%(s,course,fees))
SyntaxError: invalid syntax
>>> print(('%s %s %d')%(s,course,fees))
Acadview Python 500
>>> #Let's do some interesting exercise:
>>> name="Tony Stark"
>>> salary=1000000
>>> print(('%s %d')%(name,salary))
Tony Stark 1000000
>>> 
