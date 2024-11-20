import text as t

from core import *


# Função principal que inicia o programa
def start():
    display_content(t.welcome_message)

    # Loop principal do menu
    while True:
        display_content(t.main_menu)

        option = request_input(
            t.main_menu_prompt,
            lambda x: x in ["1", "2", "3", "0"],
            lambda x: t.main_menu_feedback_message.format(MAIN_MENU_LABELS[x])
        )

        # Executa a ação correspondente à opção escolhida pelo usuário
        match option:
            case "1": path_analysis()
            case "2": temporal_projection()
            case "3": find_out_more()
            case "0": break

    display_content(t.stop_program)


if __name__ == "__main__":
    start()
