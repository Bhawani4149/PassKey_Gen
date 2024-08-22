import random
print("I will generate a password according to your specifications")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nl= int(input("How many letters would you like in your password?\n")) 
ns= int(input(f"How many symbols would you like?\n"))
nn= int(input(f"How many numbers would you like?\n"))
s=""
for i in range(nl):
    s+=random.choice(letters)
for i in range(ns):
    s+=random.choice(symbols)
for i in range(nn):
    s+=random.choice(numbers)
print("Your easy password is "+s)
l=list(s)
pwd=""
random.shuffle(l)
for i in l:
    pwd+=i
print("Your Hard password is "+pwd)