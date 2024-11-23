import pytest


class TestePhoneBook:

    @pytest.mark.parametrize(
        "test_data", ["car#los", "@carlos", "car!los", "cart%r", "car$los"]
    )
    def test_add_phonebook_com_caractere_invalido(self, setUp, test_data):
        """teste add com caractere inválido"""
        phonebook = setUp
        resultado = phonebook.add(test_data, "123456789")
        experado = "Nome invalido"
        assert resultado == experado

    def test_add_numero_invalido(self, setUp):
        """teste add com número inválido"""
        phonebook = setUp
        resultado = phonebook.add("Carlos", " ")
        esperado = "Numero invalido"
        assert resultado == esperado

    def test_add_phonebook_name_nao_existe_adicionado(self, setUp):
        """teste add com nome não exitente válido"""
        phonebook = setUp
        phonebook.add("Carlos", "123456789")
        resultado = "Carlos" in phonebook.entries
        esperado = True
        assert resultado == esperado

    @pytest.mark.parametrize(
        "test_data", ["car#los", "@carlos", "car!los", "cart%r", "car$los"]
    )
    def test_lookup_phonebook_com_caractere_invalido(self, setUp, test_data):
        """teste lookup com caractere inválido"""
        phonebook = setUp
        phonebook.add(test_data, "333")
        resultado = phonebook.lookup(test_data)
        experado = "Nome invalido"
        assert resultado == experado

    def test_lookup_phonebook_com_nome_valido(self, setUp):
        """teste lookup com caractere inválido"""
        phonebook = setUp
        phonebook.add("Carlos", "333")
        resultado = phonebook.lookup("Carlos")
        experado = "333"
        assert resultado == experado

    def test_get_names_retornar_todos_nomes(self, setUp):
        """teste get_names para retornar todos os nomes cadastrados"""
        phonebook = setUp
        phonebook.add("Carlos", "333")
        phonebook.add("Mayara", "111")
        resultado = phonebook.get_names()
        esperado = phonebook.entries.keys()
        assert resultado == esperado

    def test_change_number_do_nome_exitente(self, setUp):
        """teste charge_number para alterar número do nome cadastrado"""
        phonebook = setUp
        phonebook.add("Mayara", "111")
        phonebook.add("Carlos", "333")
        resultado = phonebook.change_number("Carlos", "222")
        esperado = "Número atualizado"
        assert resultado == esperado

    def test_change_number_de_nome_inexistente(self, setUp):
        """teste charge_number para alterar número de nome não cadastrado"""
        phonebook = setUp
        phonebook.add("Mayara", "111")
        phonebook.add("Carlos", "333")
        resultado = phonebook.change_number("Neto", "222")
        esperado = "Nome não encontrado"
        assert resultado == esperado

    def test_get_name_by_number(self, setUp):
        """teste get_name_by_number para retornar o nome do
        número associado a ele."""
        phonebook = setUp
        phonebook.add("Carlos", "333")
        resultado = phonebook.get_name_by_number("333")
        esperado = "Carlos"
        assert resultado == esperado
