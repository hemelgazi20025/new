import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


ps_letters=int(input("How many letters do you want in your password? \n"))
ps_numbers=int(input("How many numbers do you want in your password? \n"))
ps_symbols=int(input("How many symbols do you want in your password? \n"))


password=""
for x in range(0,ps_letters//3):
  p1= random.choice(letters)
  password+= p1
# OR
# for x in range(0,ps_letters):
#     password+=random.choice(letters)
# print(password)


for x in range(0,ps_numbers//2):
    password+=random.choice(numbers)
    

for x in range(0,ps_letters//3):
    password+=random.choice(letters)
    

for x in range(0,ps_symbols//2):
   password+=random.choice(symbols)
   

for x in range(0,ps_numbers//2):
    password+=random.choice(numbers)


for x in range(0,ps_letters//3):
    password+=random.choice(letters)
    

for x in range(0,ps_numbers//2):
    password+=random.choice(symbols)
    

print(f"Your password could be: {password}")