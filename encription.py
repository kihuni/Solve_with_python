# receive input from the user
message = input("input a string here...")
# receive key or number of times to shift the character
key = int(input("input a number in range of 1-26..."))
secret_string = ""

# iterate through the given string
for char in message:
    # check if the input is a number is its leave it as its

    if char.isalpha():
        char_code = ord(char)
        char_code += key

# check if the number is uppercase minus it 26
if char.isupper():
    if char_code > ord("Z"):
        char_code -= 26
# if lowercase
    if char_code < ord("A"):
        char_code += 26
else:
    if char_code > ord("z"):
        char_code -= 26
        # if lowercase
    if char_code < ord("a"):
        char_code += 26
secret_string += chr(char_code)


key = -key

orig_message = ""
# iterate through the given string
for char in secret_string:
    # check if the input is a number is its leave it as its

    if char.isalpha():
        char_code = ord(char)
        char_code += key

# check if the number is uppercase minus it 26
if char.isupper():
    if char_code > ord("Z"):
        char_code -= 26
# if lowercase
    if char_code < ord("A"):
        char_code += 26
else:
    if char_code > ord("z"):
        char_code -= 26
        # if lowercase
    if char_code < ord("a"):
        char_code += 26
orig_message += chr(char_code)

print("Decrypt:", secret_string)
print("encrypt:", orig_message)

