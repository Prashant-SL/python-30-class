# Tuple datatype is immutable

tuple1 = (1, "prashant", True, 0.2, 112+4j)
print(tuple1)
print(type(tuple1))
newtuple = (tuple1, tuple1)
print(newtuple)

# creating tuple with only one item
var2 = ("hello",)
print(var2)

# slicing part of tuple
print(newtuple[0:2])

# we can not add or remove item from a tuple. But there is a way. We can convert tuple to list and then do modification and then convert it back to tuple.
a = (1, 2, 3, 4, 5)
b = list(a)
b.append(6)
a = tuple(b)
print("a", a)
print("b", b)

#  looping in tuple
for x in a:
    print(x)

#  join in tuple
tuple3 = a+a
print(tuple3)

# multiple tuple
print("tuple3", tuple3*2)
print("tuple3", tuple3+tuple3+tuple3)

#  take 5 input and store it in a tuple
inp = ()
n = 5
a = 0
while a < n:
    inp = inp+(int(input()),)
    a += 1
print(inp)
