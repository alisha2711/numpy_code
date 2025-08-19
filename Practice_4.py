# check if number entered by the user is odd or even
num =int(input("enter your number:"))
rem = num % 2
if (rem== 0):
   print("Entered num is Even")
else:
   print("Entered num is odd")
# find the greater of 3 numbers entered by the users

num1   =int(input("Enter your 1 num:"))
num2   =int(input("Enter your 2 num:"))
num3   =int(input("Enter your 3 num:"))

if(num1>=num2 and num1>=num3):
   print("Your Greater number is: ",num1)
elif(num1>num2):
   print("your greater number is :" ,num2)
else:
   print("your greater value is :",num3)

#check the number is multiple of 7 or not 
num= int(input("Enter any number:"))
if( num % 7 ==0):
   print("number is muliple of 7")
else:
   print("its not multiple of 7")

