number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")

print(f"\nThat's the multiplication table for {number}. Hope it helps!")
