# Análise SINASC

## Visão Geral
Este projeto realiza uma análise exploratória dos dados do Sistema de Informações sobre Nascidos Vivos (SINASC) de Rondônia, utilizando ferramentas como `pandas`, `seaborn`, `matplotlib` e `streamlit` para visualização interativa e compreensão dos dados.

## Requisitos

- Python 3.x
- pandas
- seaborn
- matplotlib
- streamlit

Para instalar as dependências necessárias, execute:
```bash
pip install pandas seaborn matplotlib streamlit
```

## Estrutura do Código

### Importação de Bibliotecas
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
```
As bibliotecas são utilizadas para leitura e manipulação de dados, visualizações gráficas e criação de uma interface interativa.

### Função `plota_pivot_table`
Esta função é responsável por criar e plotar tabelas dinâmicas com base nos parâmetros fornecidos.

```python
def plota_pivot_table(df, value, index, func, ylabel, xlabel, opcao='nada'):
    if opcao == 'nada':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).plot(figsize=[15, 5])
    elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).unstack().plot(figsize=[15, 5])
    elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).sort_values(value).plot(figsize=[15, 5])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    st.pyplot(fig=plt)
```

### Interface Streamlit
A interface apresenta:

- **Sidebar:** filtros para selecionar datas.
- **Gráficos:** diferentes visualizações exploratórias usando tabelas dinâmicas.

```python
sinasc = pd.read_csv('./input/SINASC_RO_2019.csv')
sinasc.DTNASC = pd.to_datetime(sinasc.DTNASC)

st.sidebar.title('Filtro')
valores_min = sinasc.DTNASC.min()
valores_max = sinasc.DTNASC.max()

data_min = st.sidebar.date_input('Data Mínima', valores_min)
data_max = st.sidebar.date_input('Data Máxima', valores_max)

# Containers e abas
with st.columns(2)[0]:
    st.write('Gráfico')

# Uso de abas para separação de conteúdo
with st.tabs(["data_min", "data_max"])[0]:
    st.radio('Selecione:', [1, 2])
```

### Exemplos de Gráficos

1. **Idade média da mãe por data de nascimento:**
   ```python
   plota_pivot_table(sinasc, 'IDADEMAE', 'DTNASC', 'mean', 'Média Idade Mãe por Data', 'Data Nascimento')
   ```

2. **Peso médio do bebê por gênero e data:**
   ```python
   plota_pivot_table(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'Média Peso Bebê', 'Data de Nascimento', 'unstack')
   ```

3. **Peso mediano por escolaridade da mãe:**
   ```python
   plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median', 'Peso Mediano', 'Escolaridade Mãe', 'sort')
   ```

4. **APGAR1 médio por tipo de gestação:**
   ```python
   plota_pivot_table(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'APGAR1 Médio', 'Gestação', 'sort')
   ```

## Como Executar
Para executar a aplicação Streamlit:
```bash
streamlit run app.py
```

## Melhorias Possíveis
- Adicionar opção para selecionar diferentes agregadores (`sum`, `count`, etc.).
- Melhorar validação de entradas do usuário.
- Adicionar testes automatizados.
- Implementar mais visualizações interativas.

## Conclusão
Esta análise fornece insights valiosos sobre nascimentos em Rondônia em 2019, com suporte para visualizações gráficas e interatividade por meio do Streamlit.

