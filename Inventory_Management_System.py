# Sample initial inventory data (item_id: [name, quantity, price])
inventory = {}

# Sample initial user data (username: password)
users = {
    'admin': 'adminpass'
}


def register_user(username, password):
    if username in users:
        print("Username already exists. Please choose a different username.")
    else:
        users[username] = password
        print("Registration successful. You can now log in.")


def login_user(username, password):
    if username in users and users[username] == password:
        print(f"Welcome, {username}!")
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False


def add_item(item_id, name, quantity, price):
    if item_id in inventory:
        print("Item with this ID already exists. Please use a different ID.")
    else:
        inventory[item_id] = [name, quantity, price]
        print(f"Item '{name}' added to inventory.")


def delete_item(item_id):
    if item_id in inventory:
        item_name = inventory[item_id][0]
        del inventory[item_id]
        print(f"Item '{item_name}' deleted from inventory.")
    else:
        print("Item with this ID does not exist.")


def purchase_item(item_id, quantity):
    if item_id in inventory:
        item_name, available_quantity, price = inventory[item_id]
        if available_quantity >= quantity:
            inventory[item_id][1] -= quantity
            total_cost = price * quantity
            print(f"Purchase successful. Total cost: {total_cost}")
        else:
            print("Insufficient quantity in stock.")
    else:
        print("Item with this ID does not exist.")


def main():
    print("Welcome to Inventory Management System")
    while True:
        print("\nOptions:")
        print("1. Register")
        print("2. Login")
        choice = int(input("Enter your choice (1/2): "))
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if choice == 1:
            register_user(username, password)
            continue

        if login_user(username, password):
            while True:
                print("\nOptions:")
                print("1. Add Item to Inventory")
                print("2. Delete Item from Inventory")
                print("3. Purchase Item")
                print("4. Logout")
                choice = int(input("Enter your choice (1/2/3/4): "))

                if choice == 1:
                    item_id = int(input("Enter Item ID: "))
                    name = input("Enter Item Name: ")
                    quantity = int(input("Enter Quantity: "))
                    price = float(input("Enter Price: "))
                    add_item(item_id, name, quantity, price)

                elif choice == 2:
                    item_id = int(input("Enter Item ID to delete: "))
                    delete_item(item_id)

                elif choice == 3:
                    item_id = int(input("Enter Item ID to purchase: "))
                    quantity = int(input("Enter Quantity to purchase: "))
                    purchase_item(item_id, quantity)

                elif choice == 4:
                    print("Logged out successfully.")
                    break

                else:
                    print("Invalid choice. Please try again.")

        break


if __name__ == "__main__":
    main()
