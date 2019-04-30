############### Reading from Lists ###############

list1 = [1,55,213,354,5,100, 999, 1000]
print(list1[0])
print(list1[2])
print(list1[-1])

print(len(list1))   # print the lenght of the list
print(list1[0:3])
print(list1[1:])
print(list1[:4])
print(list1[1::2])
print(list1[0::3])

############### Editing a List ###############
list1[0] = "a"
print(list1)

list1.append(4556)
print(list1)
list1.append(-2)
print(list1)

# You can add lists together
list1 += [11, 12, 13]
print(list1)

list1[1:3] = ["b", "c"]
print(list1)

#remove a section of the list by adding an empty list to the slice
list1[5:]= []
print(list1)

# remove number 5 from the list
list1.remove(5)
print(list1)

# remove the last item from a list
list1.pop()
print(list1)

# remove item using the index and pop method 
list1.pop(0)
print(list1)
