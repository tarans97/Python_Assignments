print("**********************10 I N T E G E R S**********************")
#print10integers
for i in range(1,11):
    print(i)
print("************************ S Q U A R E  O F  E L E M E N T S*************")
#create a list of integers elements by user and store squares of elements in other list
l=list(map(int,input().split()))
l1=[]
for i in l:
    i=i*i
    l1.append(i)
print(l1)
print("***********************E V E N  O D D***************************")
even=[]
odd=[]
for i in range(1,101):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even Elements are:",even)
print("Odd list of elements are:",odd)
print("************** D A T A  T Y P E S  I N  L I S T S*******************")
li=['taran',5,5.6,'5',[4,5,6]]
for i in li:
    j=type(i)
    print(j)
print("****************P  A T T E R N**************************")
for i in range(5):
    print(i*"*")
print("*****************I N F I N I T E  L O O P S****************")
print("*******************L I S T   C R E A T I O N************************")
l=list(map(int,input().split()))
print(l)
a=int(input("Enter element to search"))
for i in l:
    if a in l:
        print("Found",a)
        
        l.remove(a)
print("List after deleting searched element",l)
print("********************D I C T I O N A R Y*****************")
for x in range(5):
	a = input('enter the key')
	b = int(input('enter the values'))
	dic[a]=b
print(dic)
#write infinite loop
i=1
while(1):
    print(i)
    i=i+1

