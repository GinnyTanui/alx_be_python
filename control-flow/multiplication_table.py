operation = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    print(f"{operation} * {i} = {operation * i}")

print(f"\nThat's the multiplication table for {operation}. Hope it helps!")
