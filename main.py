
import csv
from lib2to3.pgen2.token import NEWLINE
from operator import contains
import pandas as pd
import os

# cria o arquivo da flag caso nao exista
aaaa = open("flag.txt", 'a+')

# define o caminho
path = os.path.join(os.path.dirname(__file__), 'Regions.csv')
stop = 1

while(stop != 2):

    # printa o dataframe (pandas)
    imprimir = pd.read_csv(path, index_col=0, header=0)
    print(imprimir)

    # selecionar operacao
    op = input(
        "\nselecione a operacao\n1.inserir novo registro  2.alterar/consultar/remover registro existente\n")

    if(op == '1'):
        # ! insere - OK
        reg = input("\nnome do registro a ser adicionado: ")
        idi = input("\nid do registro a ser adicionado: ")
        # atualiza a linha correspondente ao Id

        df = pd.read_csv(path, index_col=0, header=0)
        # se o indica a ser adicionado ja existe, nao adiciona
        if int(idi) in df.index:
            print("\nregistro ja existe\n")
        else:
            # abre o arquivo no modo append p/ adicionar
            with open(path, 'a', newline="\n") as file:
                escritor = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
                # coloca o que vai ser add em uma lista
                data = [[int(idi), reg]]
                # escreve no csv a nova linha
                escritor.writerows(data)
            # printa a nova tabela
            imprimir = pd.read_csv(path, index_col=0, header=0)
            print(imprimir)

    if(op == '2'):
        # pega o Id
        idi = input("\nid do registro a ser alterado/consultado/removido: ")

        # checka se registro existe
        df = pd.read_csv(path, index_col=0, header=0)
        if int(idi) not in df.index:
            print("\nregistro nao existe\n")
        else:
            # procura no arquivo das flags se o id a ser alterado/consultado/removido ja esta em execucao
            emexec = 0
            with open("flag.txt", "r+") as flag:
                f1 = flag.readlines()
                for n in f1:
                    if n == idi + '\n':
                        emexec = 1
        
            if emexec == 1:
                print("\nregistro ja em execucao\n")
            else:
                # escreve no arquivo das flags que o registro atual esta sendo editado
                with open("flag.txt", "a+") as flag:
                    flag.writelines(idi + '\n')

                oper = input(
                    "\nselecione a operacao\n1.alterar 2.consultar 3.remover\n")

                #! alterar - OK
                if(oper == '1'):
                    novo = input("\ninsira o novo nome do registro: ")
                    # cria um dataframe a partir do csv
                    df = pd.read_csv(path, index_col=0, header=0)
                    # atualiza a linha correspondente ao Id
                    df.loc[int(idi), "Name"] = novo
                    # converte de volta para csv
                    print(df)
                    df.to_csv(path, quoting=csv.QUOTE_NONNUMERIC)

                # ! consultar - OK
                if(oper == '2'):
                    # cria um dataframe a partir do csv
                    df = pd.read_csv(path, index_col=0, header=0)
                    print("\nregistro: ")
                    # printa a partir do Id
                    print(df.iloc[int(idi) - 1, 0:1])

                #! remover OK
                if(oper == '3'):
                   # cria um dataframe a partir do csv
                    df = pd.read_csv(path, index_col=0, header=0)
                    # deleta a linha de acordo com o Id
                    df.drop(int(idi), axis=0, inplace=True)
                    # converte de volta para csv
                    df.to_csv(path, quoting=csv.QUOTE_NONNUMERIC)
                    print("\nregistro removido.\n")
                    imprimir = pd.read_csv(path, index_col=0, header=0)
                    print(imprimir)
            # remove do flags o idi que foi feito a operacao
            if emexec == 0:
                with open("flag.txt", 'r') as leitor:
                    # salva as linhas do flags em uma lista
                    nums = leitor.readlines()
                    # atualiza o valor do idi para ter o \n para poder ser removido da lista
                    idi = idi + '\n'
                    # remove o idi da lista 
                    nums.remove(idi)
                    # insere a lista de volta no flag.txt sem o idi
                    with open("flag.txt", 'w') as escritor:
                        for n in nums:
                            escritor.write(n)

    stop = int(input("\nrealizar outra operacao? 1. sim 2.nao\n"))

aaaa.close()
