import random

NUMBER_EACH_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def sample():
    quick_picks = int(input("How many quick picks? "))
    for i in range(quick_picks):
        samples = []
        for j in range(NUMBER_EACH_LINE):
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            while number in samples:
                number = random.randint(MIN_NUMBER, MAX_NUMBER)
            samples.append(number)
        samples.sort()
        print(" ".join(f"{number}" for number in samples))


sample()
