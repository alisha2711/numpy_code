#LISTING: built-in data type that stores set of values
#It store elements of dufferent type( integer , float, string etc)
#string are immutable (access only ,change are not allowed)
#string  are mutable (access+change also)
student =[77,22,"alisha", "lahore"]
student[2]= "fatima"
print(student[2])
print(len(student))
#Slicing in listing as like string /sublisting
print(student[1:3]) # ending index is not included
#List.append= 1 element value end par add karna 
list= [49,98,8,90,55]
result =list.append(10)
print(result)
print(list.sort())   #SORTING :arrange in ascending / descending order(int ko int ky sath hi compare karta ha bs)
 #sort and append never retuen any value 

print (list.reverse())
print(list)
print(list.sort(reverse=True))
print(list)
#listing.insert : center ma koi value insert karnab indx,el
list1 =[2,3,5] 
list1.insert(1,9)
print(list1)
list1.remove(3)
print(list1)
list1.pop(0)
print(list1)









