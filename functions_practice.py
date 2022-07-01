"""
To-Do's:

1. A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.
2. A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.
3. A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". The function should not return anything.

"""
# Function 1
def hello():
    print('Welcome to my function, Time to party!')

# Function 2
def pack(item_1, item_2, item_3):
    return [item_1, item_2, item_3]

# Function 3
def eat_lunch(*foods):
    if(not foods):
        print('My lunchbox is empty!')
    elif(len(foods)>0):
        print(f'First i eat {foods[0]}.')
        i = 1
        while(i < len(foods)):
            print(f'Next i eat {foods[i]}.')
            i+=1

hello()
print('-----------------------------')
# Test with string
print(pack('one', 'two', 'three'))
print('-----------------------------')
# Test with Integers
print(pack(1, 2, 3))
print('-----------------------------')

# Test function with no arguments
eat_lunch()
print('-----------------------------')
# Test function with one argument
eat_lunch('apple')
print('-----------------------------')
# Test function with many arguments
eat_lunch('apple', 'bananas', 'oranges')
print('-----------------------------')

