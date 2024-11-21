from time import sleep

from constants import *
from text import invalid_input as t_invalid_input


# Exibe conteúdo após um atraso definido pela constante LATENCY
def display_content(content):
    sleep(LATENCY)
    print(content)


# Solicita entrada do usuário e valida com base em um validador customizado
def request_input(prompt, validator, feedback_message=None, invalid_input=t_invalid_input):
    while True:
        user_input = input(prompt)

        if not validator(user_input):
            display_content(invalid_input)
            continue
        
        break
    
    if feedback_message is not None:
        display_content(feedback_message(user_input) if callable(feedback_message) else feedback_message)

    return user_input  # Retorna a entrada válida do usuário


# Verifica se um valor pode ser convertido para float
def is_float(value):
    try:
        float(value)  # Tenta converter para float
        return True
    except:
        return False  # Retorna False se não for possível converter


# Valida se todas as linhas de uma tabela têm o mesmo número de colunas
def valid_table(values):
    cols = len(values[0])

    for row in values[1:]:
        if len(row) != cols: raise("Invalid Table")


# Valida a formatação das colunas em uma tabela
def valid_column_formats(values, columns_formats):
    cols = len(values[0])

    # Verifica se o formato de colunas é uma lista e tem o tamanho correto
    if isinstance(columns_formats, list) and len(columns_formats) != cols:
        raise("Invalid Columns Widths List")

    # Verifica se o formato de colunas é uma string válida
    if columns_formats not in ["LEFT_ALL", "CENTER_ALL", "RIGHT_ALL"]:
        raise Exception("Invalid Columns Widths String")


# Calcula a largura máxima de cada coluna da tabela
def get_column_widths(values):
    rows, cols = len(values), len(values[0])

    column_widths = []
    for col in range(cols):
        max_width = 0
        for row in range(rows):
            value = values[row][col]
            max_width = max(max_width, len(value))  # Determina a largura máxima da coluna

        column_widths.append(max_width)

    return column_widths


# Define o alinhamento de cada coluna com base no formato especificado
def get_column_formats(values, column_formats):
    if isinstance(column_formats, list): 
        return column_formats  # Retorna diretamente se for uma lista

    cols = len(values[0])

    match column_formats:
        case "LEFT_ALL": return ["LEFT" for _ in range(cols)]
        case "CENTER_ALL": return ["CENTER" for _ in range(cols)]
        case "RIGHT_ALL": return ["RIGHT" for _ in range(cols)]


# Formata o conteúdo de uma célula da tabela com alinhamento específico
def get_cell(value, width, format="LEFT"):
    match format:
        case "LEFT": return f" {value.ljust(width)} |"
        case "CENTER": return f" {value.center(width)} |"
        case "RIGHT": return f" {value.rjust(width)} |"


# Cria uma linha divisória da tabela com base nas larguras das colunas
def get_divider_row(widths):
    divider_row = "+"

    for width in widths:
        divider_row += "-" * (width + 2) + "+"  # Cria divisória ajustada à largura da coluna
        
    return divider_row + "\n"


# Cria uma linha da tabela formatada
def get_table_row(values, widths, column_formats):
    table_row = "|"

    for col, value in enumerate(values):
        table_row += get_cell(value, widths[col], column_formats[col])  # Adiciona célula formatada

    return table_row + "\n"


# Gera a tabela completa com divisórias e linhas formatadas
def get_table(values, column_formats):
    valid_table(values)  # Verifica consistência das linhas
    valid_column_formats(values, column_formats)  # Valida o formato das colunas

    widths = get_column_widths(values)
    column_formats = get_column_formats(values, column_formats)

    table = ""
    divider_row = get_divider_row(widths)  # Linha divisória padrão

    table += divider_row
    table += get_table_row(values[0], widths, column_formats)  # Linha de cabeçalho
    table += divider_row

    for row in values[1:]:
        table += get_table_row(row, widths, column_formats)  # Adiciona linhas de dados
    
    table += divider_row

    return table
