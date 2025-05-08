import string 

def check_strength(password):
#takes a password as input and checks it strength
    length_error = len(password) < 8
    digit_error = not any(char.isdigit() for char in password)
    uppercase_error = not any(char.isupper() for char in password)
    lowercase_error = not any(char.islower() for char in password)
    symbol_error = not any(char in string.punctuation for char in password)

    errors = {
        'Too short (<8 characters)': length_error,
        'No digits': digit_error,
        'No uppercase letters': uppercase_error,
        'No lowercase letters': lowercase_error,
        'No special characters': symbol_error,
    }
    #stores in a boolean 

    failed = [msg for msg, failed in errors.items() if failed]
    #makes a list of failed checks

    if not failed:
        strength = "Strong 💪"
    elif len(failed) <= 2:
        strength = "Moderate ⚠️"
    else:
        strength = "Weak ❌"

    return strength, failed

if __name__ == "__main__":
    password = input("Enter your password to check: ")
    strength, issues = check_strength(password)

    print(f"\nPassword Strength: {strength}")
    if issues:
        print("Issues:")
        for issue in issues:
            print(f"- {issue}")
