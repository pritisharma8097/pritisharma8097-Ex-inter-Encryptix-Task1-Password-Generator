import string
import random

def generate_password(length):
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    if length < 1:
        print("Password length must be at least 1")
        return None
    
    password = "".join(random.sample(s, length))
    return password

if __name__ == "__main__":
    while True:
        try:
            plen = int(input("Enter password length\n"))
            if plen <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer for password length.")

    password = generate_password(plen)
    if password:
        print("Your password is: ")
        print(password)
