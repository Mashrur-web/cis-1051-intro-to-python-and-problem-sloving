def summation_of_squares(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i**2
    print(f"The sum of squares up to {n} = {sum}")


n = int(input("Enter a positive integer: "))
summation_of_squares(n)
