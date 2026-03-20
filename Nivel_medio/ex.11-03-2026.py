# # Nível Fácil

# Write a function manage_section that takes water_count, microbe_level, section_code and returns a dictionary with updated greenhouse section data.

# The function increments the water count by 1, decrements the microbe level by 1, and reverses the section code string.

# Parameters:

# water_count (int): Current watering count for the section
# microbe_level (int): Current microorganism contamination level
# section_code (str): Section identifier code
# Returns: Dictionary with updated values. Format: {"water_count": updated_count, "microbe_level": updated_level, "section_code": "reversed_code"}


# # Resolução

def manage_section(water_count, microbe_level, section_code):
    # Write code here
    water_count += 1
    microbe_level -= 1
    section_code = section_code[::-1]

    dict_function = {
        'water_count': water_count,
        'microbe_level': microbe_level,
        'section_code': section_code
    }

    return dict_function


