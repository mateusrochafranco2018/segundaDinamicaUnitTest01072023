from src.phonebook import Phonebook


class TestPhonebook:
    def test_adicionar_contato(self):
        resultado_esperado = "Numero adicionado"
        phonebook = Phonebook()
        resultado = phonebook.adicionar_contato('Miguel', '468791681')
        assert resultado_esperado == resultado

    def test_adicionar_contato_duplicate_name(self):
        resultado_esperado = 'Nome duplicado'
        phonebook = Phonebook()
        phonebook.adicionar_contato('Arthur', '210051395')
        resultado = phonebook.adicionar_contato('Arthur', 'Arthur')
        assert resultado_esperado == resultado

    def test_adicionar_contato_duplicate_numero_do_contato(self):
        resultado_esperado = 'Numero duplicado'
        phonebook = Phonebook()
        phonebook.adicionar_contato('Gael', '245902673')
        resultado = phonebook.adicionar_contato('Théo', '245902673')
        assert resultado_esperado == resultado

    def test_nome_invalido_hash(self):  # teste com #
        resultado_esperado = "Nome invalido"
        phonebook = Phonebook()
        resultado = phonebook.adicionar_contato('#', '403496019')
        assert resultado_esperado == resultado

    def test_nome_invalido_at(self):  # teste com @
        resultado_esperado = "Nome invalido"
        phonebook = Phonebook()
        resultado = phonebook.adicionar_contato('@', '113645776')
        assert resultado_esperado == resultado

    def test_nome_invalido_exclamation(self):  # teste com !
        resultado_esperado = "Nome invalido"
        phonebook = Phonebook()
        resultado = phonebook.adicionar_contato('!', '488543654')
        assert resultado_esperado == resultado

    def test_nome_invalido_dolar(self):  # teste com $
        resultado_esperado = "Nome invalido"
        phonebook = Phonebook()
        resultado = phonebook.adicionar_contato('$', '126712724')  # Corrigido: troquei '!' por '$'
        assert resultado_esperado == resultado

    def test_nome_invalido_percent(self):  # teste com %
        resultado_esperado = "Nome invalido"
        phonebook = Phonebook()
        resultado = phonebook.adicionar_contato('%', '243122494')
        assert resultado_esperado == resultado

    def test_numero_invalido(self):
        resultado_esperado = "Numero invalido"
        phonebook = Phonebook()
        resultado = phonebook.adicionar_contato('Heitor', '')
        assert resultado_esperado == resultado

    def test_lookup(self):
        resultado_esperado = '254401016'
        phonebook = Phonebook()
        phonebook.adicionar_contato('Ravi', '254401016')
        resultado = phonebook.lookup('Ravi')
        assert resultado_esperado == resultado

    def test_lookup_nome_invalido(self):
        resultado_esperado = 'Nome invalido'
        phonebook = Phonebook()
        phonebook.adicionar_contato('Davi', '138156657')
        resultado = phonebook.lookup('@')
        assert resultado_esperado == resultado

    def test_get_names(self):
        resultado_esperado = ['Bernardo', 'Noah']
        phonebook = Phonebook()
        phonebook.adicionar_contato('Bernardo', '447200070')
        phonebook.adicionar_contato('Noah', '311234641')
        resultado = list(phonebook.get_nome_dos_contatos())
        assert resultado_esperado == resultado

    def test_get_numero_dos_contatos(self):
        resultado_esperado = ['194583703', '454953033']
        phonebook = Phonebook()
        phonebook.adicionar_contato('Gabriel', '194583703')
        phonebook.adicionar_contato('Helena', '454953033')
        resultado = list(phonebook.get_numero_dos_contatos())
        assert resultado_esperado == resultado

    def test_clear(self):
        phonebook = Phonebook()
        phonebook.adicionar_contato('Alice', '362409249')
        phonebook.adicionar_contato('Laura', '312615644')
        resultado_esperado = 'Phonebook limpo'
        phonebook = Phonebook()
        resultado = phonebook.clear()
        assert resultado_esperado == resultado

    def test_search(self):
        resultado_esperado = [{'Maria Alice': '120622798'}, {'Sophia': '480578989'}]
        phonebook = Phonebook()
        phonebook.adicionar_contato('Maria Alice', '120622798')
        phonebook.adicionar_contato('Sophia', '480578989')
        resultado = phonebook.search('a')
        assert resultado_esperado == resultado

    def test_get_phonebook_sorted(self):
        resultado_esperado = {'Manuela': '354874391', 'Maitê': '148941400', 'Liz': '159716391'}
        phonebook = Phonebook()
        phonebook.adicionar_contato('Manuela', '354874391')
        phonebook.adicionar_contato('Maitê', '148941400')
        phonebook.adicionar_contato('Liz', '159716391')
        resultado = phonebook.get_phonebook_sorted()
        assert resultado_esperado == resultado

    def test_get_phonebook_reverse(self):
        resultado_esperado = {'Cecília': '107335086', 'Isabella': '346679928', 'Yuri': '236306923'}
        phonebook = Phonebook()
        phonebook.adicionar_contato('Cecília', '107335086')
        phonebook.adicionar_contato('Isabella', '346679928')
        phonebook.adicionar_contato('Yuri', '236306923')
        resultado = phonebook.get_phonebook_reverse()
        assert resultado_esperado == resultado

    def test_delete_existing(self):
        resultado_esperado = 'Contato excluido'
        phonebook = Phonebook()
        phonebook.adicionar_contato('Benjamin', '196540616')
        resultado = phonebook.delete('Benjamin')
        assert resultado_esperado == resultado

    def test_delete_non_existing(self):
        resultado_esperado = 'Contato não encontrado'
        phonebook = Phonebook()
        phonebook.adicionar_contato('Erick', '98765432')
        resultado = phonebook.delete('Fernando')
        assert resultado_esperado == resultado

    def test_search_empty_phonebook(self):
        resultado_esperado = []
        phonebook = Phonebook()
        resultado = phonebook.search('a')
        assert resultado_esperado == resultado

    def test_get_phonebook_sorted_empty(self):
        resultado_esperado = {'Francisco': '476659449', 'Rodrigo': '447093368', 'Tomás': '319306744'}
        phonebook = Phonebook()
        phonebook.adicionar_contato('Tomás', '319306744')
        phonebook.adicionar_contato('Francisco', '476659449')
        phonebook.adicionar_contato('Rodrigo', '447093368')
        resultado = phonebook.get_phonebook_sorted()
        assert resultado_esperado == resultado

    def test_get_phonebook_reverse_empty(self):
        resultado_esperado = {}
        phonebook = Phonebook()
        resultado = phonebook.get_phonebook_reverse()
        assert resultado_esperado == resultado

    def test_adicionar_contato_empty_name(self):
        resultado_esperado = "Nome invalido"
        phonebook = Phonebook()
        resultado = phonebook.adicionar_contato('', '496112569')
        assert resultado_esperado == resultado

    def test_adicionar_contato_empty_numero_do_contato(self):
        resultado_esperado = "Numero invalido"
        phonebook = Phonebook()
        resultado = phonebook.adicionar_contato('Juan', '')
        assert resultado_esperado == resultado

    def test_lookup_non_existing_name(self):
        resultado_esperado = 'Nome invalido'
        phonebook = Phonebook()
        phonebook.adicionar_contato('João Guilherme', '275213754')
        resultado = phonebook.lookup('Diogo')
        assert resultado_esperado == resultado

    def test_get_names_empty_phonebook(self):
        resultado_esperado = []
        phonebook = Phonebook()
        resultado = list(phonebook.get_nome_dos_contatos())
        assert resultado_esperado == resultado

    def test_get_numero_dos_contatos_empty_phonebook(self):
        resultado_esperado = []
        phonebook = Phonebook()
        resultado = list(phonebook.get_numero_dos_contatos())
        assert resultado_esperado == resultado

    def test_clear_empty_phonebook(self):
        phonebook = Phonebook()
        phonebook.adicionar_contato('Otávio', '110217111')
        phonebook.adicionar_contato('Nathan', '425821043')
        phonebook.adicionar_contato('Calebe', '318678111')
        resultado_esperado = 'Phonebook limpo'

        resultado = phonebook.clear()
        assert resultado_esperado == resultado

    def test_search_non_existing_name(self):
        resultado_esperado = []
        phonebook = Phonebook()
        phonebook.adicionar_contato('Danilo', '237593567')
        resultado = phonebook.search('Luan')
        assert resultado_esperado == resultado

    def test_delete_empty_phonebook(self):
        resultado_esperado = 'Contato não encontrado'
        phonebook = Phonebook()
        resultado = phonebook.delete('Kaique')
        assert resultado_esperado == resultado



    def test_lookup_empty_phonebook(self):
        resultado_esperado = 'Nome invalido'
        phonebook = Phonebook()
        resultado = phonebook.lookup('Alexandre')
        assert resultado_esperado == resultado

    def test_get_phonebook_sorted_duplicate_entries(self):
        resultado_esperado = {'Iago': '507155154', 'Ricardo': '402090433'}
        phonebook = Phonebook()
        phonebook.adicionar_contato('Iago', '507155154')
        phonebook.adicionar_contato('Ricardo', '402090433')
        phonebook.adicionar_contato('Iago', '507155154')
        resultado = phonebook.get_phonebook_sorted()
        assert resultado_esperado == resultado

    def test_get_phonebook_reverse_duplicate_entries(self):
        resultado_esperado = {'Marcelo': '263447625', 'Cauê': '98765432'}
        phonebook = Phonebook()
        phonebook.adicionar_contato('Marcelo', '263447625')
        phonebook.adicionar_contato('Cauê', '98765432')
        phonebook.adicionar_contato('Marcelo', '263447625')
        resultado = phonebook.get_phonebook_reverse()
        assert resultado_esperado == resultado

    def test_change_numero_do_contato(self):
        resultado_esperado = 'Numero alterado'
        phonebook = Phonebook()
        phonebook.adicionar_contato('Benício', '435194094')
        resultado = phonebook.change_numero_do_contato('Benício', '256282651')
        assert resultado_esperado == resultado

    def test_change_numero_do_contato_contact_not_found(self):
        resultado_esperado = 'Contato não encontrado'
        phonebook = Phonebook()
        resultado = phonebook.change_numero_do_contato('Augusto', '147650549')
        assert resultado_esperado == resultado

    def test_get_name_by_numero_do_contato(self):
        resultado_esperado = 'Giovanni'
        phonebook = Phonebook()
        phonebook.adicionar_contato('Giovanni', '352622519')
        resultado = phonebook.get_nome_do_contato_by_numero_do_contato('352622519')
        assert resultado_esperado == resultado

    def test_get_name_by_numero_do_contato_numero_do_contato_not_found(self):
        phonebook = Phonebook()
        phonebook.adicionar_contato('Renato', '152239121')
        resultado_esperado = 'Numero não encontrado'

        resultado = phonebook.get_nome_do_contato_by_numero_do_contato('286291423')
        assert resultado_esperado == resultado
