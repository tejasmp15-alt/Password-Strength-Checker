import re

def password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1

    if re.search("[A-Z]", password):
        strength += 1

    if re.search("[a-z]", password):
        strength += 1

    if re.search("[0-9]", password):
        strength += 1

    if re.search("[!@#$%^&*()_+=<>?/{}~]", password):
        strength += 1

    if strength == 5:
        return "Strong Password"
    elif strength >= 3:
        return "Medium Password"
    else:
        return "Weak Password"

password = input("Enter Password: ")
print("Password Strength:", password_strength(password))
