from typing import List


def error_check(template_content, attendees):
    if (not isinstance(template_content, str)):
        raise ValueError("Template content must be a string.")

    if (not isinstance(attendees, List[dict])):
        raise ValueError("Attendees must be a list of dictionaries containing each attendees data.")

    if (template_content == "" or template_content is None):
        raise ValueError("Template is empty, no output files generated.")

    if (attendees == {} or attendees is None):
        raise ValueError("No data provided, no output files generated.")


def generate_invitations(template_content, attendees):
    placeholders = {
        'name',
        'event_title',
        'event_date',
        'event_location'
    }
    invitations = []

    error_check(template_content, attendees)

    for attendee in attendees:
        invitation = template_content
        for placeholder in placeholders:
            if attendee[placeholder]:
                replacement = attendee[placeholder]
            else:
                replacement = placeholder + ": N/A"
            invitation = invitation.replace("{" + placeholder + "}", replacement)
        invitations.append(invitation)

    i = 1
    for invite in invitations:
        with open("output_" + str(i) + ".txt", "w") as f:
            f.write(invite)
        i += 1