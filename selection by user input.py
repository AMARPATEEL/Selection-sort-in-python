def selectionsort(list):
    for i in range(0,len(list)):
        min=i
        print("Current minimum is:",list[i])
        for j in range (i+1,len(list)):
            if(list[min]>list[j]):
                min=j
        list[i],list[min]=list[min],list[i]
        print("new minimum is:",list[i])
        print(list)
        print()

list=[]
e=int(input("No of elments i the list:"));
for i in range(0,e):
    n=int(input("Enter an element:"));
    list.append(n)
print("List before sorting:",list)
selectionsort(list)
print("List after sorting:",list)
