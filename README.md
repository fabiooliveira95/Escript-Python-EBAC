###("Projeto Script_python.py")####

Projeto de Análise de Dados SINASC

Visão geral

Este projeto tem como objetivo processar e analisar dados de arquivos SINASC (Sistema de Informações sobre Nascidos Vivos) usando Python. Ele gera visualizações e insights sobre estatísticas de nascimento, como idade média materna, distribuição de peso do bebê e pontuações de Apgar.

Recursos

Lê vários arquivos CSV contendo dados SINASC.

Gera tabelas dinâmicas para métricas-chave.

Visualiza insights de dados usando mapas de calor.

Salva visualizações em pastas de saída estruturadas.

Requisitos

Para executar este projeto, certifique-se de ter os seguintes pacotes Python instalados:

pip install numpy pandas matplotlib seaborn

Estrutura do arquivo

project_root/
|-- input/
| |-- SINASC_RO_2019_MAR.csv
| |-- SINASC_RO_2019_ABR.csv
| |-- SINASC_RO_2019_MAI.csv
| |-- SINASC_RO_2019_JUN.csv
| |-- SINASC_RO_2019_DEZ.csv
|-- main.py
|-- README.md

Uso

Coloque os arquivos CSV do SINASC no diretório input/.

Execute o script Python principal:

python main.py

O script irá:

Verificar a existência de cada arquivo de entrada.

Concatenar todos os arquivos CSV válidos em um único DataFrame.

Gerar e salvar os seguintes gráficos em uma pasta nomeada após a data máxima dos dados:

Idade materna média por data de nascimento.

Idade materna média por data de nascimento e sexo.

Peso médio do bebê por data de nascimento e sexo.

Peso médio do bebê por educação materna.

Pontuação média de Apgar1 por gestação.

Saída

Os gráficos serão salvos em ~/Desktop/sinasc_img/{max_date}/ com nomes de arquivo descritivos:

media_idade_mae_por_data.png

media_idade_mae_por_sexo.png

media_peso_bebe_por_sexo.png

PESO_mediano_por_escolaridade_mae.png

media_apgar1_por_gestacao.png

Funções

plota_pivot_table()

Descrição: Plota uma tabela dinâmica usando o mapa de calor Seaborn.

Parâmetros:

df (pd.DataFrame): O DataFrame de origem.

values ​​(str): Coluna para agregar.

index (str ou lista): Colunas para agrupar.

aggfunc (str): Função de agregação (média, soma, mediana, etc.).

titulo (str): Título do gráfico.

xlabel (str): rótulo do eixo X.

layout (str, opcional): ajustes de layout de desempilhamento ou classificação.

Exemplo de saída

Aqui está um exemplo dos gráficos gerados:

Tratamento de erros

O script verifica se há arquivos ausentes e alerta o usuário se algum arquivo especificado não existir.

Melhorias

Possíveis melhorias para versões futuras incluem:

Tratamento dinâmico de erros para colunas ausentes.

Visualizações interativas.

Opções de agregação e visualização mais flexíveis.




####("Projeto Script_Zero.py")#####

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

