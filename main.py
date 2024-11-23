from src.phonebook import Phonebook


test_phone_book = Phonebook()
test_phone_book.add("Carlos", "333")
test_phone_book.add("Mayara", "111")
# test_phone_book.add("Carlos", "222")
# print(test_phone_book.lookup('Carlos'))
# print(test_phone_book.get_names)
print(test_phone_book.entries)
print(test_phone_book.change_number('Carlos', '222'))
print(test_phone_book.entries)
print(test_phone_book.change_number('Neto', '444'))
# print(test_phone_book.get_numbers())
# print(test_phone_book.get_phonebook_sorted())
print(test_phone_book.get_name_by_number("222"))
# print(list(test_phone_book.entries.keys()))
