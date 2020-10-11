#Initialise
_dictionary={
    "Name":"Game of Thrones",
    "Actor":"Peter Dinglage",
    "Actress":"Emilia Clarke",
    "Director":"George Lucas",
    "Year":2011,
    "Episodes":73,
    "Season":8,
}

#Print Element
print(_dictionary["Season"])
_year=_dictionary["Year"]
print(_year)

#Changing value
_dictionary["Year"]=2021
print(_dictionary)

#Printing keys
print("\n\nPrinting Keys")
for key in _dictionary:
    print(key)

#Printing Values
print("\n\nPrinting Values")
for value in _dictionary.values():
    print(value)

#Printing items
for item in _dictionary.items():
    print(item)

#Printing two variables
for key,value in _dictionary.items():
    print(str(key)+str(value))

#Adding element
_dictionary["Villian"]="Leena Hedy"
print(_dictionary)

#removing element
_dictionary.pop("Villian")
print(_dictionary)

#clear
new=_dictionary
print(new)
new.clear()
print(new)

#Nested Dictionary
_nestedDictionary={
"food1":{
    "eat":"Rice",
    "drink":"Milk"     
    },
"food2":{
    "eat":"biriyani",
    "drink":"cola"
    }
}
print(_nestedDictionary["food2"])