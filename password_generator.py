import random
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', '`', '~', ',', ':', ';', '.', '<', '>', '?', '/', '"',]

print("Welcome to the password generator!")
a=int(input("How many letters would you want: "))
b=int(input("How many numbers would you like: "))
c=int(input("How many symbols would you want: "))

password= ""
for i in range(1, a+1):
    char=random.choice(letters)
    password=password+char+" "

for i in range(1, b+1):
    num=random.choice(numbers)
    password=password+num+" "
for i in range(1, c+1):
    sym = random.choice(symbols)
    password=password+sym+" "
    
    
new_password=password.split()
d=len(new_password)
e=""
for i in range(1,d+1):
    passkey=random.choice(new_password)
    e=e+passkey
    
print(f"Your password is: {e}")
