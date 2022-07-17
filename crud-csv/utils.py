import os
from typing import Any, Callable, Dict

import pandas as pd


def cls() -> None:
    """Limpa console, cross-platform."""

    os.system("cls" if os.name == "nt" else "clear")


def print_df(df: pd.DataFrame) -> None:
    """Print dataframe em formato markdown."""
    print(df.to_markdown())


def record_exists(record_id: str | int, csv_path: str) -> bool:
    """Checa se registro existe."""

    df = pd.read_csv(csv_path, index_col=0, header=0)
    return int(record_id) in df.index


def lock_record(flag_file_path: str) -> Callable[..., Any]:
    """Decorador externo, de modo a suportar a passagem do path do flag_file."""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        """Decorador cuja função é travar o par (ID, Name) durante a sua modificação."""

        def wrapper(*args: Any, **kwargs: Dict[Any, Any]) -> Any:
            # Procura no arquivo das flags se o ID do registro a
            # ser manipulado ja esta em execucao
            is_locked = False
            record_id = args[1]

            with open(flag_file_path, "r+") as flag:
                f1 = flag.readlines()
                for n in f1:
                    if n == record_id + "\n":
                        is_locked = True

            if is_locked is True:
                print(
                    f"\nRegistro de ID {record_id} está sendo alterado "
                    "por outra instãncia do programa"
                )
                return

            # escreve no arquivo das flags que o registro atual esta sendo editado
            with open(flag_file_path, "a+") as flag:
                flag.writelines(record_id + "\n")

            # Aqui a operação de consulta, atualização ou remoção é realizada
            response = func(*args, **kwargs)

            # Remove do flags o ID do registro no qual foi feito a operacao
            if is_locked is False:
                with open(flag_file_path, "r") as leitor:
                    # Salva as linhas do flags em uma lista
                    nums = leitor.readlines()

                    # Atualiza o valor do record_id para ter o \n
                    # para poder ser removido da lista
                    record_id = record_id + "\n"

                    # Remove o record_id da lista
                    nums.remove(record_id)

                    # Insere a lista de volta no flag.txt sem o record_id
                    with open(flag_file_path, "w") as escritor:
                        for n in nums:
                            escritor.write(n)

            # Retorna o dataframe
            return response

        return wrapper

    return decorator
