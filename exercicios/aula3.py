"""
AULA 3 — Análise do Catálogo
==============================

Tópicos aplicados:
- Resumo estatístico (sum, mean, max, min, describe)
- Agrupamento com groupby
- Ordenação com sort_values

Preencha as funções marcadas com `# TODO`.
"""

import pandas as pd


def estatisticas_gerais(df: pd.DataFrame) -> dict:
    """
    Retorna um dicionario com:

      {
        "total_streams":       soma de todos os streams,
        "media_bpm":           media da coluna bpm,
        "media_danceability":  media da coluna 'danceability_%',
        "ano_mais_recente":    maior valor de released_year,
        "ano_mais_antigo":     menor valor de released_year,
      }

    Dica: use .sum(), .mean(), .max(), .min().
    """
    # TODO: implemente
    raise NotImplementedError("Funcao estatisticas_gerais ainda nao implementada (aula 3)")


def top_n_artistas_por_streams(df: pd.DataFrame, n: int = 10) -> pd.Series:
    """
    Retorna uma Series com os N artistas que mais somam streams, em ordem
    decrescente.

    Passos:
      - groupby na coluna 'artist(s)_name'
      - somar a coluna 'streams'
      - sort_values em ordem decrescente
      - pegar os N primeiros (head)
    """
    # TODO: implemente
    raise NotImplementedError("Funcao top_n_artistas_por_streams ainda nao implementada (aula 3)")


def media_features_por_modo(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa o DataFrame pela coluna 'mode' (Major / Minor) e retorna a media
    das tres features:
      - 'danceability_%'
      - 'energy_%'
      - 'valence_%'

    Retorno: DataFrame com 2 linhas (Major e Minor) e 3 colunas.
    """
    # TODO: implemente
    raise NotImplementedError("Funcao media_features_por_modo ainda nao implementada (aula 3)")


def lancamentos_por_ano(df: pd.DataFrame) -> pd.Series:
    """
    Retorna uma Series com a contagem de musicas lancadas por ano, ordenada
    do ano mais antigo para o mais recente.

    Dica: groupby('released_year').size() ou value_counts(sort=False) com
    sort_index() depois.
    """
    # TODO: implemente
    raise NotImplementedError("Funcao lancamentos_por_ano ainda nao implementada (aula 3)")


def artista_mais_streamado_do_ano(df: pd.DataFrame, ano: int) -> str:
    """
    Retorna o nome do artista que mais somou streams em um determinado ano.

    Passos:
      1) Filtre o df pelo ano (released_year == ano).
      2) Agrupe por 'artist(s)_name' somando 'streams'.
      3) Ordene em ordem decrescente.
      4) Retorne o nome do primeiro (use .index[0]).

    Se nao houver musicas no ano, retorne uma string como
    "Nenhuma musica encontrada para {ano}".
    """
    # TODO: implemente
    raise NotImplementedError("Funcao artista_mais_streamado_do_ano ainda nao implementada (aula 3)")
