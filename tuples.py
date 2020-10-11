#converting
_tuple=("Hi","Hello","How","Are","You","Zoe")
_list=list(_tuple)
print(_list[3])
print(type(_list))
_tuple=tuple(_list)
print(type(_tuple))

#Priting
for element in _tuple:
    print(element)

#deleting tuple or list
# del _tuple
# del _list

#join tuple
_tuple2=("Wow","Ji")
_tuple3=_tuple+_tuple2
print(_tuple3)

#count
print(_tuple3.count("Wow"))

#index
print(_tuple3.index("Wow"))