# WattsUp - Comparador de Veículos

WattsUp é uma aplicação Python que permite comparar veículos a combustão e elétricos, analisando custos de combustível, consumo de energia e emissões de CO₂.  
Com funcionalidades como **análise de trajeto** e **projeção temporal**, a plataforma ajuda usuários a entenderem o impacto financeiro e ambiental das suas escolhas de mobilidade.

---

## Funcionalidades
- **Análise de Trajeto:** Compare dois veículos (um a combustão e um elétrico) para uma distância fixa, verificando consumo, custos e emissões de CO₂.
- **Projeção Temporal:** Analise o impacto acumulado ao longo de um período definido (dias, semanas, meses ou anos), observando evolução de custos e emissões.
- **Interface Simples:** O programa solicita inputs claros e exibe resultados em tabelas formatadas para fácil entendimento.

---

## Como Executar o Programa

1. Clone o repositório para sua máquina local:
   ```bash
   git clone https://github.com/WattsUp/python.git
   cd python
   ```

2. Certifique-se de ter o Python 3.8 ou superior instalado.

3. Instale as dependências, se necessário (nenhuma biblioteca externa é obrigatória).

4. Execute o programa principal:
   ```bash
   python main.py
   ```

5. Siga as instruções no terminal para usar as funcionalidades do WattsUp.

---

## Características Técnicas Diferenciais

### 1. Função `request_input`
A função `request_input` é responsável por gerenciar entradas do usuário com validação e mensagens de feedback personalizadas.  
**Características principais:**
- Solicita entrada do usuário com um **prompt customizável**.
- Valida o input com uma função de validação fornecida como argumento.
- Exibe mensagens de erro ou feedback dinâmico em caso de entrada inválida.
- Exemplo de uso:
  ```python
  distance = request_input("Digite a distância (km): ", lambda x: is_float(x))
  ```

---

### 2. Estruturação de Arquivos e Funções

O projeto é modularizado para facilitar a manutenção e extensibilidade:
- **`constants.py`**:
  - Contém constantes do programa, como emissões de CO₂ e rótulos do menu.
- **`utils.py`**:
  - Funções utilitárias para entrada, exibição e validação de dados.
- **`core.py`**:
  - Contém as funcionalidades principais: cálculo de trajetos e projeções temporais.
- **`text.py`**:
  - Armazena mensagens exibidas ao usuário, promovendo centralização do texto.

Essa estrutura mantém o código organizado e facilita futuras implementações.

---

### 3. Funções para Geração de Tabelas
A geração das tabelas formatadas é feita através de funções dedicadas no arquivo `utils.py`:
- **`get_table`**: Cria a tabela final combinando divisores e linhas formatadas.
- **`get_table_row`**: Formata uma linha da tabela com base nos valores e larguras das colunas.
- **`get_divider_row`**: Gera as divisórias da tabela para organizar visualmente os dados.

Exemplo de uma tabela gerada:
```
+------------+--------------------+--------------------+------------+
| Parâmetros | Gol                | Tesla              | Diferença  |
+------------+--------------------+--------------------+------------+
| Custo      | R$ 458.33         | R$ 171.43          | -R$ 286.90 |
+------------+--------------------+--------------------+------------+
```

---

### 4. Constantes de Emissão de CO₂
O programa utiliza valores realistas para emissões de CO₂ por unidade de consumo de combustível e energia:
- **`gasolina`:** 2.31 kg CO₂/L.
- **`etanol`:** 0.84 kg CO₂/L.
- **`diesel`:** 2.68 kg CO₂/L.
- **`energia`:** 0.055 kg CO₂/kWh (média nacional no Brasil).

Esses valores são armazenados no arquivo `constants.py` como:
```python
CO2_EMISSION_CONSTANTS = {
    "gasolina": 2.31,
    "etanol": 0.84,
    "diesel": 2.68,
    "energia": 0.055,
}
```

Eles garantem precisão nos cálculos de impacto ambiental ao longo das análises.

---

## Link do Repositório

Repositório GitHub: [WattsUp/python](https://github.com/WattsUp/python.git)
