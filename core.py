import text as t
from utils import *
from constants import *

# Calcula tabela de análise de trajeto
def calculate_path_analysis(distance, combustion_car, electric_car):
    # Calcula o consumo e custo do combustível do carro a combustão
    combustion_car_fuel_expense = distance / combustion_car["consumption"]
    combustion_car_fuel_cost = combustion_car_fuel_expense * combustion_car["fuel_price"]
    combustion_car_co2_emission = combustion_car_fuel_expense * CO2_EMISSION_CONSTANTS[combustion_car["fuel_type"]]

    # Calcula o consumo e custo da energia do carro elétrico
    electric_car_consumption = electric_car["battery_autonomy"] / electric_car["battery_capacity"]
    electric_car_energy_expense = distance / electric_car_consumption
    electric_car_energy_cost = electric_car_energy_expense * electric_car["energy_price"]
    electric_car_co2_emission = combustion_car_fuel_expense * CO2_EMISSION_CONSTANTS["energia"]

    # Calcula a diferença de custos e emissões entre os carros
    fuel_cost_diference = electric_car_energy_cost - combustion_car_fuel_cost
    co2_emission_diference = electric_car_co2_emission - combustion_car_co2_emission

    # Formata os valores para exibição
    combustion_car_fuel_expense_value = f"{round(combustion_car_fuel_expense, 2)} L"
    combustion_car_fuel_cost_value = f"R$ {round(combustion_car_fuel_cost, 2)}"
    combustion_car_co2_emission_value = f"{round(combustion_car_co2_emission, 2)} kg"

    electric_car_energy_expense_value = f"{round(electric_car_energy_expense, 2)} kWh"
    electric_car_energy_cost_value = f"R$ {round(electric_car_energy_cost, 2)}"
    electric_car_co2_emission_value = f"{round(electric_car_co2_emission, 2)} kg"

    fuel_cost_diference_value = f"R$ {round(fuel_cost_diference, 2)}"
    co2_emission_diference_value = f"{round(co2_emission_diference, 2)} kg"

    # Gera a tabela de resultados
    values = [
        ["Parâmetros", combustion_car["name"], electric_car["name"], "Diferença"],
        ["Combustível", combustion_car_fuel_expense_value, electric_car_energy_expense_value, "(N/A)"],
        ["Custo Total", combustion_car_fuel_cost_value, electric_car_energy_cost_value, fuel_cost_diference_value],
        ["Emissão de CO₂", combustion_car_co2_emission_value, electric_car_co2_emission_value, co2_emission_diference_value]
    ]

    table = get_table(values, "LEFT_ALL")
    return table

# Gerencia o fluxo de entrada e exibição para a análise de trajeto
def path_analysis():
    display_content(t.path_analysis_title)

    display_content(t.path_analysis_header)

    distance = float(request_input(
        t.path_analysis_distance_prompt,
        lambda x: is_float(x)
    ))

    print()
    display_content(t.path_analysis_combustion_car_header)

    # Entrada de dados para o carro a combustão
    combustion_car_name = request_input(
        t.path_analysis_combustion_car_name_prompt,
        lambda x: bool(x)
    )
    combustion_car_fuel_type = request_input(
        t.path_analysis_combustion_car_fuel_type_prompt,
        lambda x: x.lower() in ["gasolina", "etanol", "diesel"]
    ).lower()
    combustion_car_consumption = float(request_input(
        t.path_analysis_combustion_car_consumption_prompt,
        lambda x: is_float(x)
    ))
    combustion_car_fuel_price = float(request_input(
        t.path_analysis_combustion_car_fuel_price_prompt,
        lambda x: is_float(x)
    ))

    print()
    display_content(t.path_analysis_electric_car_header)

    # Entrada de dados para o carro elétrico
    electric_car_name = request_input(
        t.path_analysis_electric_car_name_prompt,
        lambda x: bool(x)
    )
    electric_car_battery_capacity = float(request_input(
        t.path_analysis_electric_car_battery_capacity_prompt,
        lambda x: is_float(x)
    ))
    electric_car_battery_autonomy = float(request_input(
        t.path_analysis_electric_car_battery_autonomy_prompt,
        lambda x: is_float(x)
    ))
    electric_car_energy_price = float(request_input(
        t.path_analysis_electric_car_energy_price_prompt,
        lambda x: is_float(x)
    ))

    print()
    display_content(t.path_analysis_result_header)

    # Estruturação dos dados dos carros
    combustion_car = {
        "name": combustion_car_name,
        "fuel_type": combustion_car_fuel_type,
        "consumption": combustion_car_consumption,
        "fuel_price": combustion_car_fuel_price
    }

    electric_car = {
        "name": electric_car_name,
        "battery_capacity": electric_car_battery_capacity,
        "battery_autonomy": electric_car_battery_autonomy,
        "energy_price": electric_car_energy_price
    }

    path_analysis_result_table = calculate_path_analysis(distance, combustion_car, electric_car)

    display_content(t.path_analysis_distance_result.format(distance))
    display_content(path_analysis_result_table)

