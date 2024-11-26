import random
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ['1','2','3','4','5','6','7','8','9',"10"]
symbols = ['@',"#","$","%","+","!",("*"),"&"]
print("Welcome to password genetor")
n_letter =int(input("How many letters you want in your password"))
n_symbol=int(input("How many symbols you want in your password"))
n_numbers =int(input("How many numbers you want in your password"))
password="4"
for i in range(1,n_letter+1):
    char = random.choice(letters)
    password+=char

for i in range(1,n_symbol+1):
    char = random.choice(numbers)
    password+=char

for i in range(1,n_numbers+1):
    char = random.choice(symbols)
    password+=char
print(password)
    