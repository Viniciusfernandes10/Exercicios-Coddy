# # Nível Fácil

# Write a function process_pet_record that takes a pet's toy color name (like "red" or "blue"), 
# the number of luggage items they brought, and an urgency score. Return a dictionary with three keys:

# "toy_color_hex" - the toy color converted to its hex code (support basic colors: red, blue, green, yellow, black, white)
# "luggage_arrangements" - the product of all numbers from 1 to N (representing possible ways to arrange their luggage)
# "priority" - a string label based on urgency score: "low" (0-3), "medium" (4-7), or "high" (8-10)


# # Resolução

def process_pet_record(toy_color, luggage_count, urgency_score):
    # Write code here 

    cores = {
        "red": "#FF0000",
        "green": "#008000",
        "blue": "#0000FF",
        "black": "#000000",
        "white": "#FFFFFF",
        "yellow": "#FFFF00",
        "purple": "#000000"
    }
    
    toy_color_hex = cores.get(toy_color.lower()) 

    luggage = 1
    for i in range(1, luggage_count + 1):
        luggage *= i

    if 0 <= urgency_score <= 3:
        urgency_score = "low"
    elif 4 <= urgency_score <= 7:
        urgency_score = "medium"
    else:
        urgency_score = "high"

    return {
        "toy_color_hex": toy_color_hex,
        "luggage_arrangements": luggage,
        "priority": urgency_score
    }

