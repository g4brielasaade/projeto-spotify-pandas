"""
AULA 4 — Dashboard Visual + Export
====================================

Tópicos aplicados:
- Visualização de dados (matplotlib)
- Conectando dados (concat e merge)
- Salvando dados (to_csv)

As funcoes de grafico devem RETORNAR a figura matplotlib (fig), nao chamar
plt.show(). O Streamlit cuida de exibir.
"""

import pandas as pd
import matplotlib.pyplot as plt


def grafico_barras_top_artistas(df: pd.DataFrame, n: int = 10):
    """
    Cria um grafico de barras horizontais com os N artistas que mais somam
    streams.

    Passos:
      1) Agrupar por 'artist(s)_name', somar 'streams', ordenar, pegar os
         N primeiros. (Pode reaproveitar a logica da aula 3.)
      2) Criar uma figura com fig, ax = plt.subplots(figsize=(10, 6)).
      3) Chamar ax.barh(...) passando os nomes e valores.
      4) Ajustar titulo e labels (set_title, set_xlabel, set_ylabel).
      5) Retornar a figura (fig).
    """
    # TODO: implemente
    raise NotImplementedError("Funcao grafico_barras_top_artistas ainda nao implementada (aula 4)")


def grafico_pizza_modo(df: pd.DataFrame):
    """
    Grafico de pizza com a proporcao de musicas em modo 'Major' x 'Minor'.

    Passos:
      1) Contar quantas musicas ha de cada modo (value_counts() na coluna 'mode').
      2) Criar figura com fig, ax = plt.subplots().
      3) Chamar ax.pie(valores, labels=rotulos, autopct='%1.1f%%').
      4) Adicionar titulo.
      5) Retornar fig.
    """
    # TODO: implemente
    raise NotImplementedError("Funcao grafico_pizza_modo ainda nao implementada (aula 4)")


def grafico_linha_lancamentos_por_ano(df: pd.DataFrame):
    """
    Grafico de linha com a quantidade de lancamentos por ano (apenas anos
    >= 2000, para o grafico nao ficar esticado).

    Passos:
      1) Filtrar df para released_year >= 2000.
      2) Contar lancamentos por ano.
      3) Ordenar por ano (sort_index).
      4) Criar figura, plotar com ax.plot(x, y, marker='o').
      5) Titulo e labels. Retornar fig.
    """
    # TODO: implemente
    raise NotImplementedError("Funcao grafico_linha_lancamentos_por_ano ainda nao implementada (aula 4)")


def juntar_com_info_artistas(df_spotify: pd.DataFrame, df_info: pd.DataFrame) -> pd.DataFrame:
    """
    Faz um MERGE entre o DataFrame do Spotify e o de informacoes dos
    artistas (pais_origem, gravadora, decada_estreia).

    Atencao: as colunas tem nomes diferentes!
      - No df_spotify, o artista esta em 'artist(s)_name'.
      - No df_info, esta em 'artist_name'.

    Use pd.merge(... left_on='artist(s)_name', right_on='artist_name',
    how='left'). Por que how='left'? Para nao perder musicas cujo artista
    nao esteja na tabela de info.
    """
    # TODO: implemente
    raise NotImplementedError("Funcao juntar_com_info_artistas ainda nao implementada (aula 4)")


def unir_novos_lancamentos(df_atual: pd.DataFrame, df_novos: pd.DataFrame) -> pd.DataFrame:
    """
    Faz um CONCAT vertical (axis=0) entre o DataFrame atual e o dos novos
    lancamentos.

    Use pd.concat([df_atual, df_novos], axis=0, ignore_index=True).
    Depois do concat, REMOVA duplicatas (a base de novos contem uma
    duplicata proposital para praticar).
    """
    # TODO: implemente
    raise NotImplementedError("Funcao unir_novos_lancamentos ainda nao implementada (aula 4)")


def salvar_resultado(df: pd.DataFrame, caminho: str) -> None:
    """
    Salva o DataFrame em CSV no caminho informado, SEM o indice
    (index=False) e com encoding='utf-8'.
    """
    # TODO: implemente
    raise NotImplementedError("Funcao salvar_resultado ainda nao implementada (aula 4)")
