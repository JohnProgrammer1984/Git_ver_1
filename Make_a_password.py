import random
import time
chosen_range = random.choice([(10, 20), (50, 60)])

number = random.randint(chosen_range[0], chosen_range[1])

print("="*30)
print(" "*5,"PASSWORD CREATER"," "*5)
print("="*30)
length = int(input("Enter password length (atleast 8) >> "))
while length <8: length = int(input("Enter password length (atleast 8) >> "))
a = input("Include capital? Y/N >> ")
b = input("Include number? Y/N >> ")
c = input("Include symbol? Y/N >> ")
d = int(input("How many passwords? >> "))
password = ""
if a == "Y" or a == "y":
    capital = True
else: capital =False
if b == "Y" or b == "y":
    number = True
else: number = False
if c == "Y" or c == "y":
    symbol = True
else: symbol = False
password = ""






print(password)

sym = ( list(range(33, 48))+ list(range(58, 65))+ list(range(91, 97))+ list(range(123, 127)))


def makepass():
    password = ""
    counter = 0
    while counter < length:
        character = str(chr(random.randint(97,122)))
        password += character
        counter +=1
        if capital:
            character = str(chr(random.randint(65,90)))
            password += character
            counter +=1

        if number:
            character = str(chr(random.randint(48,57)))
            password += character
            counter +=1

        if symbol:
            character = str(chr(random.choice(sym)))
            password += character
            counter +=1
    return password

print("CREATING PASSWORD...")
print("-"*20)
print("")
time.sleep(2)

item = []

for i in range(d):
    generate = makepass()
    print("[",i+1,"]","  ",generate)
    item.append(generate)
    time.sleep(0.5)
    bar = 1
    if capital: bar +=1
    if symbol: bar +=3
    if number: bar+=2
    print("PASSWORD STRENGTH >> ","|","X"*bar,"|",)
    print("")
    time.sleep(1)


import datetime 

currenttime = datetime.datetime.now() 

timestamp = currenttime.strftime("%d-%m-%Y %H:%M:%S") 

#MAKE SURE THE FILE "passwords.txt" IS AVAILABLE

print("+"*10, "FILE SAVE","+"*10)
option = input("WANNA SAVE PASSWORD(s)? Y/N >> ").upper()
if option == "Y":
    file = open("passwords.txt","a")
    file.write(f"{timestamp}\n")
    for i in range(len(item)):
        file.write(f"{item[i]}\n")





