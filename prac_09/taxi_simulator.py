from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Program of taxi simulator with choosing a taxi and its distance, showing the bill."""
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0
    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'c':
            current_taxi = choose_taxi(taxis)
            print_bill(bill_to_date)
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
                print_bill(bill_to_date)
            else:
                bill_to_date = drive_taxi(current_taxi, bill_to_date)
        else:
            print("Invalid option")
            print_bill(bill_to_date)
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def print_bill(bill_to_date):
    """Print the bill."""
    print(f"Bill to date: ${bill_to_date:.2f}")


def choose_taxi(taxis):
    """Choose a taxi."""
    display_taxis(taxis)
    taxi_choice = int(input("Choose taxi: "))
    try:
        return taxis[taxi_choice]
    except IndexError:
        print("Invalid taxi choice")
        return None


def drive_taxi(current_taxi, bill_to_date):
    """Get the distance needed to travel, cost, and the bill."""
    distance = float(input("Drive how far? "))
    current_taxi.start_fare()
    current_taxi.drive(distance)
    cost = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
    bill_to_date += cost
    print(f"Bill to date: ${bill_to_date:.2f}")
    return bill_to_date


def display_taxis(taxis):
    """Display the list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
