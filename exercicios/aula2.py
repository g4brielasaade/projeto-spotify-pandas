"""
AULA 2 — Explorador de Faixas
==============================

Tópicos aplicados:
- Inspeção de conteúdo (describe, value_counts)
- Atribuição e criação de colunas
- Filtros simples e com AND/OR
- Dados faltantes e duplicados

Preencha as funções marcadas com `# TODO`.
"""

import pandas as pd


def carregar_e_limpar(caminho_csv: str) -> pd.DataFrame:
    """
    Carrega o CSV do Spotify e limpa os dados.

    Passos esperados:
      1) Ler o CSV. ATENCAO: o arquivo tem caracteres acentuados; use
         encoding='latin-1' no pd.read_csv.
      2) A coluna 'streams' veio como texto (object). Converta para numero
         usando pd.to_numeric(..., errors='coerce') -- valores invalidos
         viram NaN.
      3) Remova as linhas com 'streams' nulos (dropna).
      4) Remova duplicatas (drop_duplicates).
      5) Retorne o DataFrame limpo.
    """
    # TODO: implemente
    raise NotImplementedError("Funcao carregar_e_limpar ainda nao implementada (aula 2)")


def inspecionar_coluna(df: pd.DataFrame, coluna: str):
    """
    Inspeciona uma coluna do DataFrame.

    Regra:
      - Se a coluna for numerica, retorne df[coluna].describe()
      - Caso contrario, retorne df[coluna].value_counts()

    Dica: use pd.api.types.is_numeric_dtype(df[coluna]).
    """
    # TODO: implemente
    raise NotImplementedError("Funcao inspecionar_coluna ainda nao implementada (aula 2)")


def filtrar_por_artista(df: pd.DataFrame, artista: str) -> pd.DataFrame:
    """
    Filtra o DataFrame retornando apenas as linhas em que o nome do artista
    CONTEM o texto buscado (sem diferenciar maiusculas/minusculas).

    Exemplo: filtrar_por_artista(df, "taylor") deve retornar tanto
    "Taylor Swift" quanto colaboracoes como "The Weeknd, Taylor Swift".

    Dica: use .str.contains(artista, case=False, na=False) na coluna
    'artist(s)_name'.
    """
    # TODO: implemente
    raise NotImplementedError("Funcao filtrar_por_artista ainda nao implementada (aula 2)")


def filtrar_hits(df: pd.DataFrame, ano_min: int, streams_min: int) -> pd.DataFrame:
    """
    Filtro com AND: retorna apenas as musicas que satisfazem AS DUAS condicoes:
      - released_year >= ano_min
      - streams >= streams_min

    Dica: lembre-se de usar parenteses ao redor de cada expressao e o
    operador & .
    """
    # TODO: implemente
    raise NotImplementedError("Funcao filtrar_hits ainda nao implementada (aula 2)")


def criar_categoria_streams(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria uma nova coluna 'categoria_streams' baseada no valor de streams:

      - streams >= 1_000_000_000  -> 'Super Hit'
      - streams >= 500_000_000    -> 'Hit'
      - streams >= 100_000_000    -> 'Medio'
      - resto                     -> 'Underground'

    Nao altere o df original -- devolva uma copia com a coluna nova.
    Dica: use df.copy() e depois .apply().
    """
    # TODO: implemente
    raise NotImplementedError("Funcao criar_categoria_streams ainda nao implementada (aula 2)")
