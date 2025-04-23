import colorama 
from colorama import Fore 
colorama.init(autoreset=True)

print(Fore.LIGHTBLUE_EX + """

████████╗██╗░░██╗███████╗  ░██████╗███╗░░██╗░█████╗░░█████╗░██╗░░██╗  ░██████╗████████╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
╚══██╔══╝██║░░██║██╔════╝  ██╔════╝████╗░██║██╔══██╗██╔══██╗██║░██╔╝  ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
░░░██║░░░███████║█████╗░░  ╚█████╗░██╔██╗██║███████║██║░░╚═╝█████═╝░  ╚█████╗░░░░██║░░░███████║░░░██║░░░██║██║░░██║██╔██╗██║
░░░██║░░░██╔══██║██╔══╝░░  ░╚═══██╗██║╚████║██╔══██║██║░░██╗██╔═██╗░  ░╚═══██╗░░░██║░░░██╔══██║░░░██║░░░██║██║░░██║██║╚████║
░░░██║░░░██║░░██║███████╗  ██████╔╝██║░╚███║██║░░██║╚█████╔╝██║░╚██╗  ██████╔╝░░░██║░░░██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═════╝░╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝""")

print("Press 'Enter' key to start the vending machine")
input()
 
stock = { Fore.LIGHTWHITE_EX +
    """𝐒𝐍𝐀𝐂𝐊𝐒""": {
        1: {"name": "Lays Classic", "price": 1.50, "stock": 5},
        2: {"name": "Doritos", "price": 2.00, "stock": 4},
        3: {"name": "Oreo", "price": 1.75, "stock": 6},
        4: {"name": "Cheetos", "price": 2.25, "stock": 0},
        5: {"name": "M&Ms", "price": 4.75, "stock": 10}
    }, Fore.LIGHTWHITE_EX +
    """𝐃𝐑𝐈𝐍𝐊𝐒""": {
        6: {"name": "Coke", "price": 2.00, "stock": 5},
        7: {"name": "Fanta", "price": 2.00, "stock": 2},
        8: {"name": "Water", "price": 1.00, "stock": 3},
        9: {"name": "Sprite", "price": 1.00, "stock": 6},
        10: {"name": "Tea", "price": 1.00, "stock": 4}
    },
    """𝐃𝐄𝐒𝐒𝐄𝐑𝐓""": {
        11: {"name": "Chocolate Bar", "price": 2.50, "stock": 4},
        12: {"name": "Brownie", "price": 3.00, "stock": 5},
        13: {"name": "Cupcake", "price": 2.75, "stock": 6}
    }
}

def show_main_menu():
    print(Fore.LIGHTWHITE_EX + "\n" """
░█──░█ ░█▀▀▀ ░█▄─░█ ░█▀▀▄ ▀█▀ ░█▄─░█ ░█▀▀█ 　 ░█▄─░█ ─█▀▀█ ░█▀▀█ ░█─░█ ▀█▀ ░█▄─░█ ░█▀▀▀ 　 ░█▀▄▀█ ░█▀▀▀ ░█▄─░█ ░█─░█ 
─░█░█─ ░█▀▀▀ ░█░█░█ ░█─░█ ░█─ ░█░█░█ ░█─▄▄ 　 ░█░█░█ ░█▄▄█ ░█─── ░█▀▀█ ░█─ ░█░█░█ ░█▀▀▀ 　 ░█░█░█ ░█▀▀▀ ░█░█░█ ░█─░█ 
──▀▄▀─ ░█▄▄▄ ░█──▀█ ░█▄▄▀ ▄█▄ ░█──▀█ ░█▄▄█ 　 ░█──▀█ ░█─░█ ░█▄▄█ ░█─░█ ▄█▄ ░█──▀█ ░█▄▄▄ 　 ░█──░█ ░█▄▄▄ ░█──▀█ ─▀▄▄▀ """)
    for i, cat in enumerate(stock.keys(), 1):
        print(f"{i}. {cat}")
    print(Fore.LIGHTWHITE_EX + "0. " """𝐂𝐇𝐄𝐂𝐊𝐎𝐔𝐓""")

def show_items(category):
    print(f"\n----------------- {category} -----------------")
    print(f"{'No.':<5}{'Item':<20}{'Price':>8}{'Stock':>8}")
    print("------------------------------------------")
    for num, item in stock[category].items():
        print(f"{num:<5}{item['name']:<20}{item['price']:>8.2f}{item['stock']:>8}")
    print("------------------------------------------")

def get_item(num):
    for items in stock.values():
        if num in items:
            return items[num]
    return None

def buy():
    cart = []
    total = 0.0
    categories = list(stock.keys())

    while True:
        show_main_menu()
        try:
            choice = int(input("Choose category (0 to checkout): "))
            if choice == 0:
                break
            if 1 <= choice <= len(categories):
                category = categories[choice - 1]
                show_items(category)
                item_num = int(input("Enter item number: "))

                if item_num not in stock[category]:
                    print("Invalid number entered.")
                    continue

                item = stock[category][item_num]

                if item["stock"] == 0:
                    print("Out of stock.")
                    continue

                qty = int(input(f"Quantity of {item['name']}: "))
                if qty > item["stock"]:
                    print(f"Only {item['stock']} available.")
                    continue

                cost = item["price"] * qty
                total += cost
                item["stock"] -= qty
                cart.append((item["name"], qty, cost))
            else:
                print("Invalid category.")
        except ValueError:
            print("Enter numbers only.")

    if cart:
        pay(cart, total)
    else:
        print("No items purchased.")

def pay(cart, total):
    print(Fore.LIGHTBLUE_EX + "\n" """Ｃａｒｔ：""")
    print("____________________________")
    for name, qty, cost in cart:
        print(f"{qty} x {name} = {cost:.2f} AED")
    print("____________________________")
    print(f"Total: {total:.2f} AED")

    method = input("\nPayment method:\n1. Cash\n2. Card\nChoose (1/2): ")

    if method == "1":
        print("\n\nAccepted: 1, 5, 10, 20, 50 AED\n")
        inserted = 0.0
        while inserted < total:
            try:
                bill = float(input(f"Insert cash (inserted: {inserted:.2f}): "))
                if bill in [1, 5, 10, 20, 50]:
                    inserted += bill
                else:
                    print("Invalid bill.")
            except ValueError:
                print("Invalid input.")

        change = inserted - total
        if change > 0:
            print(f"Take your change: {change:.2f} AED")

    elif method == "2":
        pin = input("Enter 4-digit PIN: ")
        if pin.isdigit() and len(pin) == 4:
            print("Processing...\nPayment approved.")
        else:
            print("Invalid PIN. Payment failed.")
            return
    else:
        print("Invalid payment method.")
        return

    print("\n\n 𝒯𝒽𝒶𝓃𝓀 𝓎ℴ𝓊 𝒻ℴ𝓇 𝓎ℴ𝓊𝓇 𝓅𝓊𝓇𝒸𝒽𝒶𝓈ℯ! ")

buy()