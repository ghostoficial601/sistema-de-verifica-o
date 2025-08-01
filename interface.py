import json
import os



def carregar(arquivo):
    with open(arquivo, "r", encoding="UTF-8")as f :
        return json.load(f)

def salvar(caminho,arquivo):
    with open(caminho, 'w', encoding="UTF-8") as f:
        json.dump(arquivo, f, ensure_ascii=False, indent=4)

def criar(caminho,arquivo):
    if not os.path.exists():
        with open(caminho, "w", encoding="UTF-8") as f:
            json.dump(arquivo, f, ensure_ascii=False, indent=4)



def cadastrar():
    caminh = "dados.json"
    perfis = carregar(arquivo=caminh)
    
    nome = str(input("Escreva seu nome: "))
    idade = int(input("Escreva a sua idade: "))
    email = str(input("Por favor escreva seu email: "))
    senha = str(input("Escreva uma senha: "))

    while not "@" in email:
        print("\nERRO!! EMAIL INCORRETO!!!\n")
        email = str(input("Por favor escreva seu email: "))
        if "@" in email:
            break
        

    # Lembrar de fazer verificação através de código e não de senha
    perfil = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "senha": senha #isso vai ser temporário
    }
    perfis.append(perfil)
    salvar(caminho=caminh,arquivo=perfis)
    return f"{nome} seu cadastro foi Completo"

def login():
    caminh = "dados.json"
    perfis = carregar(arquivo=caminh)
    procure = False
    email = str(input("\nEmail:\n-> "))
    senha = str(input("\nSenha:\n--> "))


    
    for perfil in perfis:
        if perfil['email'] == email and perfil['senha'] == senha:
            procure = True
            return True
        elif perfil['email'] != email or perfil['senha'] != senha:
            while True:
                print("\n --ERRO!!-- \n Dados inseridos incorretos.\n")
                email = str(input("\nEmail:\n-> "))
                senha = str(input("\nSenha:\n--> "))
                if perfil['email'] == email and perfil['senha'] == senha:
                    procure = True
                    return procure
                elif perfil['email'] != email or perfil['senha'] != senha:
                    print("\n")




while True:
    decision = str(input("Vc gostaria de:\n 1.login\n 2.Cadastrar\n 0.Encerrar programa --> "))
    if decision in ["0","encerrar","encerrar programa"]:
        break
    elif decision in ["1", "login"]:
        print(login())
    elif decision in ["2", "cadastrar"]:
        print(cadastrar())
        break
    else:
        print("Erro de digitação")
    
