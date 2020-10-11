_list=["Apple","Mango","Orange","Water Melon","Jack"]
print(_list[2:5])

#Replacing
_list[1]="Hello"
print(_list)

#Printing all elements in list
for i in _list:
    print(i)

#If element in list
if "Apple" in _list:
    print("Yes")
else:
    print("Alas")

_input="CCXXSS"
if _input in _list:
    print("Yes")
else:
    print("Alas!! Not found")

#Length of list
print(len(_list))

#Append
_list.append("Blackberry")
print(_list)

#insert element
_list.insert(1,"Pomogranate")
print(_list)

#Remove
_list.remove("Orange")
print(_list)

#Pop
_list.pop(2)
print(_list)

#clear
#_list.clear()
#print(_list)

#copy
_newlist=_list.copy()
print("New List=" +str(_newlist))

#extend
_newList=["Hi","Hello"]
_list.extend(_newList)
print(_list)