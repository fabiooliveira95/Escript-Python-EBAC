import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set()

def plota_pivot_table(df, value, index, func, ylabel, xlabel, opcao='nada'):
    if opcao == 'nada':
        pd.pivot_table(df, values=value, index=index,aggfunc=func).plot(figsize=[15, 5])
    elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index,aggfunc=func).unstack().plot(figsize=[15, 5])
    elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index,aggfunc=func).sort_values(value).plot(figsize=[15, 5])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    st.pyplot(fig=plt)
    return None



st.write('# Análise SINASC')

sinasc = pd.read_csv('./input/SINASC_RO_2019.csv')
sinasc.DTNASC = pd.to_datetime(sinasc.DTNASC)



st.sidebar.title('filte')

valores_min = sinasc.DTNASC.min()
valores_max = sinasc.DTNASC.max()

data_min = st.sidebar.date_input('data minima', valores_min)
data_max = st.sidebar.date_input('data maxima', valores_max)

data_min, data_max = st.columns(2)
data_min.write('data_min:')
data_max.write('data_max:')

# Three columns with different widths
data_min, data_max = st.columns([1,1])
# col1 is wider

# Using 'with' notation:
with data_min :
    st.write('grafico')
st.write('outro grafico')


# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["data_min", "data_max"])
tab1.write("data_min:")
tab2.write("data_max:")

# You can also use "with" notation:
with tab1:
    st.radio('Select one:', [1, 2])


plota_pivot_table(sinasc, 'IDADEMAE', 'DTNASC', 'mean', 'média idade mãe por data', 'data nascimento')
plota_pivot_table(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean', 'media idade mae','data de nascimento','unstack')
plota_pivot_table(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'media peso bebe','data de nascimento','unstack')
plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median', 'PESO mediano','escolaridade mae','sort')
plota_pivot_table(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'apgar1 medio','gestacao','sort')

