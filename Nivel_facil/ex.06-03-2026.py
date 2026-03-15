# # Nível Fácil

# Write a function create_exhibit_label that takes full_name, project_title and returns a formatted exhibit label string.

# The function extracts the first 3 characters of the first name and combines them with the project title in the format "ABC - Project Title".

# Parameters:

# full_name (str): Student's full name (first and last name separated by space)
# project_title (str): Title of the science project
# Returns: Formatted exhibit label. Format: ABC - Project Title


# # Resolução

def create_exhibit_label(full_name, project_title):
    first_name = full_name.split()[0]     
    code = first_name[:3].upper()         
    return f"{code} - {project_title}" 

