# Printing out the squares of numbers 1 to 10.

squares = []
for number in range(1,11):
    squares.append(number**2)

print(squares)

# Another more efficient way:

squares = [value**2 for value in range(1,11)]
print(squares)
