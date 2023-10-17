name = 'Prashant'

# indexing of strings
print(name[0])
print(name[-1])

# slicing of string
a = "hello how are you?"
print(a[0:5])  # [start:stop]
print(a[0:5:2])  # [start:stop:skip-step]

# reverse the string
print(a[::-1])

# length the string
print(len(a))

# capitalize the string
print(a.upper())

# lower case the string
print(a.lower())

# replace part of the string
print(a.replace("hello", "bro"))

# find index of the letter in string
print(a.find('e'))
