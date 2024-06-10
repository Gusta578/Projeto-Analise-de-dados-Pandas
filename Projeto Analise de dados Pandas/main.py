import pandas as pd
from IPython.display import display

def dados_paises():
    # Dataframe ficticio com paises e valores ficticios!
    dados_paises = pd.DataFrame({
        'País': ['Brasil', 'EUA', 'China', 'Índia', 'Alemanha'],
        'População (milhões)': [213, 331, 1441, 1380, 83],
        'PIB (trilhões USD)': [2.14, 21.43, 14.34, 2.87, 4.42],
        'IDH': [0.759, 0.926, 0.761, 0.645, 0.947]
    })

    # Usado para exibir as primeiras linhas do dataframe
    print("Primeiras linhas do DataFrame:")
    display(dados_paises.head())

    # Exibir as informações completas do dataframe
    print("\nInformações sobre o DataFrame:")
    display(dados_paises.info())

    # Fazer analise simples.
    print("\nAnálises simples:")
    print("Número total de países:", len(dados_paises))
    print("Número de colunas:", len(dados_paises.columns))
    print("Valores únicos na coluna 'País':", dados_paises['País'].nunique())
    print("Estatísticas descritivas para a coluna 'População (milhões)':")
    display(dados_paises['População (milhões)'].describe())

    # Ordenar os paises por informação
    print("\nPaíses ordenados por PIB:")
    paises_ordenados = dados_paises.sort_values(by='PIB (trilhões USD)')
    display(paises_ordenados[['País', 'PIB (trilhões USD)']])

if __name__ == "info":
    dados_paises()
