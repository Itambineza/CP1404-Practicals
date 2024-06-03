MIN_LENGTH = 8


def main():
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def get_password(min_length):
    password = input("Password: ")
    while len(password) < min_length:
        print("Password must be at least", min_length, "characters long. ")
        password = input("Password: ")
    return password


def print_asterisks(password):
    print('*' * len(password))


main()
