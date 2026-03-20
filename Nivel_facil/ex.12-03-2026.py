# # Nível Fácil

# Write a function plan_roller_event that helps organize a community rollerblading event by processing three pieces of information: 
# an event note with a search term to highlight, the side length of a square garden bed (in meters) that will be used as a rest area, 
# and the number of days the event will run.

# Your function should return a dictionary with three keys: 
# "highlighted_note" containing the note with all case-insensitive matches of the search term wrapped in brackets (like [term]), 
# "garden_area" with the area of the square garden bed in square meters, and "total_hours" showing how many hours are in the given number of days.


# # Resolução

def plan_roller_event(note, search_term, garden_side, days):
    # Write code here
    highlighted_note = note.replace(search_term, f"[{search_term}]")
    highlighted_note = highlighted_note.replace(search_term.capitalize(), f"[{search_term.capitalize()}]")
    highlighted_note = highlighted_note.replace(search_term.upper(), f"[{search_term.upper()}]")

    garden_area = garden_side ** 2

    total_hours = days * 24

    return {
        "highlighted_note": highlighted_note,
        "garden_area": garden_area,
        "total_hours": total_hours
    }