# Calcula tabela de projeção temporal
def calculate_temporal_projection(interval_type, distance_per_interval, interval_amount, combustion_car, electric_car):
    values = [["Tempo", "Distância", "Combustível / Energia", "Custo Total (R$)", "Emissão de CO₂ (kg)", "Diferença de Custos", "Diferença de CO₂"]]

    for i in range(1, interval_amount + 1):
        total_time = i
        total_distance = total_time * distance_per_interval
        
        # Cálculos do carro a combustão
        combustion_car_fuel_expense = total_distance / combustion_car["consumption"]
        combustion_car_fuel_cost = combustion_car_fuel_expense * combustion_car["fuel_price"]
        combustion_car_co2_emission = combustion_car_fuel_expense * CO2_EMISSION_CONSTANTS[combustion_car["fuel_type"]]

        # Cálculos do carro elétrico
        electric_car_consumption = electric_car["battery_autonomy"] / electric_car["battery_capacity"]
        electric_car_energy_expense = total_distance / electric_car_consumption
        electric_car_energy_cost = electric_car_energy_expense * electric_car["energy_price"]
        electric_car_co2_emission = combustion_car_fuel_expense * CO2_EMISSION_CONSTANTS["energia"]

        # Diferenças entre os carros
        fuel_cost_diference = electric_car_energy_cost - combustion_car_fuel_cost
        co2_emission_difference = electric_car_co2_emission - combustion_car_co2_emission

        # Adiciona linha com os resultados calculados
        total_time_value = f"{total_time} {interval_type}"
        total_distance_value = f"{round(total_distance, 2)} km"
        fuel_value = f"{round(combustion_car_fuel_expense, 2)} L | {round(electric_car_energy_expense, 2)} kWh"
        cost_fuel_value = f"R$ {round(combustion_car_fuel_cost, 2)} | R$ {round(electric_car_energy_cost, 2)}"
        co2_emission_value = f"{round(combustion_car_co2_emission, 2)} kg | {round(electric_car_co2_emission, 2)} kg"
        fuel_cost_diference = f"R$ {round(fuel_cost_diference, 2)}"
        co2_emission_difference = f"{round(co2_emission_difference, 2)} kg"

        values.append([total_time_value, total_distance_value, fuel_value, cost_fuel_value, co2_emission_value, fuel_cost_diference, co2_emission_difference])
            
    table = get_table(values, "LEFT_ALL")
    return table

# Gerencia o fluxo de entrada e exibição para a projeção temporal
def temporal_projection():
    display_content(t.temporal_projection_title)

    display_content(t.temporal_projection_header)

    interval_type = request_input(
        t.temporal_projection_interval_type_prompt,
        lambda x: x.lower() in ["dias", "semanas", "meses", "anos"]
    ).lower()
    distance_per_interval = float(request_input(
        t.temporal_projection_distance_per_interval_prompt,
        lambda x: is_float(x)
    ))
    interval_amount = int(request_input(
        t.temporal_projection_interval_amount_prompt,
        lambda x: x.isdigit()
    ))

    print()
    display_content(t.temporal_projection_combustion_car_header)

    # Entrada de dados para o carro a combustão
    combustion_car_name = request_input(
        t.temporal_projection_combustion_car_name_prompt,
        lambda x: bool(x)
    )
    combustion_car_fuel_type = request_input(
        t.temporal_projection_combustion_car_fuel_type_prompt,
        lambda x: x.lower() in ["gasolina", "etanol", "diesel"]
    ).lower()
    combustion_car_consumption = float(request_input(
        t.temporal_projection_combustion_car_consumption_prompt,
        lambda x: is_float(x)
    ))
    combustion_car_fuel_price = float(request_input(
        t.temporal_projection_combustion_car_fuel_price_prompt,
        lambda x: is_float(x)
    ))

    print()
    display_content(t.temporal_projection_electric_car_header)

    # Entrada de dados para o carro elétrico
    electric_car_name = request_input(
        t.temporal_projection_electric_car_name_prompt,
        lambda x: bool(x)
    )
    electric_car_battery_capacity = float(request_input(
        t.temporal_projection_electric_car_battery_capacity_prompt,
        lambda x: is_float(x)
    ))
    electric_car_battery_autonomy = float(request_input(
        t.temporal_projection_electric_car_battery_autonomy_prompt,
        lambda x: is_float(x)
    ))
    electric_car_energy_price = float(request_input(
        t.temporal_projection_electric_car_energy_price_prompt,
        lambda x: is_float(x)
    ))

    print()
    display_content(t.temporal_projection_result_header)

    # Estruturação dos dados dos carros
    combustion_car = {
        "name": combustion_car_name,
        "fuel_type": combustion_car_fuel_type,
        "consumption": combustion_car_consumption,
        "fuel_price": combustion_car_fuel_price
    }
    
    electric_car = {
        "name": electric_car_name,
        "battery_capacity": electric_car_battery_capacity,
        "battery_autonomy": electric_car_battery_autonomy,
        "energy_price": electric_car_energy_price
    }

    temporal_projection_result_table = calculate_temporal_projection(interval_type, distance_per_interval, interval_amount, combustion_car, electric_car)

    display_content(t.temporal_projection_distance_per_interval_result.format(distance_per_interval))
    display_content(temporal_projection_result_table)

# Exibe informações adicionais sobre o programa
def find_out_more():
    display_content(t.find_out_more)
