def prime(n):
    isprime = True
    for x in range(2, n):
        if n % x == 0:
            isprime = False
    if isprime:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")


print("Welcome to PrimeFind")
number = int(input("Enter a number: "))

prime(n=number)
