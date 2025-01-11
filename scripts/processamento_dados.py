import json
import csv


class Dados():
    def __init__(self, path, ext):
        self.path = path
        self.ext = ext
        self.dados = self.leitura_dados()
        self.nome_colunas = self.obter_nome_colunas()
        self.quantidade_registros = self.obter_quantidade_registros()

    def leitura_json(self):
        with open(self.path, 'r') as file:
            dados = json.load(file)
        return dados

    def leitura_csv(self):
        with open(self.path, 'r') as file:
            dados = csv.DictReader(file, delimiter=',')
            dados = list(dados)
        return dados

    def leitura_dados(self):
        if self.ext == 'csv':
            dados = self.leitura_csv()
        elif self.ext == 'json':
            dados = self.leitura_json()
        elif self.ext == 'list':
            dados = self.path
            self.path = 'lista em memoria'
        return dados

    def obter_nome_colunas(self):
        return list(self.dados[0].keys())

    def renomear_colunas(self, key_mapping):
        new_dados = []

        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados.append(dict_temp)

        self.dados = new_dados

    def obter_quantidade_registros(self):
        return len(self.dados)

    def join_dados(left, right):
        new_dados = []

        if len(left.nome_colunas) > len(right.nome_colunas):
            new_dados.extend(left.dados)
            new_dados.extend(right.dados)

        else:
            new_dados.extend(right.dados)
            new_dados.extend(left.dados)

        return Dados(new_dados, 'list')

    def listdict_to_listlist(self):
        new_dados = [self.nome_colunas]

        for dict in self.dados:
            temp_lista = []
            for key in new_dados[0]:
                temp_lista.append(dict.get(key, 'indisponivel'))
            new_dados.append(temp_lista)

        return new_dados

    def save_dados(self, new_path):
        dados = self.listdict_to_listlist()
        with open(new_path, 'w') as file:
            spamwriter = csv.writer(file)
            spamwriter.writerows(dados)