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
        with open('phone_book.txt', 'a+', encoding='utf-8') as f:
            f.write(f'{first_name} {last_name} {second_name} {phone_number} {organization}\n')

    def edit():
        pass

    def find():
        pass

phone_book = PhoneBook()
