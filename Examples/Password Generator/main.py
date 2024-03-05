from generator import generatePassword

if __name__ == "__main__":
    print(f"Generated password: {generatePassword(int(input('Enter length of password: ')))}")