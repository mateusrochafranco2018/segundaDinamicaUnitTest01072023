class Phonebook:
    def __init__(self):
        self.entries = {}

    def adicionar_contato(self, nome_do_contato, numero_do_contato):
        if self.nome_invalido(nome_do_contato):
            return 'Nome invalido'

        if len(numero_do_contato) == 0:
            return 'Numero invalido'

        if nome_do_contato in self.entries:
            return 'Nome duplicado'

        if any(value == numero_do_contato for value in self.entries.values()):
            return 'Numero duplicado'

        self.entries[nome_do_contato] = numero_do_contato
        return 'Numero adicionado'

    def lookup(self, nome_do_contato):
        if self.nome_invalido(nome_do_contato) or nome_do_contato not in self.entries:
            return 'Nome invalido'
        return self.entries[nome_do_contato]

    def nome_invalido(self, nome_do_contato):
        if len(nome_do_contato.strip()) == 0:  # Verifica se o nome está em branco
            return True

        invalid_characters = ['#', '@', '!', '$', '%']
        for char in invalid_characters:
            if char in nome_do_contato:
                return True
        return False

    def get_nome_dos_contatos(self):
        if self.is_empty():
            return []
        return list(self.entries.keys())

    def get_numero_dos_contatos(self):
        if self.is_empty():
            return []
        return list(self.entries.values())

    def is_empty(self):
        return len(self.entries) == 0

    def clear(self):
        self.entries = {}
        return 'Phonebook limpo'

    def search(self, search_nome_do_contato):
        result = []
        for nome_do_contato, numero_do_contato in self.entries.items():
            if search_nome_do_contato in nome_do_contato:
                result.append({nome_do_contato: numero_do_contato})
        return result

    def get_phonebook_sorted(self):
        if self.is_empty():
            return {}
        return dict(sorted(self.entries.items()))

    def get_phonebook_reverse(self):
        if self.is_empty():
            return {}
        return dict(sorted(self.entries.items(), reverse=True))

    def delete(self, nome_do_contato):
        if nome_do_contato in self.entries:
            del self.entries[nome_do_contato]
            return 'Contato excluido'
        return 'Contato não encontrado'

    def change_numero_do_contato(self, nome_do_contato, numero_do_contato):
        if nome_do_contato in self.entries:
            self.entries[nome_do_contato] = numero_do_contato
            return 'Numero alterado'
        return 'Contato não encontrado'

    def get_nome_do_contato_by_numero_do_contato(self, numero_do_contato):
        for nome_do_contato, num in self.entries.items():
            if num == numero_do_contato:
                return nome_do_contato
        return 'Numero não encontrado'
