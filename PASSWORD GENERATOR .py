8import random
import string

def generate_password(length):
    if length < 1:
        print("Password length should be at least 1.")
        return
    
    # Define the character sets to choose from
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all the character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    password = generate_password(length)
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
