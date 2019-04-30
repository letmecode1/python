single_qoutes = 'This is John'
double_qoutes = "This is Max"

print(single_qoutes)
print(double_qoutes)

triple_qouted = '''
this is a triple
qouted string
'''
print(triple_qouted)

password = "pass" + "word"
print(password)

ha = "HA" * 5
print(ha)

string = "What does the fox say?"
print(string.find("say")) # true, so prints 18

print("javi".find('i')) # true, so it prints 3
print("javi".find('b')) # false, so it prints -1
print("javi".find('vi')) # true, so it prints 2

ssh = 'PoRTstr22isTCp'
print(ssh)

print(ssh.lower())
print(ssh.upper())

# If we need to use qoutes or special characters in a string we can do that by using the '\' character
print("John\tCena")
print("Stone\nCold")
print("'Single' in a double")
print('"Double" in a single')
print("\"Double\" in a Double")
