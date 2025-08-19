#Tuple :works as like listing but is immutable hota ha (change nahi kar sakty)
tup=(2,1 ,3, 4)
print(tup[0])
print(tup[3])
#tup[0]=5  not posssible 
tup=()
print(tup)
print(type(tup))
tup =(1,) # (1,)single values ky sath koma zarroor ho warna yeh simple integer declare ho ga 
print(tup)
print(type(tup))
tup=(1)
print(tup)
print(type(tup))
#Slicing
tup= (1,6 ,5, 9,5)
print(tup[1:4])
#indexMthod ka mtlb element nikalna 
print(tup.index(6))
#countmethodka matlb wo element kitni bar tuple ma aya ha 
print(tup.count(5))