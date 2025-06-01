number = int(input("Enter a number to see its multiplication table: "))

# Introduction line
print(f"\nMultiplication Table for {number}:\n")

# Loop to print the table
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
