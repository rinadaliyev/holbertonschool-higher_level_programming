#!/usr/bin/python3
"""
Task 0: Simple Templating Program
Generates invitation files from a template and a list of attendees.
"""

import os


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template.

    Parameters:
        template (str): The template string containing placeholders.
        attendees (list): List of dictionaries with attendee info.

    Returns:
        None
    """

    # ----------------- INPUT TYPE CHECK -----------------
    if not isinstance(template, str):
        print(f"Error: Template should be a string, got {type(template).__name__}")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Attendees should be a list of dictionaries, got {type(attendees).__name__}")
        return

    # ----------------- EMPTY INPUT CHECK -----------------
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # ----------------- PROCESS EACH ATTENDEE -----------------
    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        # Replace placeholders
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            invitation = invitation.replace(f"{{{key}}}", str(value))

        # Write output file
        filename = f"output_{index}.txt"
        try:
            with open(filename, "w") as f:
                f.write(invitation)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
