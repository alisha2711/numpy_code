#check if a list contain a palindrome(shuri sy bhi same hoand end sy parho to bhi same ) of elements 
list = []
l1=(input("enter a 1 element of list :"))
list.append(l1)
l2=(input("enter a 2 element of list :"))
list.append(l2)
l3=(input("enter a 3 element of list :"))
list.append(l3)
l4=(input("enter a 4 element of list :"))
list.append(l4)
copy_list= list.copy()
copy_list.reverse()
if(list == copy_list):
    print("list is palandrome")
else:
    print("list is not pallendrome")

    

