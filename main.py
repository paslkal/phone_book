class PhoneBook:
    def add(
        self,
        *,
        phone_number: str,
        first_name: str,
        second_name: str,
        last_name: str,
        organization: str,
    ):
        with open("phone_book.txt", "a+", encoding="utf-8") as f:
            f.write(
                f"{first_name} {last_name} {second_name} {phone_number} {organization}\n"
            )

    def edit():
        pass

    def find(
        self,
        phone_number=None,
        first_name=None,
        second_name=None,
        last_name=None,
        organization=None,
    ):
        pass

    def get_data(self):
        with open("phone_book.txt", "r", encoding='utf-8') as f:
            string_people = f.readlines()
            dict_people = []
            for string_person in string_people:
                dict_people.append(self.string_to_dict(string_person))

            return dict_people

    def string_to_dict(self, string: str):
        first_name, second_name, last_name, phone_number, organization = string.split()

        person = {
            first_name:first_name,
            second_name:second_name,
            last_name:last_name,
            phone_number:phone_number,
            organization:organization
        }

        return person


phone_book = PhoneBook()
