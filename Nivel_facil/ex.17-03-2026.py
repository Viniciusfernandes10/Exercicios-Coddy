# # Nível Fácil

# Write a function organize_move that helps prepare for the photography studio's moving day. You'll receive a box ID number (integer), 
# a list of item labels (strings that may have consecutive duplicates), a distance in meters (integer), and steps per meter (integer).

# Return a dictionary with three keys: "largest_digit" containing the largest digit found in the box ID, 
# "cleaned_labels" with consecutive duplicate labels removed (keeping the first of each run), and "total_steps" for the round trip (distance × 2 × steps per meter).

# # Resolução

def organize_move(box_id, item_labels, distance, steps_per_meter):
    # Write code here 
    
    largest_digit = max(int(digit) for digit in str(box_id))

    cleaned_labels = []
    for item in item_labels:
        if not cleaned_labels or item != cleaned_labels[-1]:
            cleaned_labels.append(item)

    total_steps = (distance * steps_per_meter) * 2

    return {
        "largest_digit": largest_digit,
        "cleaned_labels": cleaned_labels,
        "total_steps": total_steps
    }


