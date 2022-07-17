from time import sleep
from typing import Any, Callable, Optional, Tuple

import pandas as pd
from actions import APP_ACTIONS, AppActions
from config import OPTIONS_TEXT, PATHS
from utils import cls, lock_record, print_df, record_exists


def get_program_action() -> Tuple[Optional[str], Optional[Callable[..., Any]], int]:
    """Função auxiliar que automatiza a multiplexação de ações no programa principal."""
    cls()
    action_msg = None
    action_callable = None

    try:
        option = int(input(OPTIONS_TEXT))
        action = APP_ACTIONS[option]

        if action is not None:
            action_msg, action_callable = action
    except (KeyError, ValueError):
        print("\nOpção não suportada!")
        sleep(0.5)
        get_program_action()

    return action_msg, action_callable, option


def main(flag_file_path: str, csv_file_path: str) -> None:
    """Programa principal."""
    flag_file = open(flag_file_path, "a+")

    while True:
        action_msg, action_callable, option = get_program_action()

        if option == AppActions.QUIT.value:
            break

        cls()
        print(action_msg)

        if option == AppActions.PRINTCSV.value and action_callable is not None:
            action_callable(pd.read_csv(csv_file_path, index_col=0))

        elif option == AppActions.CREATE.value and action_callable is not None:
            error_msg, content = action_callable(csv_file_path)

            if error_msg is not None:
                print(error_msg)
            else:
                print(f"{action_msg} realizada com sucesso!\n")
                print_df(content)
        else:

            @lock_record(flag_file_path)
            def modify_csv(csv_path: str, rec_id: str) -> pd.DataFrame | None:
                return (
                    action_callable(csv_path, int(rec_id))
                    if action_callable is not None
                    else None
                )

            # Pega o ID
            record_id = input("\nInforme o ID do registro: ")

            if not record_exists(record_id, csv_file_path):
                print(f"\nRegistro com ID {record_id} não existe")
            else:
                content = modify_csv(csv_file_path, record_id)

                if isinstance(content, pd.DataFrame):
                    print_df(content)
                else:
                    print(content)

        input("\nPressione tecla para continuar...")

    flag_file.close()


if __name__ == "__main__":
    cls()
    try:
        flag_file_path = PATHS["flag"]
        csv_file_path = PATHS["csv"]

        if flag_file_path and csv_file_path:
            main(flag_file_path, csv_file_path)

    except KeyboardInterrupt:  # Lida com o Ctrl+C
        print("\n\nRecebido SIGINT. Encerrando aplicação...\n")
        exit(0)
    except Exception as exc:  # Catch geral
        print(f"\n\n{exc.__class__.__name__}: {str(exc)}\n")
        exit(1)
