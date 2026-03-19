# # Nível Fácil

# Write a function calculate_lab_budget that takes computer_cost, monitor_cost and returns a formatted budget breakdown string.

# The function calculates the total cost for setting up the community center's computer lab and creates a budget summary.

# Parameters:

# computer_cost (int): Cost of computers in dollars
# monitor_cost (int): Cost of monitors in dollars
# Returns: Budget breakdown string. Format: Computers: $X, Monitors: $Y, Total: $Z


# # Resolução

def calculate_lab_budget(computer_cost, monitor_cost):
    # Write code here
    return f"Computers: ${computer_cost}, Monitors: ${monitor_cost}, Total: ${computer_cost + monitor_cost}"
