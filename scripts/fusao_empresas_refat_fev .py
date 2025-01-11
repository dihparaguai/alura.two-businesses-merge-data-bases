from processamento_dados import Dados


# leitura
path_empA = 'data_raw/dados_empresaA.json'
path_empB = 'data_raw/dados_empresaB.csv'

dados_empA = Dados(path_empA, 'json')
dados_empB = Dados(path_empB, 'csv')

print(f'nome das colunas dos dados da empresa A: {dados_empA.nome_colunas}')
print(f'nome das colunas dos dados da empresa B: {dados_empB.nome_colunas}')


# transformação
key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

dados_empB.renomear_colunas(key_mapping)
print(
    f'novo nome das colunas dos dados da empresa B: {dados_empA.nome_colunas}')

print(
    f'qtd de linhas dos dados da empresa A: {dados_empA.quantidade_registros}')
print(
    f'qtd de linhas dos dados da empresa B: {dados_empB.quantidade_registros}')

dados_fusao = Dados.join_dados(dados_empA, dados_empB)
print(f'nome das colunas dos dados da fusao: {dados_fusao.nome_colunas}')
print(f'qtd de linhas dos dados da fusao: {dados_fusao.quantidade_registros}')


# salvar
path_dados_fusao_tabela = 'data_processed/dados_combinados_5.csv'
dados_fusao.save_dados(path_dados_fusao_tabela)


# teste
path_empA_csv = 'data_raw/dados_empresaA_csv.csv'
dados_empA.save_dados(path_empA_csv)