#TUPLES
print(*****************************T U P L E S*******************************)
#QUESTION 1
t1=('taran',4,4.0,[2,3,4],[3,'kaur'])
print(t1)
#finding len of tule
print("length of tuple is",len(t1))
#finding largest and smallest element of tuple
t2=(5,6,7,810,34,56,12)
print("Maximum element is:",max(t2))
print("Minimum element is:",min(t2))
#product of element of tuples
t3=(2,3,5,6)
p=1
for i in t3:
    p=p*i
print(p)
print("Product of elements of tuples is:",p)

print(**************S E T S ************************)
#SETS
s1=set(map(int,input().split()))
s2=set(map(int,input().split()))
s3=s1-s2
print("Difference btw sets is",s3)
s4=s1&s2
print("Intersection of Set1 and set2 is",s4)
#compare sets
if s1>s2:
    print("S1 is Superset")
elif s1<s2:
    print("S2 is superset")
else:
    print("S1 and S2 are same")
print(************* D I C T I O N A R I E S**************************)
#DICTIONARIES
mydic={"names":["Taran","Karan","Sam","Jass","Nivi"],"Marks":[79,60,65,89,91]}
a=mydic['Marks'].sort()
print(mydic['Marks'])

print("********************************")
for i in a:
	j={}
	j=a.count(i)
	print(i,j)
