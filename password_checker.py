import re
import hashlib


def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add a number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add a special character")

    return score, feedback


def hash_password(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

password = input("Enter your password: ")

strength, feedback = check_password_strength(password)
hashed_password = hash_password(password)

if strength <= 2:
    print("Password Strength: WEAK")
elif strength <= 4:
    print("Password Strength: MEDIUM")
else:
    print("Password Strength: STRONG")

print("\nHashed Password (stored securely):")
print(hashed_password)

if feedback:
    print("\nSuggestions to improve your password:")
    for tip in feedback:
        print("-", tip)
