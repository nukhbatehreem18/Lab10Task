def show_menu():
    menu = {
        1: ("Espresso", 350),
        2: ("Cappuccino", 480),
        3: ("Latte", 500),
        4: ("Americano", 400),
    }
    print("\n--- Welcome to Coffee Shop ---")
    for code, (name, price) in menu.items():
        print(f"{code}. {name} - Rs. {price}")
    return menu


def take_order(menu):
    order_items = []
    while True:
        choice = input("\nEnter item number (or 'done' to finish): ").strip().lower()
        if choice == "done":
            break
        if not choice.isdigit() or int(choice) not in menu:
            print("Invalid choice. Please try again.")
            continue

        qty_input = input("Enter quantity: ").strip()
        if not qty_input.isdigit() or int(qty_input) <= 0:
            print("Quantity must be a positive number.")
            continue

        item_name, price = menu[int(choice)]
        qty = int(qty_input)
        order_items.append((item_name, price, qty))
        print(f"Added {qty} x {item_name}")

    return order_items


def print_receipt(order_items):
    if not order_items:
        print("\nNo items ordered. Thank you!")
        return

    print("\n--- Order Summary ---")
    subtotal = 0
    for name, price, qty in order_items:
        line_total = price * qty
        subtotal += line_total
        print(f"{name} x {qty} = Rs. {line_total}")

    print(f"Total Bill: Rs. {subtotal}")
    print("Thank you for visiting!")


def main():
    menu = show_menu()
    order_items = take_order(menu)
    print_receipt(order_items)


if __name__ == "__main__":
    main()
