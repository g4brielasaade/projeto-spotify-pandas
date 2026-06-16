"""
AULA 4 - Dashboard Visual + Export
====================================

Topicos aplicados:
- Visualizacao de dados (matplotlib)
- Conectando dados (concat e merge)
- Salvando dados (to_csv, to_excel, download)

As funcoes de grafico devem RETORNAR a figura matplotlib (fig), nao chamar
plt.show(). O Streamlit cuida de exibir.
"""

import io
import pandas as pd
import matplotlib.pyplot as plt


def grafico_barras_top_artistas(df: pd.DataFrame, n: int = 10):
    """
    Grafico de barras horizontais com os N artistas que mais somam streams.

    Dica: ax.barh(...). Retorne fig (sem plt.show()).
    """
    top_artistas = df.groupby('artist(s)_name')['streams'].sum().sort_values(ascending=False).head(n)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_artistas.index, top_artistas.values)
    ax.set_xlabel('Total de Streams')
    ax.set_title(f'Top {n} Artistas por Streams')
    plt.gca().invert_yaxis()  # Inverte a ordem para o maior ficar no topo
    return fig


    # TODO: implemente
    raise NotImplementedError("Funcao grafico_barras_top_artistas ainda nao implementada (aula 4)")


def grafico_pizza_modo(df: pd.DataFrame):
    """
    Pizza com a proporcao de musicas em modo 'Major' x 'Minor'.

    Dica: ax.pie(valores, labels=rotulos, autopct='%1.1f%%').
    """

    contagem_modos = df['mode'].value_counts()
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(contagem_modos.values, labels=contagem_modos.index, autopct='%1.1f%%')
    ax.set_title('Proporcao de Musicas por Modo')
    return fig

    # TODO: implemente
    raise NotImplementedError("Funcao grafico_pizza_modo ainda nao implementada (aula 4)")


def grafico_linha_lancamentos_por_ano(df: pd.DataFrame):
    """
    Linha com a quantidade de lancamentos por ano (>= 2000).
    """
    lancamentos_por_ano = df[df['released_year'] >= 2000].groupby('released_year').size()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(lancamentos_por_ano.index, lancamentos_por_ano.values, marker='o')
    ax.set_xlabel('Ano de Lancamento')
    ax.set_ylabel('Quantidade de Lancamentos')
    ax.set_title('Lancamentos por Ano (>= 2000)')
    return fig


    # TODO: implemente
    raise NotImplementedError("Funcao grafico_linha_lancamentos_por_ano ainda nao implementada (aula 4)")


def juntar_com_info_artistas(df_spotify: pd.DataFrame, df_info: pd.DataFrame) -> pd.DataFrame:
    """
    MERGE entre Spotify e info dos artistas (pais_origem, gravadora, etc).
    No df_spotify a coluna do artista e 'artist(s)_name'; no df_info e 'artist_name'.
    Use how='left' para nao perder musicas.
    """
    # TODO: implemente
    raise NotImplementedError("Funcao juntar_com_info_artistas ainda nao implementada (aula 4)")


def unir_novos_lancamentos(df_atual: pd.DataFrame, df_novos: pd.DataFrame) -> pd.DataFrame:
    """
    CONCAT vertical (axis=0) entre df_atual e df_novos. Depois drop_duplicates.
    """
    # TODO: implemente
    raise NotImplementedError("Funcao unir_novos_lancamentos ainda nao implementada (aula 4)")


def salvar_resultado(df: pd.DataFrame, caminho: str) -> None:
    """
    Salva o DataFrame em CSV no caminho informado, sem indice e encoding utf-8.
    """
    # TODO: implemente
    raise NotImplementedError("Funcao salvar_resultado ainda nao implementada (aula 4)")


def grafico_dispersao_energia_dancabilidade(df: pd.DataFrame):
    """
    Scatter plot: eixo X = 'energy_%', eixo Y = 'danceability_%'.

    Passos:
      1) fig, ax = plt.subplots(figsize=(8, 6))
      2) ax.scatter(df['energy_%'], df['danceability_%'], alpha=0.5)
      3) Titulo e labels
      4) Retornar fig
    """
    # TODO: implemente
    raise NotImplementedError("Funcao grafico_dispersao_energia_dancabilidade ainda nao implementada (aula 4)")


def grafico_histograma_bpm(df: pd.DataFrame, bins: int = 30):
    """
    Histograma do BPM (batidas por minuto).

    Passos:
      1) fig, ax = plt.subplots()
      2) ax.hist(df['bpm'], bins=bins)
      3) Titulo e labels
      4) Retornar fig
    """
    # TODO: implemente
    raise NotImplementedError("Funcao grafico_histograma_bpm ainda nao implementada (aula 4)")


def salvar_em_excel(df: pd.DataFrame, caminho: str) -> None:
    """
    Salva o DataFrame em formato Excel (.xlsx) no caminho informado, sem
    indice.

    Dica: df.to_excel(caminho, index=False). Precisa do pacote openpyxl
    instalado (ja esta no requirements.txt).
    """
    # TODO: implemente
    raise NotImplementedError("Funcao salvar_em_excel ainda nao implementada (aula 4)")


def preparar_csv_para_download(df: pd.DataFrame) -> bytes:
    """
    Prepara o DataFrame como CSV pronto para ser baixado pelo botao
    st.download_button do Streamlit.

    DIFERENCA para salvar_resultado: aqui NAO escrevemos em arquivo. A funcao
    deve retornar os BYTES do CSV. O Streamlit recebe esses bytes diretamente.

    Passos:
      1) Use df.to_csv(index=False) (SEM passar caminho — retorna string).
      2) Converta a string para bytes com .encode('utf-8').
      3) Retorne os bytes.

    Exemplo de uso no Streamlit:
      bytes_csv = preparar_csv_para_download(df)
      st.download_button("Baixar", bytes_csv, "dados.csv", "text/csv")
    """
    # TODO: implemente
    raise NotImplementedError("Funcao preparar_csv_para_download ainda nao implementada (aula 4)")
