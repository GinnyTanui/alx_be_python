size = int(input("Enter the size of the pattern: "))

# This code draws a square pattern of asterisks based on the user-defined size.
row = 0
while row < size:
    for col in range(size):
        print("*", end="")  # print asterisks side-by-side
    print()  # move to the next line after a row is printed
    row += 1  # go to the next row
