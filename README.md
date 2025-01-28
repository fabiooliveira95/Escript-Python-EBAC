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
As bibliotecas são utilizadas para leitura e manipulação de dados, visualizações gráficas e criação de uma interface interativa.

### Função `plota_pivot_table`
Esta função é responsável por criar e plotar tabelas dinâmicas com base nos parâmetros fornecidos.

### Interface Streamlit
A interface apresenta:

- **Sidebar:** filtros para selecionar datas.
- **Gráficos:** diferentes visualizações exploratórias usando tabelas dinâmicas.

### Exemplos de Gráficos

1. **Idade média da mãe por data de nascimento:**
 
2. **Peso médio do bebê por gênero e data:**
   
3. **Peso mediano por escolaridade da mãe:**
 
4. **APGAR1 médio por tipo de gestação:**
 
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

