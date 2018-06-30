#leapyear
l=int(input("Enter year"))
if l%4==0:
    if l%100==0:
        if l%400==0:
            print("Leap year")
else:
    print("Not a leap Year")
#check whether a squaere or triangle
print("*************************************************************")
l1=int(input("Lenghth"))
b=int(input("Breadth"))
if l1==b:
    print("It is square")
else:
    print("A Rectangle")
print("*************************************************************")
#input age of 3 people and determine oldest and youngest
a=list(map(int,input("Enter ages of three person").split()))
print("The oldest one is:",max(a))
print("The youngest one is:",min(a))
print("*************************************************************")
#question4
a=int(input())
if a>0 and a<=50:
    print("Sorry!No Prize this time")
elif a>=51 and a<=150:
    print("Congratulations! You won a Wooden Dog!")
elif a>=151 and a<=180:
    print("Congratulations! You won a Book")
elif a>=181 and a<=200:
    print("Congratulations! You won a Chocolates")
else:
    pass

print("*************************************************************")
#question5
q=int(input("Enter Quantity"))
cost=q*100
dis=(cost*10)/100
tcost=cost-dis
print("Total cost for user is:",tcost)



    
