"""Inventory management system for tracking stock items and quantities."""

import json


stock_data = {}


def add_item(item, qty, logs=None):
    """
    Add an item to the inventory with specified quantity.

    Args:
        item: Name of the item to add
        qty: Quantity of the item
        logs: Optional list to append operation logs
    """
    if logs is None:
        logs = []
    stock_data[item] = qty
    logs.append(f"Added {item}")
    print(f"Added {item} with quantity {qty}")


def remove_item(item):
    """
    Remove an item from the inventory.

    Args:
        item: Name of the item to remove
    """
    try:
        if item in stock_data:
            del stock_data[item]
    except KeyError as e:
        print(f"Error removing item: {e}")


def get_qty(item):
    """
    Get the quantity of a specific item.

    Args:
        item: Name of the item

    Returns:
        Quantity of the item or 0 if not found
    """
    return stock_data.get(item, 0)


def load_data(filename):
    """
    Load inventory data from a JSON file.

    Args:
        filename: Path to the JSON file to load

    Returns:
        dict: The loaded inventory data
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {filename} not found. "
              "Starting with empty inventory.")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filename}. "
              "Starting with empty inventory.")
        return {}


def save_data(filename):
    """
    Save inventory data to a JSON file.

    Args:
        filename: Path to the JSON file to save
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(stock_data, f)


def print_data():
    """Print all items in the inventory."""
    for item, qty in stock_data.items():
        print(f"{item}: {qty}")


def check_low_items(threshold=5):
    """
    Check and print items below a quantity threshold.

    Args:
        threshold: Minimum quantity threshold (default: 5)
    """
    for item, qty in stock_data.items():
        if qty < threshold:
            print(f"Low stock: {item} ({qty})")


def main():
    """Main function to demonstrate inventory system functionality."""
    # Load existing inventory data
    loaded_data = load_data("inventory.json")
    if loaded_data:
        stock_data.update(loaded_data)
    add_item("apple", 10)
    add_item("banana", 3)
    print_data()
    save_data("inventory.json")
    print("Inventory system demonstration complete")


if __name__ == "__main__":
    main()
