from phone_book import PhoneBook
import random

phone_book = PhoneBook()
for _ in range(100):
    phone_book.create(
        first_name='Egor',
        second_name='Ptushkin',
        last_name='Sanalovich',
        personal_phone_number=str(random.randint(10**4, 10**5)),
        work_phone_number='1328123123',
        organization='Jicy Ducy'
    )

