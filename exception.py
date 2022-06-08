# What is required:
# Enter a string to hide in uppercase: HIDE
# print the secret message : 23134311
# print the origin message: HIDE

# INPUT BY THE USER
userInput = input("Enter your secret key here:..")

secret_string = ""

# cycle through each character in the string
for char in userInput:
    # store each character code in a new string
    secret_string += str(ord(char))

print("secret Message :", secret_string)

# CONVERTING BACK TO STRING
secret_string = ''
for i in range(0, len(secret_string)-1, 2):
    char_code = secret_string[i] + secret_string[i+1]
    userInput += chr(int(char_code))
    print("Original String :", userInput)

