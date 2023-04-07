import re

def email_checker(email):

    # Define regular expression patterns for email validation checking.
    # going to copy it and paste it, too long lol
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Now, match the email to the pattern using regular expression(s)
    match = re.match(pattern, email)

    # If the match object found then email is validated, if else, it is invalid.
    if match:
        return "Valid email."
    else:
        return "Invalid email."

email = "pro@mail.com" # Replace with the email you would want to check (FOR ETHICAL PURPOSES ONLY)
result = email_checker(email)
print(result)