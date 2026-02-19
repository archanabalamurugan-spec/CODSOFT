import random
import string

length = int(input("Enter password length: "))

use_letters = input("Include letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

characters = ""

if use_letters:
    characters += string.ascii_letters
if use_digits:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

if characters == "":
    print("You must select at least one option!")
else:
    password = "".join(random.choice(characters) for _ in range(length))
    print("Generated Password:", password)
