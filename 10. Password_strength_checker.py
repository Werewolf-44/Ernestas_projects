# This program checks if the password meets requirements for a strong password. 

import hashlib
import requests

# Password Complexity Rules:
#   Minimum length (e.g., 8+ characters).
#   Requires uppercase, lowercase, numbers, and special characters.
#   Bans common passwords (e.g., "password123").

def check_complexity(password):
    # Check length
    length_ok = len(password) >= 8

    # Check for uppercase, lowercase, digits, and special characters
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_=+[]{};:,.<>?/" for c in password)

    #Score calculation
    score = 0
    if length_ok: score += 1
    if has_upper: score += 1
    if has_lower: score += 1
    if has_digit: score += 1
    if has_special: score += 1

    #Feedback
    if score == 5:
        return "Strong password"
    elif score == 4:
        return "Moderate password"
    elif score <= 3:
        return "Weak password"

def check_breached(password):
    # Has the password (SHA-1, uppercase)
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    # Call HIBP's range API (k-Anonymity)
    # to check if the password is in the database
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    # Check if suffix is in the response
    hashes = [line.split(':') for line in response.text.splitlines()]
    for h, count in hashes:
        if h == suffix:
            return int(count) #Number of timees the password was breached
    return 0 #Not breached

#Combine both Checks
def evaluate_password(password):
    #check complexity
    complexity = check_complexity(password)
    print(f"Complexity: {complexity}")

    #Check breaches
    breach_count = check_breached(password)
    if breach_count > 0:
        print(f"Password has been breahced {breach_count} times!")
    else:
        print("Password has not been breached.")

if __name__ == "__main__":
    user_password = input("Enter a password to check: ")
    evaluate_password(user_password)