Marks =int(input("Enter your marks here:"))
if(Marks>=90):
    Grade="Congartulation ,You got A grade"
elif(Marks<90 and Marks >=80):
    Grade ="congratulation , you got B grade"
elif(Marks<80 and Marks>=70):
    Grade ="Congratulation , you got c Grade"
elif(Marks<70 and Marks>=60):
    Grade ="you got grade D"
elif(Marks<60 and Marks >=50):
    Grade ="you are pass "
else:
    (Marks <50)
    Grade ="sorry you are fail"
print(Grade)
