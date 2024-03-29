import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '*', '+']

print ("Welcome to the password generator")
num_letters = int(input("How many letters would you like to have in your password?\n"))
num_numbers = int(input("How many numbers would you like to have in your password?\n"))
num_symbols = int(input("How many symbols would you like to have in your password?\n"))

random_password = []
for n in range (1,num_letters+1):
    random_password.append(random.choice (letters)) 
        
for n in range (1, num_numbers+1):
    random_password.append(random.choice (numbers))
    
for n in range (1, num_symbols+1):
    random_password.append(random.choice (symbols))
    
random.shuffle(random_password)
password = ""
for randpass in random_password:
    password += randpass

print(f"This is your new suggested password:\n {password}")
