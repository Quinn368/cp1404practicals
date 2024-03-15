def main():
    email_to_name = {}
    email = input("Enter email: ")
    while email != '':
        name = get_name_from_email(email)
        check_name = input(f"Is your name {name}? (Y/n) ")
        if check_name.upper() != "Y" and check_name != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    prefix = email.split('@')[0]
    part = prefix.split('.')
    name = " ".join(part).title()
    return name


main()