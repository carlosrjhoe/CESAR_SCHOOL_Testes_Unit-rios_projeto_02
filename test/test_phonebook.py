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

    def test_get_numbers_retornar_todos_numeros(self, setUp):
        """teste get_names para retornar todos os nomes cadastrados"""
        phonebook = setUp
        phonebook.add("Carlos", "333")
        phonebook.add("Mayara", "111")
        phonebook.add("Neto", "444")
        resultado = list(phonebook.get_numbers())
        esperado = list(phonebook.entries.values())
        assert resultado == esperado

    def test_clear_para_excluir_todos_nomes_e_numeros_cadastrados(self, setUp):
        phonebook = setUp
        phonebook.add("Carlos", "333")
        phonebook.add("Mayara", "111")
        phonebook.add("Neto", "444")
        resultado = phonebook.clear()
        esperado = "Phonebook foi limpado com sucesso"
        assert resultado == esperado

    @pytest.mark.parametrize(
        "subSt, reTur",
        [
            ("POL", [{"POLICIA", "190"}]),
            ("Car", [{"Carlos", "333"}]),
            ("May", [{"Mayara", "111"}]),
            ("Net", [{"Neto", "444"}]),
            (
                "",
                [
                    {"POLICIA", "190"},
                    {"Carlos", "333"},
                    {"Mayara", "111"},
                    {"Neto", "444"},
                ],
            ),
        ],
    )
    def test_search_retornar_o_que_contam_substring(self, setUp, subSt, reTur):
        """teste search para retornar o nome da subString"""
        phonebook = setUp
        phonebook.add("Carlos", "333")
        phonebook.add("Mayara", "111")
        phonebook.add("Neto", "444")
        resultado = phonebook.search(subSt)
        assert resultado == reTur

    def test_get_phonebook_sorted(self, setUp):
        """teste get_phonebook_sorted para retornar a lista ordenada"""
        phonebook = setUp
        phonebook.add("Carlos", "333")
        phonebook.add("Mayara", "111")
        phonebook.add("Neto", "444")
        resultado = phonebook.get_phonebook_sorted()
        esperado = dict(sorted(phonebook.entries.items()))
        assert resultado == esperado

    def test_get_phonebook_reverse(self, setUp):
        """teste get_phonebook_reverse para retornar
        a lista ordenada invertida"""
        phonebook = setUp
        phonebook.add("Carlos", "333")
        phonebook.add("Mayara", "111")
        phonebook.add("Neto", "444")
        resultado = phonebook.get_phonebook_reverse()
        esperado = {"Carlos": "333", "Mayara": "111",
                    "Neto": "444", "POLICIA": "190"}
        assert resultado == esperado

    @pytest.mark.parametrize(
        "nome, esperado",
        [
            ("Carlos", "Número deletado"),
            ("Car", "Nome não encontrado"),
        ],
    )
    def test_delete_para_deletar_um_usuario(self, setUp, nome, esperado):
        """teste delete para verificar se o contato é deletado"""
        phonebook = setUp
        phonebook.add("Carlos", "333")
        phonebook.add("Mayara", "111")
        phonebook.add("Neto", "444")
        resultado = phonebook.delete(nome)
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
