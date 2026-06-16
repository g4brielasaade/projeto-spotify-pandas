"""
AULA 3 - Analise do Catalogo
==============================

Topicos aplicados:
- Resumo estatistico (sum, mean, max, min, describe)
- Agrupamento com groupby
- Ordenacao com sort_values

Preencha as funcoes marcadas com `# TODO`.
"""

import pandas as pd


def estatisticas_gerais(df: pd.DataFrame) -> dict:
    """
    Retorna um dicionario com:
      - total_streams: soma de streams
      - media_bpm: media de bpm
      - media_danceability: media de 'danceability_%'
      - ano_mais_recente: maior released_year
      - ano_mais_antigo: menor released_year
    """

    return {
        'total_streams': df['streams'].sum(),
        'media_bpm': df['bpm'].mean(),
        'media_danceability': df['danceability_%'].mean(),
        'ano_mais_recente': df['released_year'].max(),
        'ano_mais_antigo': df['released_year'].min()
    }

    # TODO: implemente
    raise NotImplementedError("Funcao estatisticas_gerais ainda nao implementada (aula 3)")


def top_n_artistas_por_streams(df: pd.DataFrame, n: int = 10) -> pd.Series:
    """
    Retorna uma Series com os N artistas que mais somam streams, em ordem
    decrescente.

    Passos: groupby + sum + sort_values + head.
    """

    return df.groupby('artist(s)_name')['streams'].sum().sort_values(ascending=False).head(n)

    # TODO: implemente
    raise NotImplementedError("Funcao top_n_artistas_por_streams ainda nao implementada (aula 3)")


def media_features_por_modo(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa por 'mode' (Major / Minor) e retorna a media de:
      - 'danceability_%'
      - 'energy_%'
      - 'valence_%'
    """
    return df.groupby('mode')[['danceability_%', 'energy_%', 'valence_%']].mean()


    # TODO: implemente
    raise NotImplementedError("Funcao media_features_por_modo ainda nao implementada (aula 3)")


def lancamentos_por_ano(df: pd.DataFrame) -> pd.Series:
    """
    Contagem de musicas lancadas por ano, ordenada do ano mais antigo para
    o mais recente.

    Dica: groupby('released_year').size().
    """
    return df.groupby('released_year').size().sort_index()

    # TODO: implemente
    raise NotImplementedError("Funcao lancamentos_por_ano ainda nao implementada (aula 3)")


def artista_mais_streamado_do_ano(df: pd.DataFrame, ano: int) -> str:
    """
    Retorna o nome do artista que mais somou streams em um ano.

    Passos: filtrar pelo ano -> groupby + sum -> sort -> pegar o primeiro.

    Se nao houver musicas no ano, retornar "Nenhuma musica encontrada para {ano}".
    """

    df_ano = df[df['released_year'] == ano]
    if df_ano.empty:
        return f"Nenhuma musica encontrada para {ano}"
    artista_mais_streamado = df_ano.groupby('artist(s)_name')['streams'].sum().idxmax()
    return artista_mais_streamado

    # TODO: implemente
    raise NotImplementedError("Funcao artista_mais_streamado_do_ano ainda nao implementada (aula 3)")


def top_n_musicas_mais_dancantes(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """
    Retorna as N musicas com maior 'danceability_%', em ordem decrescente.

    Devolva um DataFrame com colunas ['track_name', 'artist(s)_name',
    'danceability_%'].

    Dica: sort_values na coluna 'danceability_%' com ascending=False, depois
    head(n) e selecionar as colunas.
    """

    return df.sort_values('danceability_%', ascending=False).head(n)[['track_name', 'artist(s)_name', 'danceability_%']]
    

    # TODO: implemente
    raise NotImplementedError("Funcao top_n_musicas_mais_dancantes ainda nao implementada (aula 3)")


def streams_por_decada(df: pd.DataFrame) -> pd.Series:
    """
    Agrupa por DECADA de lancamento e retorna a soma de streams por decada.

    Exemplo: ano 2017 -> decada 2010; ano 1985 -> decada 1980.

    Dica: crie uma coluna auxiliar `decada = (released_year // 10) * 10` no
    DataFrame (use df.copy() para nao alterar o original). Depois groupby
    na decada somando streams. Ordene por decada (sort_index).
    """

    df_copy = df.copy()
    df_copy['decada'] = (df_copy['released_year'] // 10) * 10
    return df_copy.groupby('decada')['streams'].sum().sort_index()

    # TODO: implemente
    raise NotImplementedError("Funcao streams_por_decada ainda nao implementada (aula 3)")


def bpm_medio_por_modo(df: pd.DataFrame) -> pd.Series:
    """
    Retorna uma Series com o BPM medio para cada modo (Major e Minor).

    Dica: groupby('mode')['bpm'].mean().
    """
    return df.groupby('mode')['bpm'].mean()

    # TODO: implemente
    raise NotImplementedError("Funcao bpm_medio_por_modo ainda nao implementada (aula 3)")


def musicas_por_quantidade_de_artistas(df: pd.DataFrame) -> pd.Series:
    """
    Quantas musicas tem 1 artista, 2 artistas, 3 artistas... (colaboracoes).

    Retorne uma Series indexada por 'artist_count' com a contagem de musicas
    de cada categoria, ordenada por quantidade de artistas (ascendente).

    Dica: value_counts() na coluna 'artist_count', depois sort_index().
    """

    return df['artist_count'].value_counts().sort_index()

    # TODO: implemente
    raise NotImplementedError("Funcao musicas_por_quantidade_de_artistas ainda nao implementada (aula 3)")


def ano_com_mais_streams(df: pd.DataFrame) -> int:
    """
    Retorna o ANO em que a soma total de streams (de musicas lancadas
    naquele ano) foi a maior.

    Passos: groupby('released_year') somando streams -> .idxmax()
    """

    return df.groupby('released_year')['streams'].sum().idxmax()

    # TODO: implemente
    raise NotImplementedError("Funcao ano_com_mais_streams ainda nao implementada (aula 3)")
