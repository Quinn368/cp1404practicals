def main():
    """Get password and print password in form of asterisks"""
    password = get_password()
    print_asterisks(password)


def get_password():
    """Get password from users"""
    password = input(f"Enter password: ")
    return password


def print_asterisks(password):
    """Print password in form of asterisks, relating to the length of the password"""
    print('*' * len(password))


main()
