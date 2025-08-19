#string: characters , concatination means characters adding 
str1 = "Alisha  "
str2 = "Shakil "
print(str1 + str2)
print(len(str1))   #space also count in string lenght
#INDEXING:  alisha pythn
        #   012345678910
str = "Alisha shakil"
ch = str[3]
print(ch)
print(str[9],str[8])  #indexing sy hum value change nahi kar sakty 
#str[4]="e"  not possible


#slicing : string ky parts ko slicing kahty ha 
#strgname[starting index:ending index]
#starting index include hota ha lakin ending index include nahi hta 

Str ="Alisha Shakil"
print(str[0:5])
print(str[7:len(str)])
print(str[7:]) #agar hum last valuenshi dety to by default last index select ho jata ha 

print(str[:5]) # agar satrting wala nahi hota to by default starting wali slsect kar lata ha 
#slicing negative indexing 
str ="apple"
print(str[-3:-1])
str = "i am learning and exploring language names paython language"
print (str.endswith("language"))
print(str.capitalize()) #capitalize ap just aik bar kar sakty ho original string ma changes nahi hoti  
print(str) #agar original string ma captilze karna ha to" str = strn.capitalize()" ma add karwa do
print(str.replace("o" ,"a"))
print(str.replace("learning" ,"teaching"))
print(str.find("language"))
print(str.find("q")) # agar letter string ma available na ho to "-1" a jata ha
print(str.count("language"))


