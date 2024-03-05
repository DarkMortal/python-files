import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_characters = string.punctuation
character_list = letters + digits + special_characters

def generatePassword(length: int) -> str:
    password = []
    for i in range(length):
        password.append(secrets.choice(character_list))
    return "".join(password)

if __name__ == "__main__":
    print(f"Generated password: {generatePassword(int(input('Enter length of password: ')))}")