import os

class PhoneBook:
    def __init__(self):
        with open("phone_book.txt", "r", encoding="utf-8") as f:
            if not os.path.exists('phone_book.txt'):
                self.size = 0
            else:
                self.size = len(f.readlines())

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
            self.size += 1
            f.write(
                f"{self.size} {first_name} {last_name} {second_name} {work_phone_number} {personal_phone_number} {organization}\n"
            )

    def edit(
        self,
        *,
        id: int,
        first_name: str | None,
        second_name: str | None,
        last_name: str | None,
        personal_phone_number: str | None,
        work_phone_number: str | None,
        organization: str | None,
    ):
        with open("phone_book.txt", "r", encoding="utf-8") as f:
            data = f.readlines()

        person = self.from_string_to_dict(data[id - 1])

        if first_name:
            person["first_name"] = first_name

        if second_name:
            person["second_name"] = second_name

        if last_name:
            person["last_name"] = last_name

        if personal_phone_number:
            person["personal_phone_number"] = personal_phone_number

        if work_phone_number:
            person["work_phone_number"] = work_phone_number

        if organization:
            person["organization"] = organization

        data[id - 1] = self.from_dict_to_string(person) + "\n"

        with open("phone_book.txt", "w", encoding="utf-8") as f:
            f.writelines(data)

    def find(
        self,
        personal_phone_number: str,
    ) -> str:
        """находит человека по номеру телефона"""

        phone_to_person = self.get_all_data()
        if personal_phone_number is not None:
            if personal_phone_number in phone_to_person:
                return self.from_dict_to_string(phone_to_person[personal_phone_number])

        return "Not found"

    def get_data(self, page=1) -> dict[str, dict[str, str]]:
        """
        читает данные в файле и возвращает в виде словаря,
        в котором ключ -- номер телефона, а значение -- словарь со всеми данными о человеке
        """

        with open("phone_book.txt", "r", encoding="utf-8") as f:
            string_people = f.readlines()
            dict_people = {}
            for i in range((page - 1) * 10, min(len(string_people), page * 10)):
                string_person = string_people[i]
                if string_people == " ":
                    continue
                person = self.from_string_to_dict(string_person)
                dict_people[person["personal_phone_number"]] = person

            return dict_people

    def get_all_data(self) -> dict[str, dict[str, str]]:
        """
        читает все данные в файле и возвращает в виде словаря,
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

    def from_string_to_dict(self, string: str) -> dict[str, str]:
        """превращает строку с данными в словарь"""

        (
            id,
            first_name,
            second_name,
            last_name,
            work_phone_number,
            personal_phone_number,
            organization,
        ) = string.split()

        person = {
            "id": id,
            "first_name": first_name,
            "second_name": second_name,
            "last_name": last_name,
            "work_phone_number": work_phone_number,
            "personal_phone_number": personal_phone_number,
            "organization": organization,
        }

        return person


    def from_dict_to_string(self, person: dict[str, str]) -> str:
        """преобразует словарь с данными о человеке в строку"""

        return f"{person['id']} {person['first_name']} {person['second_name']} {person['last_name']} {person['work_phone_number']} {person['personal_phone_number']} {person['organization']}"
