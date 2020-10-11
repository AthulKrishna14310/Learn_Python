#Function and Global variable
out="Hello World"
def fun():
    print(out)
fun()

#global keyword
def function():
    global x , y
    x="Hello"
    y="world"
function()
print(x)
print(y)

