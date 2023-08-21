"""
Emails
Estimate: 1 hour
Actual: 45mins 10seconds
"""
email_to_name = {}
email = input("Email: ")

while email != "":
    split_name = email.split("@")

    if "." in split_name[0]:
        split_name = split_name[0].split(".")
        name = (" ".join([split_name[0], split_name[1]])).title()
    else:
        name = split_name[0]

    confirm = input(f"Is your name {name}? (Y/n) ").lower()
    if confirm == "n" or confirm == "no":
        name = input("Name: ")

    email_to_name[email] = name

    email = input("Email: ")

for email, full_name in email_to_name.items():
    print(f"{full_name} ({email})")
