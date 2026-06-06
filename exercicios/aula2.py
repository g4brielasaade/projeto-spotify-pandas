"""
AULA 2 - Explorador de Faixas
==============================

Topicos aplicados:
- Inspecao de conteudo (describe, value_counts)
- Atribuicao e criacao de colunas
- Filtros simples e com AND/OR
- Dados faltantes e duplicados

Preencha as funcoes marcadas com `# TODO`.
"""

import pandas as pd


def carregar_e_limpar(caminho_csv: str) -> pd.DataFrame:
    """
    Carrega o CSV do Spotify e limpa os dados.

    Passos:
      1) Ler o CSV com encoding='latin-1'.
      2) Converter 'streams' para numero (pd.to_numeric com errors='coerce').
      3) Remover linhas com streams nulos (dropna).
      4) Remover duplicatas (drop_duplicates).
      5) Retornar o DataFrame limpo.
    """
    # TODO: implemente
    raise NotImplementedError("Funcao carregar_e_limpar ainda nao implementada (aula 2)")


def inspecionar_coluna(df: pd.DataFrame, coluna: str):
    """
    Se a coluna for numerica, retorna df[coluna].describe().
    Caso contrario, retorna df[coluna].value_counts().

    Dica: use pd.api.types.is_numeric_dtype(df[coluna]).
    """
    # TODO: implemente
    raise NotImplementedError("Funcao inspecionar_coluna ainda nao implementada (aula 2)")


def filtrar_por_artista(df: pd.DataFrame, artista: str) -> pd.DataFrame:
    """
    Retorna apenas as linhas em que o nome do artista CONTEM o texto buscado
    (sem diferenciar maiusculas/minusculas).

    Dica: .str.contains(artista, case=False, na=False) na coluna 'artist(s)_name'.
    """
    # TODO: implemente
    raise NotImplementedError("Funcao filtrar_por_artista ainda nao implementada (aula 2)")


def filtrar_hits(df: pd.DataFrame, ano_min: int, streams_min: int) -> pd.DataFrame:
    """
    Filtro com AND: released_year >= ano_min E streams >= streams_min.

    Dica: use parenteses ao redor de cada expressao e o operador & .
    """
    # TODO: implemente
    raise NotImplementedError("Funcao filtrar_hits ainda nao implementada (aula 2)")


def criar_categoria_streams(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria uma coluna 'categoria_streams':
      - streams >= 1_000_000_000  -> 'Super Hit'
      - streams >= 500_000_000    -> 'Hit'
      - streams >= 100_000_000    -> 'Medio'
      - resto                     -> 'Underground'

    NAO altere o df original (use df.copy()).
    """
    # TODO: implemente
    raise NotImplementedError("Funcao criar_categoria_streams ainda nao implementada (aula 2)")


def filtrar_por_modo(df: pd.DataFrame, modo: str) -> pd.DataFrame:
    """
    Filtra o DataFrame por modo musical: 'Major' ou 'Minor'.

    Dica: filtro simples df[df['mode'] == modo].
    """
    # TODO: implemente
    raise NotImplementedError("Funcao filtrar_por_modo ainda nao implementada (aula 2)")


def filtrar_por_intervalo_ano(df: pd.DataFrame, ano_inicio: int, ano_fim: int) -> pd.DataFrame:
    """
    Retorna as musicas lancadas entre ano_inicio e ano_fim (inclusivo nos
    dois lados).

    Dica: pode usar .between(ano_inicio, ano_fim) ou um AND com >= e <=.
    """
    # TODO: implemente
    raise NotImplementedError("Funcao filtrar_por_intervalo_ano ainda nao implementada (aula 2)")


def filtrar_super_dancante_ou_super_energica(df: pd.DataFrame, limite: int = 85) -> pd.DataFrame:
    """
    Filtro com OR: retorna musicas em que 'danceability_%' >= limite OU
    'energy_%' >= limite.

    Dica: use o operador | (pipe) entre as expressoes, com parenteses ao
    redor de cada uma.
    """
    # TODO: implemente
    raise NotImplementedError("Funcao filtrar_super_dancante_ou_super_energica ainda nao implementada (aula 2)")


def contar_nulos_por_coluna(df: pd.DataFrame) -> pd.Series:
    """
    Retorna uma Series com o nome de cada coluna e a quantidade de valores
    nulos.

    Dica: df.isnull().sum().
    """
    # TODO: implemente
    raise NotImplementedError("Funcao contar_nulos_por_coluna ainda nao implementada (aula 2)")


def preencher_nulos_da_coluna(df: pd.DataFrame, coluna: str, valor) -> pd.DataFrame:
    """
    Preenche os valores nulos da coluna informada com o valor passado.

    Exemplo:
      preencher_nulos_da_coluna(df, 'key', 'Desconhecido')

    NAO altere o df original. Retorne uma copia.

    Dica: df_novo = df.copy(); df_novo[coluna] = df_novo[coluna].fillna(valor).
    """
    # TODO: implemente
    raise NotImplementedError("Funcao preencher_nulos_da_coluna ainda nao implementada (aula 2)")
