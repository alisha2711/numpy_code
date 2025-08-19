#type conversions   int =float
a=9 
b=1.5
sum =a+b
print(sum)

#a="2"
#b =2.3
#sum =a+b
#print(sum) #geeting error while adding string into float because yeh add nahi ho sakty 

#   TYPE CASTING : int + float automatically add ho jaty ha lakin jis ma hum manually add kary different types ko like int +float
#characters kabhi bhi int ma convert nahi ho sakty just digits hi convert ho sakty ha

a= int("3")
b =66
sum =a+b
print(sum)

b= str(66)
print(type(b))


#OUTPUT
name =input("enter your name:")    #inputhar value ko sting ma convert kar deta ha

print("welcome",name)



val =input("enter you marks:")

print(type(val), "you enters:",val)

data = int(input("enter you marks:"))
print(type(val), "you enters:",val)


   