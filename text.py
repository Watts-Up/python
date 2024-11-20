# Mensagens do Sistema

welcome_message = """Seja bem-vindo(a) ao WattsUp!

Somos uma plataforma inteligente de comparação entre carros a combustão e
carros elétricos, ajudando você a entender as diferenças nos custos de
combustíveis na emissão de CO₂ na atmosfera.
"""

invalid_input = "Entrada Inválida!\n"

stop_program = """Obrigado por usar o WattsUp! Até a próxima.
Programa encerrado."""


# Menu Principal

main_menu = """================================ Menu Principal ================================
[1] Fazer uma Análise de Trajeto
[2] Fazer uma Projeção Temporal
[3] Saiba Mais
[0] Encerrar Programa
"""

main_menu_prompt = "Escolha uma opção: "

main_menu_feedback_message = 'Você Escolheu "{}"\n'


# Análise de Trajeto

path_analysis_title = "============================== Análise de Trajeto ==============================\n"

path_analysis_header = "Insira as informações:\n"

path_analysis_combustion_car_header = "Carro a Combustão:"

path_analysis_electric_car_header = "Carro Elétrico:"

path_analysis_result_header = "Resultado:\n"

path_analysis_distance_prompt = "Distância do trajeto (em km): "

path_analysis_combustion_car_name_prompt = "> Nome do Carro: "

path_analysis_combustion_car_fuel_type_prompt = "> Combustível (gasolina | etanol | diesel): "

path_analysis_combustion_car_consumption_prompt = "> Consumo de Combustível (km/l): "

path_analysis_combustion_car_fuel_price_prompt = "> Preço do Litro do Combustível (R$): "

path_analysis_electric_car_name_prompt = "> Nome do Carro: "

path_analysis_electric_car_battery_capacity_prompt = "> Capacidade da Bateria (kWh): "

path_analysis_electric_car_battery_autonomy_prompt = "> Autonomia da Bateria (km): "

path_analysis_electric_car_energy_price_prompt = "> Preço da Energia (R$/kWh): "

path_analysis_distance_result = "Distância do trajeto: {} km"


# Projeção Temporal

temporal_projection_title = "============================== Projeção Temporal ===============================\n"

temporal_projection_header = "Insira as informações:\n"

temporal_projection_combustion_car_header = "Carro a Combustão:"

temporal_projection_electric_car_header = "Carro Elétrico:"

temporal_projection_result_header = "Resultado:\n"

temporal_projection_interval_type_prompt = "Intervalo (dias | semanas | meses | anos): "

temporal_projection_distance_per_interval_prompt = "Distância percorrida a cada intervalo (km): "

temporal_projection_interval_amount_prompt = "Quantidade de Intervalos: "

temporal_projection_combustion_car_name_prompt = "> Nome do Carro: "

temporal_projection_combustion_car_fuel_type_prompt = "> Combustível (gasolina | etanol | diesel): "

temporal_projection_combustion_car_consumption_prompt = "> Consumo de Combustível (km/l): "

temporal_projection_combustion_car_fuel_price_prompt = "> Preço do Litro do Combustível (R$): "

temporal_projection_electric_car_name_prompt = "> Nome do Carro: "

temporal_projection_electric_car_battery_capacity_prompt = "> Capacidade da Bateria (kWh): "

temporal_projection_electric_car_battery_autonomy_prompt = "> Autonomia da Bateria (km): "

temporal_projection_electric_car_energy_price_prompt = "> Preço da Energia (R$/kWh): "

temporal_projection_distance_per_interval_result = "Distância percorrida a cada intervalo : {} km"


# Projeção Temporal

find_out_more = """=========================== Sobre as Funcionalidades ===========================

- Análise de Trajeto:
    Compare o impacto econômico e ambiental de um carro a combustão e um carro
    elétrico em um trajeto fixo, considerando o consumo de combustível e
    energia, além das emissões de CO₂.

- Projeção Temporal:
    Veja a evolução dos custos e emissões ao longo do tempo, analisando
    períodos configuráveis e distâncias recorrentes.
"""
