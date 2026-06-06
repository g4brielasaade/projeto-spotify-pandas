"""
Spotify Insights — Projeto Pandas Harve
========================================

App Streamlit que serve de palco para os exercícios das aulas 2, 3 e 4.

Você NÃO precisa mexer neste arquivo. Toda a lógica que você vai escrever
está em exercicios/aula2.py, aula3.py e aula4.py.

Para rodar:
    streamlit run app.py
"""

from pathlib import Path

import pandas as pd
import streamlit as st

from exercicios import aula2, aula3, aula4

# ------------------------------------------------------------------
# Configuração geral
# ------------------------------------------------------------------
st.set_page_config(
    page_title="Spotify Insights — Pandas Harve",
    page_icon="🎵",
    layout="wide",
)

DATA_DIR = Path(__file__).parent / "data"
CSV_PRINCIPAL = DATA_DIR / "spotify-2023.csv"
CSV_ARTISTAS = DATA_DIR / "artistas_info.csv"
CSV_NOVOS = DATA_DIR / "spotify_novos_lancamentos.csv"

st.title("🎵 Spotify Insights")
st.caption("Projeto do módulo de Pandas — Harve")


# ------------------------------------------------------------------
# Helper para chamar funções dos alunos sem quebrar o app
# ------------------------------------------------------------------
def safe_call(func, *args, **kwargs):
    """Executa a função do aluno; se der NotImplementedError, mostra aviso."""
    try:
        return func(*args, **kwargs), None
    except NotImplementedError as e:
        return None, f"⏳ {e}"
    except Exception as e:
        return None, f"❌ Erro: {type(e).__name__}: {e}"


# ------------------------------------------------------------------
# Carrega base principal (chama função do aluno - aula 2)
# ------------------------------------------------------------------
df, erro_carga = safe_call(aula2.carregar_e_limpar, str(CSV_PRINCIPAL))

if erro_carga:
    st.warning(
        "Para o app começar a funcionar, implemente primeiro a função "
        "`carregar_e_limpar` em **exercicios/aula2.py**."
    )
    st.info(erro_carga)
    st.stop()

st.success(f"Base carregada: {df.shape[0]} músicas, {df.shape[1]} colunas")

# ------------------------------------------------------------------
# Abas - uma por aula
# ------------------------------------------------------------------
aba2, aba3, aba4 = st.tabs([
    "Aula 2 — Explorador de Faixas",
    "Aula 3 — Análise do Catálogo",
    "Aula 4 — Visual + Export",
])

# ==================================================================
# ABA AULA 2
# ==================================================================
with aba2:
    st.header("Explorador de Faixas")
    st.write("Exercícios de inspeção, filtros e criação de colunas.")

    col1, col2 = st.columns(2)

    # --- Inspecionar coluna ---
    with col1:
        st.subheader("🔎 Inspecionar coluna")
        coluna = st.selectbox("Escolha uma coluna:", df.columns, index=0)
        resultado, erro = safe_call(aula2.inspecionar_coluna, df, coluna)
        if erro:
            st.info(erro)
        else:
            st.write(resultado)

    # --- Filtro por artista ---
    with col2:
        st.subheader("🎤 Filtrar por artista")
        artista = st.text_input("Digite parte do nome do artista:", value="Taylor")
        if artista:
            resultado, erro = safe_call(aula2.filtrar_por_artista, df, artista)
            if erro:
                st.info(erro)
            else:
                st.write(f"{len(resultado)} música(s) encontrada(s)")
                st.dataframe(resultado[['track_name', 'artist(s)_name', 'released_year', 'streams']])

    st.divider()

    # --- Filtro AND ---
    st.subheader("⚡ Filtrar hits (AND)")
    c1, c2 = st.columns(2)
    ano_min = c1.number_input("Ano mínimo", min_value=1900, max_value=2025, value=2020)
    streams_min = c2.number_input("Streams mínimos", min_value=0, value=500_000_000, step=100_000_000)
    resultado, erro = safe_call(aula2.filtrar_hits, df, ano_min, streams_min)
    if erro:
        st.info(erro)
    else:
        st.write(f"{len(resultado)} hit(s)")
        st.dataframe(resultado[['track_name', 'artist(s)_name', 'released_year', 'streams']])

    st.divider()

    # --- Categoria ---
    st.subheader("🏷️ Categoria de streams")
    resultado, erro = safe_call(aula2.criar_categoria_streams, df)
    if erro:
        st.info(erro)
    else:
        st.write(resultado['categoria_streams'].value_counts())
        st.dataframe(resultado[['track_name', 'artist(s)_name', 'streams', 'categoria_streams']].head(20))


