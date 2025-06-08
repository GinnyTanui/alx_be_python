def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit") 

def main():
    shopping_list = ["Apples", "Bananas", "Carrots"]  # Initial shopping list
    print("Welcome to the Shopping List Manager!")
    while True:
        display_menu() 
        choice = input("Enter your choice: ") 
        if choice == "1":
            item = input("Enter an item you want to add:") 
            shopping_list.append(item) 
            print(f"item '{item}' added to the shopping list.")
        elif choice == "2":
            item = input("Enter an item you want to remove:") 
            if item in shopping_list:
                shopping_list.remove(item) 
                print(f"item '{item}' removed from the shopping list.")
            else:
                print(f"item '{item}' not found in the shopping list.")
        elif choice == "3":
            print("Shopping List:")
            for idx, item in enumerate(shopping_list, start=1):
                print(f"{idx}. {item}")
        elif choice == "4":
            print("Exiting Shopping List Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()