def first():
    """this function prints x using the shape and size given by user"""
    symbol = input("Enter a symbol to draw the X: ")
    size = int(input("Enter size: "))

    for i in range(size):
        for j in range(size):
            if j == i or j == size - 1 - i:
                print(symbol, end="")
            else:
                print(" ", end="")
        print()

# ==============================================================================================
def second():
    '''this function is for printing a tree using user's symbols and size'''
    symbol = input("Enter a symbol to draw the X: ")
    size = int(input("Enter size: "))
    print('archa: ')

    for i in range(1, size+1):
        print(" " * (size - i) + symbol * (2 * i - 1))
    print(" " * (size - 1) + symbol)

# ==============================================================================================

def third():
    '''this function is for printing the shape z using symbols and size that user gave'''
    shape = input("Enter a shape: ")
    n = int(input("Enter a number (height of Z): "))

    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == n - 1 - i:
                print(shape, end="")
            else:
                print(" ", end="")
        print()

# ==============================================================================================
def fifth():
    a = 'I am a PDP student!'
    print(a)
    student = 'Akbar'
    print(student)
    student = 'Akobir'
    print(student)
    print(len(a + student))

# ==============================================================================================

# hw

def sixth():
    num = int(input('enter a number: '))
    fl = float(input('enter a float: '))
    while True:
        print('Do u wanna add these nums? yes/no: ')
        res = input()
        if res == 'yes':
            print(float(num) + fl)
            break
        elif res == 'no':
            if float(num) > fl:
                print(float(num) - fl)
                break
            else:
                print(fl - float(num))
                break
        else:
            print('you didnt type yes or no, try again')


# ==============================================================================================

def seventh():
    fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    fruits.pop(1)
    fruits.pop(2)
    print(fruits)

# ==============================================================================================

def eighth():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = list(filter(lambda x : x % 2 == 1, numbers))
    print(res)

# ==============================================================================================

def nineth():
    my_list = [10, 20, 30, 40, 50, 60, 70, 80]
    del my_list[3:5]
    print(my_list)


# ==============================================================================================

def tenth():
    cities = ['New york', 'London', 'Tokyo', 'Moscow', 'Paris']
    del cities[2]
    print(cities)


# ==============================================================================================

def eleventh():
    nums = [5, 10, 15, 20, 25]
    nums.pop(0)
    nums.pop(-1)
    print(nums)
eleventh()

# ==============================================================================================

def twelveth():
    fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    fruits = [fruits.pop(1)]
    print(fruits)

twelveth()

# ==============================================================================================

def thirteenth():
    items = [1, 2, 3, 4, 5]
    del items[0::]
    print(items)
thirteenth()


# ==============================================================================================

def fourteenth():
    cars = ['Toyota', 'Ford', 'BMW', 'Audi']
    cars.append(cars.pop(0))
    print(cars)

fourteenth()

# ==============================================================================================

def fifteenth():
    numbers = [1, 2, 3, 4, 5]
    numbers.reverse()
    print(numbers)
fifteenth()

# efvd












