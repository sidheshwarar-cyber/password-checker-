# Password Strength Checker
import string

password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1
if any(ch.isupper() for ch in password):
    score += 1
if any(ch.islower() for ch in password):
    score += 1
if any(ch.isdigit() for ch in password):
    score += 1
if any(ch in string.punctuation for ch in password):
    score += 1

if score <= 2:
    print("Password Strength: Weak")
    print("Feedback: Use at least 8 characters with uppercase, lowercase, numbers, and special characters.")
elif score <= 4:
    print("Password Strength: Medium")
    print("Feedback: Add the missing character types and use at least 8 characters.")
else:
    print("Password Strength: Strong")
    print("Feedback: Good password! Keep it private and do not reuse it.")
