import string
import random

def generate_password(length=16):
    
    characters = string.ascii_letters + string.digits
       

    password = ''.join(random.choice(characters) for _ in range(length))
   
    return password

#Key Lenght
print(generate_password(8))




