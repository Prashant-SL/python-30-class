list1 = ["apple", "ball", "cat", "dog"]

# length of list/array
print(len(list1))

# slice part of list/array
print(list1[0:2:2])

# change any item of list/array
list1[0] = "fish"
print(list1)

# change range(multiple) items of list/array
list1[0:1] = ['aeroplane', 'astronaut']
print(list1)

# add new item of list/array
list1.append("fish")
print(list1)

# remove new item of list/array
list1.remove("fish")
print(list1)

# remove new item of list/array
list1.reverse()
print(list1)


nos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
length = len(nos)
add = 0
for i in range(length):
    add += i
    i += 1
print(add)
