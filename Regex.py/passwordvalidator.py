import re

def password_strength(password):
    if len(password) < 8:
        return 'Too short'
    elif re.search(r'[0-9]', password) is None:
        return 'Weak'
    elif re.search(r'[a-z]', password) is None or re.search(r'[A-Z]', password) is None:
        return 'Weak'
    elif re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is None:
        return 'Weak'
    else:
        return 'Strong'

password = input("Enter a password: ")
print("Password Strength:", password_strength(password))
