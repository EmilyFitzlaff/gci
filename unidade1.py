import pandas as pd 
import numpy as np
import streamlit as st 
import altair as alt 
import matplotlib.pyplot as plt 
import seaborn as sns 

@st.cache_data
def load_database():
    return pd.read_csv('brasil_estados.csv')

st.title('Meu primeiro APP - GCI')

estados = load_database()

dados, estatistica = st.tabs(
    ['Dados', 'Estatística Descritiva']
)

with dados:
    regiao = st.selectbox(
        'Selecione a região:',
        estados['regiao_nome'].unique()
    )
    st.dataframe(estados[estados['regiao_nome'] == regiao])

with estatistica:
    variavel = st.selectbox(
        'Selecione a variável desejada:',
        ['area', 'populacao', 'idh', 'matricula']
    )
    st.table(estados[variavel].describe())

# st.dataframe(estados)
# st.table(estados) - outra forma de gerar a tabela 
