from pytest import fixture
from src.phonebook import Phonebook


@fixture
def setUp():
    return Phonebook()
