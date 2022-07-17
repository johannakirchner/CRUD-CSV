import csv
from typing import Dict, Tuple

import pandas as pd


def create_record(csv_path: str) -> Tuple[str | None, pd.DataFrame | None]:
    try:
        record_id = int(input("\nID do registro a ser adicionado: "))
    except ValueError:
        return "ID informado não é válido!", None

    record_name = input("\nNome do registro a ser adicionado: ")

    # atualiza a linha correspondente ao Id
    df = pd.read_csv(csv_path, index_col=0, header=0)

    # se o indica a ser adicionado ja existe, nao adiciona
    if record_id in df.index:
        return f"\nRegistro com ID {record_id} já existe!", None
    else:
        # abre o arquivo no modo append p/ adicionar
        with open(csv_path, "a", newline="\n") as file:
            escritor = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)

            # coloca o que vai ser add em uma lista
            data = [[record_id, record_name]]

            # escreve no csv a nova linha
            escritor.writerows(data)

        return None, pd.read_csv(csv_path, index_col=0, header=0)


def retrieve_record(csv_path: str, record_id: int) -> Dict[str, str | int]:
    df = pd.read_csv(csv_path)
    condition = df["Id"] == record_id
    id, name = df[condition].values[0]

    return {
        "id": id,
        "name": name,
    }


def update_record(csv_path: str, record_id: int) -> pd.DataFrame:
    record_name = input("\nInsira o novo nome do registro: ")

    # cria um dataframe a partir do csv
    df = pd.read_csv(csv_path, index_col=0, header=0)

    # atualiza a linha correspondente ao Id
    df.loc[record_id, "Name"] = record_name

    # converte de volta para csv
    df.to_csv(csv_path, quoting=csv.QUOTE_NONNUMERIC)

    return df


def delete_record(csv_path: str, record_id: int) -> pd.DataFrame:
    # cria um dataframe a partir do csv
    df = pd.read_csv(csv_path, index_col=0, header=0)

    # deleta a linha de acordo com o Id
    df.drop(record_id, axis=0, inplace=True)

    # converte de volta para csv
    df.to_csv(csv_path, quoting=csv.QUOTE_NONNUMERIC)

    return df
