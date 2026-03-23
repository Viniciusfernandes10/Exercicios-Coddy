# # Nível Fácil

# Write a function manage_park_reports that takes disease_reports, incident_logs, safety_reports, and retraction_ids and returns a dictionary with report counts and updated safety data.

# The function processes park health and safety data by counting active disease reports, medical incidents, and filtering out retracted safety reports.

# Parameters:

# disease_reports (list): List of plant disease names
# incident_logs (list): List of visitor medical incident descriptions
# safety_reports (list): List of safety report IDs
# retraction_ids (list): List of report IDs to remove from safety reports
# Returns: Dictionary with park management data. Format: {"diseases": count, "incidents": count, "active_reports": [remaining_report_ids]}


# # Resolução

def manage_park_reports(disease_reports, incident_logs, safety_reports, retraction_ids):
    # Write code here

    total_disease = len(disease_reports)
    
    total_incident = len(incident_logs)
    
    total_numbers = []
    for i in safety_reports:
        if i not in retraction_ids:
            total_numbers.append(i)


    return {
        "diseases": total_disease,
        "incidents": total_incident,
        "active_reports": total_numbers
    }
