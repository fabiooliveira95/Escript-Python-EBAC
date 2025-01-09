import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


def plota_pivot_table(df, values, index, aggfunc, titulo, xlabel, layout=None):
    """
    Function to plot a pivot table using seaborn heatmap.

    Parameters:
    - df (pd.DataFrame): The source DataFrame.
    - values (str): The column to aggregate.
    - index (str or list): The column(s) to group by for the index.
    - aggfunc (str): Aggregation function to apply (e.g., 'mean', 'sum', 'median').
    - titulo (str): Title of the plot.
    - xlabel (str): Label for the x-axis.
    - layout (str, optional): Layout type for unstacking or sorting.

    Returns:
    - None (displays the plot).
    """
    # Create the pivot table
    pivot_table = pd.pivot_table(df, values=values, index=index, aggfunc=aggfunc)

    # Apply layout adjustments if specified
    if layout == 'unstack':
        pivot_table = pivot_table.unstack()
    elif layout == 'sort':
        pivot_table = pivot_table.sort_values(by=values, ascending=False)

    # Set up the Matplotlib figure
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot_table, annot=True, fmt=".2f", cmap="Blues", cbar=True)

    # Add labels and title
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(", ".join(index) if isinstance(index, list) else index)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Show the plot
    plt.show()


# Define file paths
file_paths = [
    './input/SINASC_RO_2019_MAR.csv',
    './input/SINASC_RO_2019_ABR.csv',
    './input/SINASC_RO_2019_MAI.csv',
    './input/SINASC_RO_2019_JUN.csv',
    './input/SINASC_RO_2019_DEZ.csv'
]

# Check and process each file
for file_path in file_paths:
    if not os.path.exists(file_path):
        print(f"Error: the file '{file_path}' does not exist. Please check the path.")
    else:
        print(f"Processing file: {file_path}")

        # Concatenate multiple CSV files into a single DataFrame
        sinasc = pd.concat([pd.read_csv(fp) for fp in file_paths])

        # Display some basic data insights
        sinasc.DTNASC.value_counts()
        sinasc.info()

        # Extract the maximum date for creating output folders
        max_data = sinasc.DTNASC.max()[:7]
        print(max_data)
        os.makedirs(os.path.expanduser(f'~/Desktop/sinasc_img/{max_data}'), exist_ok=True)

        # Plot pivot tables
        plota_pivot_table(sinasc, 'IDADEMAE', 'DTNASC', 'mean', 'média idade mãe por data', 'data nascimento')
        plt.savefig(os.path.expanduser(f'~/Desktop/sinasc_img/{max_data}/media_idade_mae_por_data.png'))

        plota_pivot_table(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean', 'média idade mãe por sexo',
                          'data de nascimento', 'unstack')
        plt.savefig(os.path.expanduser(f'~/Desktop/sinasc_img/{max_data}/media_idade_mae_por_sexo.png'))

        plota_pivot_table(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'média peso bebê por sexo',
                          'data de nascimento', 'unstack')
        plt.savefig(os.path.expanduser(f'~/Desktop/sinasc_img/{max_data}/media_peso_bebe_por_sexo.png'))

        plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median', 'PESO mediano por escolaridade',
                          'escolaridade mãe', 'sort')
        plt.savefig(os.path.expanduser(f'~/Desktop/sinasc_img/{max_data}/PESO_mediano_por_escolaridade_mae.png'))

        plota_pivot_table(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'apgar1 médio por gestação', 'gestação', 'sort')
        plt.savefig(os.path.expanduser(f'~/Desktop/sinasc_img/{max_data}/media_apgar1_por_gestacao.png'))

