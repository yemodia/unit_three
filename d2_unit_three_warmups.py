
def add_one(number):
    number += 1
    print("number in function is", number)  # number is 6


def main():
    number = 5
    add_one(number)
    print("number in main is", number)  # number is 5


main()