# ==================================================================
# ABA AULA 3
# ==================================================================
with aba3:
    st.header("Análise do Catálogo")
    st.write("Estatísticas e agrupamentos.")

    st.subheader("📊 Estatísticas gerais")
    resultado, erro = safe_call(aula3.estatisticas_gerais, df)
    if erro:
        st.info(erro)
    else:
        c1, c2, c3 = st.columns(3)
        c1.metric("Total de streams", f"{resultado['total_streams']:,}".replace(",", "."))
        c2.metric("BPM médio", f"{resultado['media_bpm']:.1f}")
        c3.metric("Danceability média", f"{resultado['media_danceability']:.1f}%")
        c4, c5 = st.columns(2)
        c4.metric("Ano mais antigo", resultado['ano_mais_antigo'])
        c5.metric("Ano mais recente", resultado['ano_mais_recente'])

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏆 Top N artistas por streams")
        n = st.slider("N", min_value=5, max_value=20, value=10)
        resultado, erro = safe_call(aula3.top_n_artistas_por_streams, df, n)
        if erro:
            st.info(erro)
        else:
            st.dataframe(resultado)

    with col2:
        st.subheader("🎼 Média de features por modo")
        resultado, erro = safe_call(aula3.media_features_por_modo, df)
        if erro:
            st.info(erro)
        else:
            st.dataframe(resultado)

    st.divider()

    st.subheader("📅 Lançamentos por ano")
    resultado, erro = safe_call(aula3.lancamentos_por_ano, df)
    if erro:
        st.info(erro)
    else:
        st.line_chart(resultado)

    st.subheader("🎯 Artista mais streamado em um ano")
    ano_escolhido = st.number_input("Ano:", min_value=1950, max_value=2025, value=2023, key="ano_artista")
    resultado, erro = safe_call(aula3.artista_mais_streamado_do_ano, df, int(ano_escolhido))
    if erro:
        st.info(erro)
    else:
        st.success(f"🥇 {resultado}")


# ==================================================================
# ABA AULA 4
# ==================================================================
with aba4:
    st.header("Dashboard Visual + Export")

    st.subheader("📊 Top artistas (gráfico de barras)")
    n_bar = st.slider("N", 5, 20, 10, key="n_barras")
    resultado, erro = safe_call(aula4.grafico_barras_top_artistas, df, n_bar)
    if erro:
        st.info(erro)
    else:
        st.pyplot(resultado)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🥧 Major x Minor (pizza)")
        resultado, erro = safe_call(aula4.grafico_pizza_modo, df)
        if erro:
            st.info(erro)
        else:
            st.pyplot(resultado)

    with col2:
        st.subheader("📈 Lançamentos por ano (linha)")
        resultado, erro = safe_call(aula4.grafico_linha_lancamentos_por_ano, df)
        if erro:
            st.info(erro)
        else:
            st.pyplot(resultado)

    st.divider()

    st.subheader("🔗 Juntar com info dos artistas (merge)")
    if CSV_ARTISTAS.exists():
        df_info = pd.read_csv(CSV_ARTISTAS, encoding='utf-8')
        resultado, erro = safe_call(aula4.juntar_com_info_artistas, df, df_info)
        if erro:
            st.info(erro)
        else:
            colunas_show = ['track_name', 'artist(s)_name', 'streams', 'pais_origem', 'gravadora']
            colunas_existentes = [c for c in colunas_show if c in resultado.columns]
            st.dataframe(resultado[colunas_existentes].head(20))

    st.subheader("➕ Unir novos lançamentos (concat)")
    if CSV_NOVOS.exists():
        df_novos = pd.read_csv(CSV_NOVOS, encoding='utf-8')
        df_novos['streams'] = pd.to_numeric(df_novos['streams'], errors='coerce')
        resultado, erro = safe_call(aula4.unir_novos_lancamentos, df, df_novos)
        if erro:
            st.info(erro)
        else:
            st.success(f"Base original: {len(df)} linhas. Após concat: {len(resultado)} linhas.")
            st.dataframe(resultado.tail(10)[['track_name', 'artist(s)_name', 'released_year', 'streams']])

    st.divider()

    st.subheader("💾 Exportar")
    if st.button("Exportar base limpa para CSV"):
        destino = Path(__file__).parent / "saida.csv"
        _, erro = safe_call(aula4.salvar_resultado, df, str(destino))
        if erro:
            st.info(erro)
        else:
            st.success(f"Arquivo salvo em {destino}")
            with open(destino, 'rb') as f:
                st.download_button("Baixar saida.csv", f, file_name="saida.csv")
