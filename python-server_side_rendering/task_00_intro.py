import os

def generate_invitations(template, attendees):
    # Validate input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Handle empty inputs
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        # Replace placeholders with values or "N/A"
        content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None or value == "":
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        # Write to output file
        filename = f"output_{idx}.txt"
        try:
            with open(filename, "w") as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
