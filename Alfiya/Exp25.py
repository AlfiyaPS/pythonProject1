list1=[]
n=int(input("enter the no of elements"))
for i in range(0,n):
    i=input()
    list1.append(i)
print(list1)
list2=[]
k=int(input("enter the no of elements"))
for i in range(0,k):
    i=input()
    list2.append(i)
print(list2)
print("elements in list1 but not in list2 are:")
c=list(set(list1).difference(list2))
print(c)

