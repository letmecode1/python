points = (1.0, 2.0)
print(points)
third_point = points + (3.0,)
print(third_point)

x, y, z = third_point
print("x equals: " + str(x))
print(y)
print(z)

print("My name is: %s %s" % ("John", "Cena"))

this_range = range(100)
print(this_range)

# prints every 10 items
this_range = range(0,100,10)
print(this_range)

# prints every 100 items
this_range = range(0,1000,100)
print(this_range)
