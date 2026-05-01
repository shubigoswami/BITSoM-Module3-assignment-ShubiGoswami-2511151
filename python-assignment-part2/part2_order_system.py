## PART2 : DATA STRUCTURES

#Raw Data 

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

# Task 1. Menue Printed Grouped by Category

# 1. Get unique categories
categories = set(item["category"] for item in menu.values())

for category in categories:
    print(f"\n===== {category} =====")
    
    for name, details in menu.items():
        if details["category"] == category:
            status = "Available" if details["available"] else "Unavailable"
            print(f"{name:<15} ₹{details['price']:.2f}   [{status}]")

#2.
# 
#  Total Number of Items

total_items = len(menu)
print("\nTotal items on menu:", total_items)


# Total Available Items

available_items = sum(1 for item in menu.values() if item["available"])
print("Total available items:", available_items)

#Most Expensive Item

most_expensive = max(menu.items(), key=lambda x: x[1]["price"])
print(f"Most expensive item: {most_expensive[0]} (₹{most_expensive[1]['price']:.2f})")


# Items Priced Under ₹150

print("\nItems under ₹150:")
for name, details in menu.items():
    if details["price"] < 150:
        print(f"{name} - ₹{details['price']:.2f}")


# Task 2 — Cart Operations

cart = []

# Add item
def add_to_cart(item_name, quantity):
    # Check if item exists
    if item_name not in menu:
        print(f"{item_name} does not exist in menu.")
        return
    
 # Check the availability
    if not menu[item_name]["available"]:
        print(f"{item_name} is currently unavailable.")
        return
    
 # Check if in cart
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] += quantity
            print(f"Updated {item_name} quantity to {item['quantity']}")
            return
    
 # Add new item
    cart.append({
        "item": item_name,
        "quantity": quantity,
        "price": menu[item_name]["price"]
    })
    print(f"Added {item_name} x{quantity} to cart")


# Remove item
def remove_from_cart(item_name):
    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print(f"Removed {item_name} from cart")
            return
    print(f"{item_name} not found in cart.")


# Print cart
def print_cart():
    print("\nCurrent Cart:")
    if not cart:
        print("Cart is empty.")
        return
    
    for item in cart:
        print(f"{item['item']} x{item['quantity']} (₹{item['price']})")


# ------
# SIMULATION :
# ------

add_to_cart("Paneer Tikka", 2)
print_cart()

add_to_cart("Gulab Jamun", 1)
print_cart()

add_to_cart("Paneer Tikka", 1)  # should update
print_cart()

add_to_cart("Mystery Burger", 1)  # does not exist
print_cart()

add_to_cart("Chicken Wings", 1)  # unavailable
print_cart()

remove_from_cart("Gulab Jamun")
print_cart()


# ------
# Order Summary
# ------

print("\n ---- Order Summary ---")

subtotal = 0

for item in cart:
    total_price = item["quantity"] * item["price"]
    subtotal += total_price
    print(f"{item['item']:<15} x{item['quantity']}    ₹{total_price:.2f}")

print("------")

gst = subtotal * 0.05
total = subtotal + gst

print(f"Subtotal:        ₹{subtotal:.2f}")
print(f"GST (5%):        ₹{gst:.2f}")
print(f"Total Payable:   ₹{total:.2f}")
print("-----------.")

# Task 3 — Inventory Tracker with Deep Copy

# 1. Deep Copy Inventory

import copy

# Create deep copy
inventory_backup = copy.deepcopy(inventory)

# Modify original inventory to demonstrate independence
inventory["Paneer Tikka"]["stock"] = 999

print("Modified Inventory (after manual change):")
print(inventory["Paneer Tikka"])

print("\nBackup Inventory (should be unchanged):")
print(inventory_backup["Paneer Tikka"])

# Restore original inventory
inventory = copy.deepcopy(inventory_backup)

print("\nInventory restored to original:")
print(inventory["Paneer Tikka"])

# 2.Simulate Order Fulfillment

# Deduct stock based on cart
for item in cart:
    name = item["item"]
    qty_needed = item["quantity"]
    
    stock_available = inventory[name]["stock"]
    
    if stock_available >= qty_needed:
        inventory[name]["stock"] -= qty_needed
    else:
        print(f"⚠ Warning: Only {stock_available} {name} available, cannot fulfill {qty_needed}")
        inventory[name]["stock"] = 0

# 3. Reorder Alerts

print("\n--- Reorder Alerts ---")

for name, details in inventory.items():
    if details["stock"] <= details["reorder_level"]:
        print(f"⚠ Reorder Alert: {name} — Only {details['stock']} unit(s) left (reorder level: {details['reorder_level']})")

# 4. Final Comparison

print("\n--- Final Inventory ---")
for item, details in inventory.items():
    print(item, details)

print("\n--- Backup Inventory (Unchanged) ---")
for item, details in inventory_backup.items():
    print(item, details)


# Task 4 — Daily Sales Log Analysis

# 1. Total Revenue Per Day

print("=== Revenue Per Day ===")

daily_revenue = {}

for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    daily_revenue[date] = total
    print(f"{date}: ₹{total:.2f}")

# 2. Best-Selling Day

best_day = max(daily_revenue.items(), key=lambda x: x[1])
print(f"\nBest-selling day: {best_day[0]} (₹{best_day[1]:.2f})")

# 3. Most Ordered Item

from collections import Counter

item_counter = Counter()

for orders in sales_log.values():
    for order in orders:
        # count each item once per order
        unique_items = set(order["items"])
        item_counter.update(unique_items)

most_ordered = item_counter.most_common(1)[0]
print(f"\nMost ordered item: {most_ordered[0]} ({most_ordered[1]} orders)")

# 4. Add New Day & Recompute

sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

print("\n -- Updated Revenue Per Day --")

daily_revenue = {}

for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    daily_revenue[date] = total
    print(f"{date}: ₹{total:.2f}")

best_day = max(daily_revenue.items(), key=lambda x: x[1])
print(f"\nUpdated Best-selling day: {best_day[0]} (₹{best_day[1]:.2f})")

# Recomputing  most ordered item
item_counter = Counter()

for orders in sales_log.values():
    for order in orders:
        item_counter.update(set(order["items"]))

most_ordered = item_counter.most_common(1)[0]
print(f"Updated Most ordered item: {most_ordered[0]} ({most_ordered[1]} orders)")