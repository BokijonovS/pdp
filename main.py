# the x
symbol = input("Enter a symbol to draw the X: ")
size = 9

for i in range(size):
    for j in range(size):
        if j == i or j == size - 1 - i:
            print(symbol, end="")
        else:
            print(" ", end="")
    print()


# the tree
print('archa: ')

for i in range(1, size+1):
    print(" " * (size - i) + symbol * (2 * i - 1))
print(" " * (size - 1) + symbol)


# the z
shape = input("Enter a shape: ")
n = int(input("Enter a number (height of Z): "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == n - 1 - i:
            print(shape, end="")
        else:
            print(" ", end="")
    print()
