from prac_09.unreliable_car import UnreliableCar


def main():
    """Run a test on UnreliableCar class."""
    my_car = UnreliableCar("My Car", 120, 80)
    other_car = UnreliableCar("Other Car", 100, 90)

    for i in range(1, 12):
        print(f"Distance to drive {i} km:")
        print(f"{my_car.name} drove {my_car.drive(i)} km")
        print(f"{other_car.name} drove {other_car.drive(i)} km")

    print(my_car)
    print(other_car)


main()
