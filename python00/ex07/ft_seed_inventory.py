
def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    if (unit == "packets"):
        print(f"{seed_type} seeds: {quantity} packets available")
    elif (unit == "grams"):
        print(f"{seed_type} seeds: {quantity} packets total")
    elif (unit == "area"):
        print(f"{seed_type} seeds: {quantity} packets meters")
    else:
        print("Unknown unit tquantity")

