import pandas as pd

def forca_opcao(msg, lista):
    x = input(msg)
    while x not in lista:
        print("Digite uma opção cadastrada!")
        x = input(msg)
    return x

def login(dic_usuario):
    email_login = input("Digite seu email: ")
    senha_login = input("Digite sua senha: ")
    i = 3
    while i > 0:
        if email_login != dic_usuario['email'] or senha_login != dic_usuario['senha']:
            if i == 1:
                print("Seu número de tentativas acabou! Tente novamente mais tarde.")
                quit()
            i -= 1
            print(f"Email ou senha incorretos! Mais {i} tentativas!")
            email_login = input("Digite seu email: ")
            senha_login = input("Digite sua senha: ")
            continue
        else:
            break
    return

def printar_dic(dic):
    print(pd.DataFrame(dic))
    return

def perguntar_destino(lista, dic):
    for i in range(len(lista)):
        print(f"{i} : {lista[i]}")
    destino = int(forca_opcao("Para qual destino você quer ir? ", ['0', '1', '2']))
    if destino == 0:
        for i in range(3):
            print(f"----- OPÇÃO {i + 1} -----")
            for key in dic.keys():
                print(f"{key} : {dic[key][i]}")
    elif destino == 1:
        for i in range(3, 6):
            print(f"----- OPÇÃO {i - 2} -----")
            for key in dic.keys():
                print(f"{key} : {dic[key][i]}")
    else:
        for i in range(6, 9):
            print(f"----- OPÇÃO {i - 5} -----")
            for key in dic.keys():
                print(f"{key} : {dic[key][i]}")
    return


def add_fav(dic_onibus, dic_usuario, lista_opcoes):
    for i in range(len(dic_onibus['nome'])):
        print(f"{i} : {dic_onibus['número'][i]} - {dic_onibus['nome'][i]}")
    opcao_fav = int(forca_opcao("Qual ônibus você deseja adicionar aos seus favoritos? ", lista_opcoes))
    if 'lista de favoritos' not in dic_usuario:
        dic_usuario['lista de favoritos'] = []
    while opcao_fav in dic_usuario['lista de favoritos']:
        print("Esse ônibus ja está na lista de favoritos! Escolha outro.")
        opcao_fav = int(forca_opcao("Qual ônibus você deseja adicionar aos seus favoritos? ", lista_opcoes))
    dic_usuario['lista de favoritos'].append(opcao_fav)
    return opcao_fav

def verificar_fav(dic_onibus, dic_usuario):
    if 'lista de favoritos' in dic_usuario:
        print("Lista de Favoritos: ")
        for i in range(len(dic_usuario['lista de favoritos'])):
            print(
                f"{dic_onibus['número'][dic_usuario['lista de favoritos'][i]]} - {dic_onibus['nome'][dic_usuario['lista de favoritos'][i]]}")
    else:
        print("Você não adicionou nenhum ônibus a sua lista de favoritos! ")
    return