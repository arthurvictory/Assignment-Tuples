orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Arthur", "Desktop", 1),
    ("James", "Graphics Card", 2)
]

def format_orders(orders):
    for index, (name, order, quantity) in enumerate(orders):
        print(f"Order {index + 1}: {name} has ordered {quantity} {order}")

format_orders(orders)