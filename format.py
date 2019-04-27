# Replace {} in strings by other strings, numbers, or variables.
name = "Hello, my name is {}"
print(name.format("Alex"))

new_name = "Ben"
print(name.format(new_name))

# These get replaced in the order they appear.
sentence = "Welcome, my name is {} and I am {} years old."
print(sentence.format("John", 53))

# We can also give each a name, for more readability.
example2 = "Hello, my name is {name} and I am {age} years old."
print(example2.format(name="Quavo", age=25))

# Something frequently used is restricting decimal points to 2.
student_grade =  15.0/20
sgrade = "I scored {grade} on the test!"
print(sgrade.format(grade=student_grade))



