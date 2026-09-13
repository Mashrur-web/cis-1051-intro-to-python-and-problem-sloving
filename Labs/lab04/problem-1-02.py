def multiplication_table(n):
    for i in range(1, n + 1):
        r = ""
        for j in range(1, n + 1):
            r = r + f"{i * j:5d}"
        print(r)


n = int(input("Enter a number less than 20: "))
multiplication_table(n)
