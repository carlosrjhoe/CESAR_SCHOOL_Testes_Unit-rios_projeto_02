class Phonebook:

    def __init__(self):
        self.entries = {"POLICIA": "190"}

    def add(self, name, number):
        """
        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'

        Erros identificados:
            O tratamento dos caracteres especiais como #, @, !, $, %repete
            código e possui erros de digitação nas mensagens retornadas.
            Exemplo: "Nme invalido"e "Nome invalio".

        Pontos de melhoria:
            Centralize a validação de caracteres em uma função separada para
            evitar duplicação e garantir consistência.
        """
        """Código refatorado:"""
        for char in ["#", "@", "!", "$", "%"]:
            if char in name:
                return "Nome invalido"

        if not number or not number.isdigit():
            return "Numero invalido"

        if name not in self.entries:
            self.entries[name] = number
            return "Numero adicionado"

        """Código antigo."""
        # if "#" in name:
        #     return "Nome invalido"
        # if "@" in name:
        #     return "Nome invalido"
        # if "!" in name:
        #     return "Nome invalido"
        # if "$" in name:
        #     return "Nome invalido"
        # if "%" in name:
        #     return "Nome invalido"

        # if len(number) < 0:
        #     return "Numero invalid"

        # if name not in self.entries:
        #     self.entries[name] = number

        # return "Numero adicionado"

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name

        Erros identificados:
            Não há tratamento para casos em que o nome não existe nenhum
            dicionário, resultando em um erro de chave.

        Pontos de melhoria:
            Usar dict.get()o valor padrão para evitar erros, ou verificar
            explicitamente se o nome existe.

        """
        """Código antigo."""
        # if "#" in name:
        #     return "Nome invalido"
        # if "@" in name:
        #     return "Nome invalido"
        # if "!" in name:
        #     return "Nome invalido"
        # if "$" in name:
        #     return "Nome invalido"
        # if "%" in name:
        #     return "Nome invalido"

        """Código refatorado:"""
        for char in ["#", "@", "!", "$", "%"]:
            if char in name:
                return "Nome invalido"
        if name in self.entries:
            return self.entries[name]
        else:
            return "Nome não encontrado"

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        return self.entries.keys()

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        return self.entries.values()

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'

        Erros identificados:
            Retornar uma string como confirmação do método pode ser redundante,
            considerando que quem chamou o método já sabe que ele foi executado
        """
        self.entries.clear()
        return "Phonebook foi limpado com sucesso"

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search

        Erros identificados:
            A lógica de if search_name not in name está invertida.

        Pontos de melhoria:
            Retornar uma lista com os pares {nome, número}
            para os contatos que contêm uma substring
        """

        result = []
        for name, number in self.entries.items():
            if search_name in name:
                result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """
        :return: return phonebook in sorted order

        Erros identificados:
            método está retornando o dicionário self.entries diretamente,
            sem aplicar qualquer ordenação.

        Pontos de melhoria:
            retornar os itens do dicionário em uma lista de tuplas
            (ou reconstruir o dicionário ordenado):
        """
        return dict(sorted(self.entries.items()))

    def get_phonebook_reverse(self):
        """
        :return: return phonebook in reverse sorted order

        Erros identificados:
            O método atualmente apenas retorna o dicionário self.entriessem
            aplicar nenhuma ordenação, não atendendo à descrição de retornar
            os dados em ordem reversa.

        Pontos de melhoria:
            Use sorted() para garantir que os
            itens sejam ordenados em ordem decrescente.
        """
        return dict(sorted(self.entries.items()))

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'

        Erros identificados:
            Não há verificação se o nome existe no
            phonebook antes de tentar removê-lo

        Pontos de melhoria:
            Verificar se o nome existe antes de tentar removê-lo.
        """
        if name in self.entries:
            self.entries.pop(name)
            return "Número deletado"
        return "Nome não encontrado"

    def change_number(self, name, number):
        if name not in self.entries:
            return "Nome não encontrado"
        self.entries[name] = number
        return "Número atualizado"

    def get_name_by_number(self, number):
        for name in self.entries:
            if self.entries[name] == number:
                return name
        return "Número não encontrado"
