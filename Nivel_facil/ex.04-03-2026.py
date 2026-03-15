# # Nível Fácil

# Write a function assign_plot that takes a gardener's planting note (a string) and the day's temperature (a number). 
# Your function should normalize the note by converting it to lowercase, trimming whitespace, and replacing multiple spaces with single spaces. 
# Then check if the temperature is at boiling point (100 or above) and whether the normalized note reads the same forwards and backwards when ignoring spaces.
# Return a dictionary with three keys: "normalized_note" (the cleaned string), "is_palindrome" (boolean), and "is_boiling" (boolean).


# # Resolução

def assign_plot(note, temperature):
    # Write code here
    normalized_note = " ".join(note.lower().strip().split())
    no_spaces = normalized_note.replace(" ", "")
    is_palindrome = no_spaces == no_spaces[::-1]

    is_boiling = temperature >= 100

    return {
        "normalized_note": normalized_note,
        "is_palindrome": is_palindrome,
        "is_boiling": is_boiling
    }
