from phone_book import PhoneBook


def main():
    phone_book = PhoneBook()
    print(f"List of commands:")
    print(f"- see --- see whole phone book")
    print(f"- find --- find person by personal phone number")
    print(f"- create --- create a new person in phone book")
    print(f"- edit --- edit info about person")
    while True:
        print(">", end=" ")
        command = input().split()
        if not command:
            continue

        if command[0] == "see":
            print("============================PHONE BOOK============================")
            people = phone_book.get_data().values()
            if len(people) == 0:
                print("There's no people in phone book")
            for person in people:
                for info in person.values():
                    print(info, end=" ")
                print()
            print("==================================================================")
        elif command[0] == "create":
            first_name = input("First Name:")
            while " " in first_name:
                print("First Name must consist of one word")
                first_name = input("First Name:")

            second_name = input("Second Name:")
            while " " in second_name:
                print("Second Name must consist of one word")
                second_name = input("Second Name:")

            last_name = input("Last Name:")
            while " " in last_name:
                print("Last Name must consist of one word")
                last_name = input("Last Name:")

            work_phone_number = input("Work Phone Number:")
            while " " in work_phone_number:
                print(f"Work Phone Number must consist of one word")
                work_phone_number = input("Work Phone Number:")

            personal_phone_number = input("Personal Phone Number:")
            while " " in personal_phone_number:
                print(f"Personal Phone Number must consist of one word")
                personal_phone_number = input("Personal Phone Number:")

            organization = input("Organization:")
            while " " in organization:
                print("Organization must consist of one word")
                organization = input("Organization:")

            phone_book.create(
                first_name=first_name,
                second_name=second_name,
                last_name=last_name,
                work_phone_number=work_phone_number,
                personal_phone_number=personal_phone_number,
                organization=organization,
            )
            print(f"\nPerson is created!")
        elif command[0] == "find":
            if len(command) == 1:
                print("There's no number to find person")
            else:
                print(phone_book.find(command[1]))
        elif command[0] == "edit":
            print("edited")
        else:
            print("There's no such command")


if __name__ == "__main__":
    main()
