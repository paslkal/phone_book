class PhoneBook:
    def create(
        self,
        *,
        first_name: str,
        second_name: str,
        last_name: str,
        personal_phone_number: str,
        work_phone_number: str,
        organization: str,
    ):
        """добавляет новую информацию в конец файла"""

        with open("phone_book.txt", "a+", encoding="utf-8") as f:
            f.write(
                f"{first_name} {last_name} {second_name} {work_phone_number} {personal_phone_number} {organization}\n"
            )

    def edit():
        pass

    def find(
        self,
        personal_phone_number: str,
    ) -> str:
        """находит человека по номеру телефона"""

        phone_to_person = self.get_data()
        if personal_phone_number is not None:
            if personal_phone_number in phone_to_person:
                return self.from_dict_to_string(phone_to_person[personal_phone_number])

        return "Not found"

    def get_data(self) -> dict[str, dict]:
        """
        читает данные в файле и возвращает в виде словаря,
        в котором ключ -- номер телефона, а значение -- словарь со всеми данными о человеке
        """

        with open("phone_book.txt", "r", encoding="utf-8") as f:
            string_people = f.readlines()
            dict_people = {}
            for string_person in string_people:
                if string_people == " ":
                    continue
                person = self.from_string_to_dict(string_person)
                dict_people[person["personal_phone_number"]] = person

            return dict_people

    def from_string_to_dict(self, string: str):
        """превращает строку с данными в словарь"""

        (
            first_name,
            second_name,
            last_name,
            work_phone_number,
            personal_phone_number,
            organization,
        ) = string.split()

        person = {
            "first_name": first_name,
            "second_name": second_name,
            "last_name": last_name,
            "work_phone_number": work_phone_number,
            "personal_phone_number": personal_phone_number,
            "organization": organization,
        }

        return person

    def from_dict_to_string(self, person: dict):
        """преобразует словарь с данными о человеке в строку"""

        return f"{person['first_name']} {person['second_name']} {person['last_name']} {person['work_phone_number']} {person['personal_phone_number']} {person['organization']}"


def main():
    phone_book = PhoneBook()
    print(f"List of commands:")
    print(f"- see --- see whole phone book")
    print(f"- find --- find person by phone number")
    print(f"- create --- create a new person in phone book", end="\n\n")
    while True:
        command = input().split()
        if len(command) == 1:
            if command[0] == "see":
                print("============================PHONE BOOK==================")
                people = phone_book.get_data().values()
                for person in people:
                    for info in person.values():
                        print(info, end=" ")
                    print()
                print("========================================================")
            elif command[0] == "create":
                first_name = input("First Name:")

                second_name = input("Second Name:")

                last_name = input("Last Name:")

                work_phone_number = input("Work Phone Number")

                personal_phone_number = input("Personal Phone Number")

                organization = input("Organization")

                phone_book.create(
                    first_name=first_name,
                    second_name=second_name,
                    last_name=last_name,
                    work_phone_number=work_phone_number,
                    personal_phone_number=personal_phone_number,
                    organization=organization,
                )
                print(f'Person was created!')
        elif len(command) == 2 and command[0] == "find":
            print(phone_book.find(command[1]))


if __name__ == "__main__":
    main()
