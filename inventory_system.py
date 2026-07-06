# Inventory System

def main():
    inventory = {
        "apple": 5,
        "banana": 3,
        "orange": 8
    }

    while True:
        print("\nInventory Menu")
        print("1. Show all items")
        print("2. Add new item")
        print("3. Update item quantity")
        print("4. Show total quantity")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_items(inventory)
        elif choice == "2":
            add_item(inventory)
        elif choice == "3":
            update_item(inventory)
        elif choice == "4":
            show_total(inventory)
        elif choice == "5":
            print("See you next time!")
            break
        else:
            print("Please choose a valid option.")


def show_items(inventory):
    for item, quantity in inventory.items():
        print(f"{item.title()}: {quantity}")


def add_item(inventory):
    item = input("Item name: ").strip().lower()

    try:
        quantity = int(input("Quantity: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if quantity < 0:
        print("Quantity cannot be negative.")
        return

    inventory[item] = quantity
    print(f"Got it! {item.title()} has been added.")


def update_item(inventory):
    item = input("Which item do you want to update? ").strip().lower()

    if item not in inventory:
        print("Sorry, item not found.")
        return

    try:
        quantity = int(input("New quantity: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if quantity < 0:
        print("Quantity cannot be negative.")
        return

    inventory[item] = quantity
    print(f"Quantity of {item.title()} has been updated to {quantity}.")


def show_total(inventory):
    total = 0
    for quantity in inventory.values():
        total += quantity

    print(f"Total quantity: {total}")


main()