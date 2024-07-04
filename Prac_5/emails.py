def main():
    email_dict = {}

    while True:
        email = input('Email: ').strip()

        if email == "":
            break
        name = extract_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        # if confirm == '' or confirm == 'y':
        #     print(f"Email'{email}' already exists in the dictionary")
        #     continue

        name = extract_name(email)
        print(f"Extracted name: {name}")

        confirm = input(f"Is '{name}' correct? (Y/n) ").strip().lower()
        if confirm == '' or confirm == 'y':
            email_dict[email] = name
        else:
            name = input("Name: ").strip()
            email_dict[email] = name

    print("\nStored Emails and Names:")
    for email, name in email_dict.items():
        print(f"{name} ({email})")


def extract_name(email):
    # Extracts a name from the email address
    username = email.split('@')[0]
    name = ' '.join(username.split('.')).title()  # Assuming username might have dots
    return name


main()
