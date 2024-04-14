from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Run a test on SilverServiceTaxi class."""
    # hummer_taxi = SilverServiceTaxi("Hummer", 200, 4)
    # print(hummer_taxi)
    test_taxi = SilverServiceTaxi("Test Taxi", 100, 2)
    test_taxi.drive(18)
    print(f"${test_taxi.get_fare():.2f}")


main()
