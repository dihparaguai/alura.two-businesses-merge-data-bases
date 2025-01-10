import json
import csv


# funcoes de leitura, transformacao e disponilbização
def leitura_json(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    return dados_json


def leitura_csv(path_csv):
    dados_csv = []
    with open(path_csv, 'r') as file:
        dados_csv = csv.DictReader(file, delimiter=',')
        dados_csv = list(dados_csv)
    return dados_csv


def leitura_dados(path, tipo_arquivo):
    if tipo_arquivo == 'csv':
        return leitura_csv(path)
    if tipo_arquivo == 'json':
        return leitura_json(path)


def get_columns_name(dados):
    return list(dados[0].keys())


def rename_columns(dados, key_mapping):
    new_dados = []

    for old_dict in dados:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_dados.append(dict_temp)
    
    return new_dados


def size_dados(dados):
    return len(dados)


def join_dados(dadosA, dadosB):
    qtd_colunas_dadosA = size_dados(get_columns_name(dadosA))
    qtd_colunas_dadosB = size_dados(get_columns_name(dadosB))
    
    new_dados = []
    
    if qtd_colunas_dadosA > qtd_colunas_dadosB:
        new_dados.extend(dadosA)
        new_dados.extend(dadosB)
        return new_dados
    
    new_dados.extend(dadosB)
    new_dados.extend(dadosA)
    return new_dados


def listdict_to_listlist(dados):
    new_dados = [get_columns_name(dados)]
    
    for dict in dados:
        temp_lista = []
        for key in new_dados[0]:
            temp_lista.append(dict.get(key, 'indisponivel'))
        new_dados.append(temp_lista)
    
    return new_dados


def save_dados(path_dados, dados):
    with open(path_dados, 'w') as file:
        spamwriter = csv.writer(file)
        spamwriter.writerows(dados)


# leitura
path_empA = 'data_raw/dados_empresaA.json'
path_empB = 'data_raw/dados_empresaB.csv'

dados_empA = leitura_dados(path_empA, 'json')
dados_empB = leitura_dados(path_empB, 'csv')

print(f'nome das colunas dos dados da empresa A: {get_columns_name(dados_empA)}')
print(f'nome das colunas dos dados da empresa B: {get_columns_name(dados_empB)}')



# transformação
key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'}

dados_empB = rename_columns(dados_empB, key_mapping)

print(f'qtd de linhas dos dados da empresa A: {size_dados(dados_empA)}')
print(f'qtd de linhas dos dados da empresa B: {size_dados(dados_empB)}')

dados_fusao = join_dados(dados_empA, dados_empB)
print(f'qtd de linhas dos dados da fusao: {size_dados(dados_fusao)}')



# salvar
path_dados_fusao_tabela = 'data_processed/dados_combinados_4.csv'

dados_fusao_tabela = listdict_to_listlist(dados_fusao)

save_dados(path_dados_fusao_tabela, dados_fusao_tabela)