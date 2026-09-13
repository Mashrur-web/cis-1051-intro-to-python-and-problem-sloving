def bottles_of_beer(n):
    for i in range(n, 0, -1):
        print("bottles of beer on the wall", i, "bottles of beer")
        print("Take one down, pass it around", (i - 1), "bottles of beer on the wall")


n = int(input("Enter the numer of bottles: "))
bottles_of_beer(n)
