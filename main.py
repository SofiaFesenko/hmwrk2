# number 1

x = int(input('enter x'))
y = int(input('enter y'))
a = print('choose: 1. Addition, 2. Subtraction, 3. Multiply, 4. Divide, 5. Exit')
choice = int(input("Enter choice:"))

sum_func = lambda x, y: print(x + y)
sub_func = lambda x, y: print(x - y)
multiply_func = lambda x, y: print(x * y)
divide_func = lambda x, y: print(x / y)

def check():
    if choice == 1:
        sum_func(x, y)
    elif choice == 2:
        sub_func(x, y)
    elif choice == 3:
        multiply_func(x, y)
    elif choice == 4:
        if y == 0:
            print('you can`t do it')
        else:
            divide_func(x, y)
    else:
        exit()

check()

# number 2

x = int(input())

def generator(x):
    print(x**3)

generator(x)

# number 3

def time_func(func):
    import time

    start = time.time()
    func()
    end = time.time()
    print(end - start)


@time_func
def func():
    x = 23
    y = 7
    c = x**y + y - x*78
    d = y**x - c
    print(d)
    # взагалі тут можна будь що напипсати, але я не знала що придумати, тому просто приклади :|

func()
