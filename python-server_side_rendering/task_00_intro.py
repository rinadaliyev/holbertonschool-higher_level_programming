import os

def generate_invitations(template, attendees):
    # -----------------------------
    # Validate input types
    # -----------------------------
    if not isinstance(template, isinstance(template, str).__class__):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Ensure each item is a dictionary
    if any(not isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # -----------------------------
    # Handle empty template
    # -----------------------------
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # -----------------------------
    # Handle empty attendee list
    # -----------------------------
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # -----------------------------
    # Generate invitation files
    # -----------------------------
    for index, attendee in enumerate(attendees, start=1):

        # Create a copy of template for modification
        filled_template = template

        # Replace placeholders
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)

            # If missing or None → use "N/A"
            if value is None:
                value = "N/A"

            filled_template = filled_template.replace("{" + key + "}", str(value))

        # Write output file
        filename = f"output_{index}.txt"

        try:
            with open(filename, "w") as f:
                f.write(filled_template)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
            return
