#Question1
try:
    a=3
    if a<4:
        b=a/(a-3)
        print(b)
except(ZeroDivisionError):
    print("Number can't be divided by zero")
#Question2
   
try:
    l=[1,2,3]
    print(l[3])
except(IndexError):
    print("IndexErrorr: Index doesn't Exist")

#question 3 OUTPUT ORIENTED
try:
    raise NameError("Hi there")
except NameError:
    print "a"
    
