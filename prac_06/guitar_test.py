from prac_06.guitar import Guitar

THIS_YEAR = 2024


def run_tests():
    """Run a test code to check if Guitar class is working well."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    old_guitar = Guitar(name, year, cost)
    new_guitar = Guitar("Another Guitar", 2013, 38433.45)

    print(f"{old_guitar.name} get_age() - Expected {100}. Got {old_guitar.get_age()}")
    print(f"{new_guitar.name} get_age() - Expected {9}. Got {new_guitar.get_age()}")
    print(f"{old_guitar.name} is_vintage() - Expected {True}. Got {old_guitar.is_vintage()}")
    print(f"{new_guitar.name} is_vintage() - Expected {False}. Got {new_guitar.is_vintage()}")


run_tests()
