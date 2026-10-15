
# ICT Club Candidate Verification System
from pyscript import display, document


def view_user(e):
    document.getElementById("result").innerHTML = " "

    # Get's the First and Last Name Inputted
    first_name = document.getElementById("firstName").value
    last_name = document.getElementById("lastName").value

    candidate_name = first_name + " " + last_name

    # List of ICT Club members
    ict_club_members = ["rivera victoria", "lim reuben", "manalo antonio", "manapat lucas", "dannug reign", "macachor hans", "ukwatte dan"]

    # Checks the name
    candidate_checker = candidate_name.lower() in ict_club_members

    # Store both possible messages
    display_message = (f'Sorry {candidate_name}, your name is not on the list.',f'Congratulations {candidate_name} You are now part of the ICT club.')

    # Display the result
    display(display_message[candidate_checker], target="result")
