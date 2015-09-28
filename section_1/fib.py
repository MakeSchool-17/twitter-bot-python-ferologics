nth = int(input("Please enter an integer: "))


def nth_fib(n):
    i = 0
    a, b = 0, 1

    while a < 9999999999999999999999999999999999999999999999999999999999999999:
        i += 1
        a, b = b, a+b

        if i == n:
            print(a)


def fib(n):
    a, b = 0, 1

    while a < n:
        print(a, end=" ")
        a, b = b, a+b
    print()

print("fib up to", nth)
fib(nth)

print(nth, "th fib")
nth_fib(nth)
