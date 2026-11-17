

def error_check(template_content, attendees):
    if (not isinstance(template_content, str)):
        raise ValueError("Template content must be a string.")

    if (not isinstance(attendees, list)):
        raise ValueError("Attendees must be a list of dictionaries.")

    for attendee in attendees:
        if (not isinstance(attendee, dict)):
            raise ValueError("Attendee data must be a dictionary")

    if (template_content == ""):
        raise ValueError("Template is empty, no output files generated.")

    if (attendees == {}):
        raise ValueError("No data provided, no output files generated.")


def generate_invitations(template_content, attendees):
    placeholders = {
        'name',
        'event_title',
        'event_date',
        'event_location'
    }
    invitations = []

    try:
        error_check(template_content, attendees)
    except ValueError as e:
        print(e)
        return None

    for attendee in attendees:
        invitation = template_content
        for placeholder in placeholders:
            try:
                if attendee[placeholder]:
                    replacement = attendee[placeholder]
                else:
                    replacement = placeholder + ": N/A"

                invitation = invitation.replace("{" + placeholder + "}", replacement)
            except KeyError:
                invitation = invitation.replace("{" + placeholder + "}", placeholder + ": N/A")
        invitations.append(invitation)

    i = 1
    for invite in invitations:
        with open("output_" + str(i) + ".txt", "w") as f:
            f.write(invite)
        i += 1