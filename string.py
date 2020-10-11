_x="""This,is a multitline string 
with 3 lines one as a example for
each other"""
print(_x)     

_start_element=_x[0]
print(_start_element)

_sliced=_x[2:10]
print(_sliced)          

_neg_slice=_x[-10:-2]
print(_neg_slice)

_length=len(_x)
print(_length)

_stripped=_x.strip()
print(_stripped)

_upper=_x.upper()
print(_upper)

_lower=_x.lower()
print(_lower)

_replaced=_x.replace("multitline","fck")
print(_replaced)

_splitted=_x.split(" ")
print(_splitted)
print(type(_splitted))

_check="line" in _x
print(_check)

_result=_x+" F * C * K"
print(_result)

_result=_x+str(35)
print(_result)

_str="My Name is Athul  i am called \"Kuttan\""
print(_str)