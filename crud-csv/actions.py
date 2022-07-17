from enum import IntEnum
from typing import Any, Callable, Dict, Tuple

from crud import create_record, delete_record, retrieve_record, update_record
from utils import print_df


class AppActions(IntEnum):
    CREATE = 1
    RETRIEVE = 2
    UPDATE = 3
    DELETE = 4
    PRINTCSV = 5
    QUIT = 6


APP_ACTIONS: Dict[int, Tuple[str, Callable[..., Any] | None]] = {
    AppActions.CREATE.value: (
        "Criação de registro",
        create_record,
    ),
    AppActions.RETRIEVE.value: (
        "Consulta de registro",
        retrieve_record,
    ),
    AppActions.UPDATE.value: (
        "Alteração de registro",
        update_record,
    ),
    AppActions.DELETE.value: (
        "Remoção de registro",
        delete_record,
    ),
    AppActions.PRINTCSV.value: (
        "Mostrar tabela de dados",
        print_df,
    ),
    AppActions.QUIT.value: ("Encerramento", None),
}
