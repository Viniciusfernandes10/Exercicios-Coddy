# # Nível Fácil

# Write a function update_inventory that takes equipment_name, current_count, change_amount and returns a formatted inventory string.

# The function updates the equipment count by adding or subtracting the change amount, then returns the result in a specific format.

# Parameters:

# equipment_name (str): Name of the baseball equipment
# current_count (int): Current number of items in inventory
# change_amount (int): Amount to add (positive) or remove (negative)
# Returns: Formatted string showing updated inventory. Format: Equipment: [name] - Count: [updated_count]


# # Resolução

def update_inventory(equipment_name, current_count, change_amount):
    # Write code here
    count = current_count + change_amount
    return f"Equipment: {equipment_name} - Count: {count}"

