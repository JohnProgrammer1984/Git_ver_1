import random

#1
roll = random.randint(1,6)
print("Ban da ra duoc so: ", roll)

#2
name = input("Input Name: ")
select = name[random.randint(0,len(name)-1)]
print("Selected random character is: ",select)

#3
Adjective = ["Awesome", "Mad", "Intelligent", "Gleeous"]
Object = ["Pelican", "Eagle", "Agent", "Programmer"]
print(Adjective[random.randint(0,len(Adjective)-1)],Object[random.randint(0,len(Object)-1)])

#4
Password = ""
for i in range(0,4):
    Number = str(random.randint(0,9))
    Password = Password + Number
print("Your new password is >> ",Password)

#5
length = int(input("Enter a length >> "))
password = ""
for i in range(length):
    newcharacter = chr(random.randint(97,122))
    password += newcharacter
print(password)

#6
sentence = input("Enter a sentence >> ")
mixed = sentence.split()
random.shuffle(mixed)
for i in range(len(mixed)):
    print(mixed[i], end=" ")