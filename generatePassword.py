#password generator using python

import string
import random

def generate_password(length):
    
    #define all letters for using in password
    letters = string.ascii_letters 
    #define digits
    digits = string.digits 
    #define special caharcters
    S_char = string.punctuation
    choosing_list = string.ascii_letters + string.digits + string.punctuation
    
    #taking an specific length for password
    if length <= 0:
        print("Password length should be at least 6 characters.")
        return None

    password = ''.join(random.choice(choosing_list)for i in range(length))
    return password

length = int(input("Enter password length: "))
print("Generated Password : ", generate_password(length))