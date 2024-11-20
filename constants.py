# Constante que define o tempo de latência (em segundos) para simulações ou operações que precisem de pausas
LATENCY = 0.5

# Dicionário com as opções do menu principal e seus respectivos rótulos para exibição ao usuário
MAIN_MENU_LABELS = {
    "1": "Análise de Trajeto",
    "2": "Projeção Temporal",
    "3": "Saiba Mais",
    "0": "Encerrar Programa",
}

# Constantes que definem as emissões de CO₂ (em kg) por unidade de energia/combustível consumido
CO2_EMISSION_CONSTANTS = {
    "gasolina": 2.31,
    "etanol": 0.84,
    "diesel": 2.68,
    "energia": 0.055,  # Emissão de CO₂ derivada da geração de energia, tomando como referencia a matriz energética brasileira
}
