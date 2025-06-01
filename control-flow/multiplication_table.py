number = int(input("Enter a number to see its multiplication table: "))

# Loop to print the table
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Final message
print(f"\nThat's the multiplication table for {number}. Hope it helps!")
