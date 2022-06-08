# creating a # tree


# get the number of the tree
tree_height = input("how tall is the tree : ")

# convert into integers
tree_height = int(tree_height)

# get the starting space for the top of the tree
spaces = tree_height - 1

# initial hash
hashes = 1

# stump spaces
stump_spaces = tree_height - 1

# while loop to iterate through the user input
while tree_height != 0:

    # print the spaces
    for i in range(spaces):
        print(' ', end="")

    # print the hashes
    for i in range(hashes):
        print('#', end="")

    # Decrement spaces by 1 each time
    spaces -= 1

    # increments the hashes by 2 each time
    hashes += 2

    # Decrement the tree height each time to jump out of the loop
    tree_height -= 1

    # print the spaces before the stump and the hash
    for i in range(stump_spaces):
        print(' ', end="")

    print("#")
