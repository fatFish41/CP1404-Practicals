LOWER = 33
UPPER = 127


def main():
    char = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(char, ord(char)))
    number = get_number_between(LOWER, UPPER)
    print("The character for {} is {}".format(number, chr(number)))

    # ASCII table (no columns)
    for value in range(LOWER, UPPER + 1):
        print("{:3} {:>4}".format(value, chr(value)))


def get_number_between(lower=LOWER, upper=UPPER):
    number = int(
        input("Enter a number between {} and {}: ".format(lower, upper)))
    while number < lower or number > upper:
        number = int(
            input("Enter a number between {} and {}: ".format(lower, upper)))
    return number


main()