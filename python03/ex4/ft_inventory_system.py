import sys


def ft_inventory_system() -> None:
    """
    Parse command-line inventory items and generate analytics.

    The function reads arguments in the form "item:quantity",
    builds an inventory dictionary, and aggregates quantities
    for duplicate items.

    It then displays inventory statistics including total items,
    unique item types, percentage distribution, abundance
    classification, restock recommendations, and dictionary
    property demonstrations.
    """
    inventory: dict[str, int] = {}
    try:
        if len(sys.argv) < 2:
            raise ValueError("Too less args")
        total: int = 0

        for arg in sys.argv[1:]:
            result: list[str] = arg.split(":")
            if len(result) != 2:
                raise ValueError("Invalid argumment !")
            name, value = result
            qty: int = int(value)
            total += qty
            inventory[name] = inventory.get(name, 0) + qty

    except ValueError as e:
        print("Error:", e)
        return

    print("=== Inventory System Analysis ===")
    dict_len: int = len(inventory)
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {dict_len}")
    print("")

    print("=== Current Inventory ===")
    moderate: dict[str, int] = {}
    scarce: dict[str, int] = {}
    restock: list[str] = []
    flag: bool = True
    max_qty: int = 0
    min_qty: int = 0
    item_max: str | None = None
    item_min: str | None = None
    for name, value in inventory.items():
        print(f"{name}: {value} units ({(value * 100 / total):.1f}%)")
        if value >= 5:
            moderate[name] = value
        else:
            scarce[name] = value
        if value <= 1:
            restock.append(name)
        if flag:
            flag = False
            max_qty = value
            min_qty = value
            item_max = name
            item_min = name
        else:
            if max_qty < value:
                max_qty = value
                item_max = name
            if min_qty > value:
                min_qty = value
                item_min = name

    print("")
    print("=== Inventory Statistics ===")
    print(f"Most abundant: {item_max} ({max_qty} units)")
    print(f"Least abundant: {item_min} ({min_qty} units)")
    print("")

    print("=== Item Categories ===")
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("")
    print("=== Management Suggestions ===")
    print(f"Restock needed: {restock}")
    print("")

    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys: ", end="")
    flag: int = False
    for key in inventory.keys():
        if flag:
            print(", ", end="")
        print(key, end="")
        flag = True

    flag = False
    print("")
    print("Dictionary values: ", end="")
    for value in inventory.values():
        if flag:
            print(", ", end="")
        print(value, end="")
        flag = True
    print("")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    ft_inventory_system()
