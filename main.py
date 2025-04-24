class PhoneBook:
    def add(
        self,
        *,
        first_name: str,
        second_name: str,
        last_name: str,
        personal_phone_number: str,
        work_phone_number: str,
        organization: str,
    ):
        with open("phone_book.txt", "a+", encoding="utf-8") as f:
            f.write(
                f"{first_name} {last_name} {second_name} {work_phone_number} {personal_phone_number} {organization}\n"
            )

    def edit():
        pass

    def find(
        self,
        personal_phone_number=None | str,
    ) -> list[str]:
        phone_to_person = self.get_data()
        if personal_phone_number is not None:
            if personal_phone_number in phone_to_person:
                return [
                    self.from_dict_to_string(phone_to_person[personal_phone_number])
                ]

    def get_data(self) -> dict[str, dict]:
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
        return f"{person['first_name']} {person['second_name']} {person['last_name']} {person['work_phone_number']} {person['personal_phone_number']} {person['organization']}"


phone_book = PhoneBook()
# phone_book.add(
#     work_phone_number="+79778549563",
#     personal_phone_number="+79778549563",
#     first_name="Паскаль",
#     second_name="Синдайихебура",
#     last_name="Этьенович",
#     organization="АВ-СОФТ",
# )
# print(phone_book.get_data())
# print(phone_book.find('+79778549563'))