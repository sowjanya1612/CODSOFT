import random
import string

def generate_password():
    print("===== PASSWORD GENERATOR =====")
    
    try:
        length = int(input("Enter the desired password length: "))
        
        if length <= 0:
            print("Password length must be greater than 0")
            return
        
        # Characters to use in password
        characters = string.ascii_letters + string.digits + string.punctuation
        
        password = "".join(random.choice(characters) for _ in range(length))
        
        print("\nGenerated Password:")
        print(password)
    
    except ValueError:
        print("Please enter a valid number")

generate_password()
