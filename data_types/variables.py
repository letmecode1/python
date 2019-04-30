########## Working with Variables ##########

my_string = "Today is Monday"
print(my_string)

my_string += " and I hate Mondays"
print(my_string)


'''
If we assign a variable with another variable it will be assigned to the result of the variable and not whatever that variable points to later
'''

test_string = 1
my_int = test_string
test_string = "Fetty Wap"
print(my_int)

