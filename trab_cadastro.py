from os import system

clientes = []

# clientes = [
#     {'nome': 'Gregor Oliveira', 'cpf': '14373183635', 'data_nascimento': '31/01/2003', 'telefone': '984039502', 'naturalidade': 'Brasil', 'endereco': 'Rua Godofredo Machado', 'numero': '324', 'bairro': 'Roosevelt', 'cidade': 'Uberlândia', 'estado': 'MG'},
#     {'nome': 'Davi Mendes', 'cpf': '12345678999', 'data_nascimento': '11/12/1212', 'telefone': '123456789', 'naturalidade': 'Brasil', 'endereco': 'Rua Rua', 'numero': '1', 'bairro': 'Bairro Bairro', 'cidade': 'Uberlândia', 'estado': 'MG'},
#     {'nome': 'Izabel Oliveira', 'cpf': '12312312399', 'data_nascimento': '15/03/2005', 'telefone': '123412349', 'naturalidade': 'Brasil', 'endereco': 'Rua dos Buritis', 'numero': '1100', 'bairro': 'Vila Brasilia', 'cidade': 'Udia', 'estado': 'MG'},
#     {'nome': 'Fellipe de Neves', 'cpf': '98765432111', 'data_nascimento': '14/05/2002', 'telefone': '932103843', 'naturalidade': 'Brasil', 'endereco': 'Rua Olívia das Graças', 'numero': '114', 'bairro': 'Shopping Park', 'cidade': 'Uberlândia', 'estado': 'MG'}
# ]
def Menu():
    print("|------CADASTRO DE CLIENTES-----|")
    print("| 1 - Cadastrar                 |")
    print("| 2 - Pesquisar                 |")
    print("| 3 - Excluir                   |")
    print("| 4 - Atualizar                 |")
    print("| 5 - Sair do programa          |")
    print('|-------------------------------|')
    
    try:
        opcao = int(input("Escolha uma opção: "))
        return opcao
    except ValueError:
        print("\tErro. Escolha um número inteiro!")
        return 0


def validar_nome(nome):
    if len(nome.split()) > 1:
        return True
    else:
        return False

def validar_cpf(cpf_validando):
    if len(cpf_validando) == 11:
        if cpf_validando.isdigit():
            return True
    return False

def cpf_existe(cpf_verificar, clientes_verificiar):
    for pessoa in clientes_verificiar:
        if cpf_verificar == pessoa["cpf"]:
            return True
    return False

def validar_data_nascimento(data_verificar):
    if len(data_verificar) == 10:
        if (data_verificar[2] == "/" ) and (data_verificar[5] == "/"):
            return True
    return False


def validar_telefone(telefone_validando):
    if len(telefone_validando) == 9:
        if telefone_validando.isdigit():
            return True
    return False


def cadastrar():
    print("\n--- Novo Cadastro ---")
    while True:
        nome = input("Digite o nome do Cliente: ")
        if validar_nome(nome):
            break
        else:
            print("\tERRO: Digite NOME e SOBRENOME!\n")

    while True:
        cpf = input("CPF (apenas números): ")
        if validar_cpf(cpf):
            if cpf_existe(cpf, clientes):
                print("\tERRO! CPF já cadastrado!\n")
            else:
                break
        else:
            print("\tERRO: Formato inválido! Digite 11 NÚMEROS.\n")
        
    while True:
        data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
        if validar_data_nascimento(data_nascimento):
            break
        else:
            print("\tErro! Digite a data no formato válido: DD/MM/AAAA - (Lembre de usar as barras).\n")

    while True:
        telefone = input("Digite o número de telefone (9 números):")
        if validar_telefone(telefone):
            break
        else:
            print("\tErro! Digite o telefone com 9 números.\n")

    naturalidade = input("Digite a naturalidade: ")
    endereco = input("Digite o endereço: ")
    numero = input("Digite o numero: ")
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")

    cadastrando_cliente = criar_dicionario(nome, cpf, data_nascimento, telefone, naturalidade, endereco, numero, bairro, cidade, estado)
    clientes.append(cadastrando_cliente)

    print("\t _______________________________________")
    print("\t|    Cliente cadastrado com sucesso!    |")
    print("\t|_______________________________________|\n")


def criar_dicionario(nome, cpf, data_nascimento, telefone, naturalidade, endereco, numero, bairro, cidade, estado):
    novo_cliente = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "telefone": telefone,
        "naturalidade": naturalidade,
        "endereco": endereco,
        "numero": numero,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado
    }
    return novo_cliente

def nome_ou_cpf():
    while True:
        try:
            escolha = int(input("Digite 1 para pesquisar por nome.\nOu\nDigite 2 para pesquisar por CPF.\nEscolha: "))
            if ((escolha == 1 ) or (escolha == 2)):
                return escolha
            else:
                print("\tERRO! Escolha entre um ou dois!\n")
        except ValueError:
            print("\tERRO! Escolha entre um ou dois!\n")

def nome_existe(nome_verificar, clientes_verificiar):
    for pessoa in clientes_verificiar:
        if nome_verificar == pessoa["nome"]:
            return True
    return False

def pesquisar():
    opcao_nomeCPF = nome_ou_cpf()
    if opcao_nomeCPF == 1:
        while True:
            nomeCPF = input('\nDigite o nome que deseja pesquisar ou "0" para sair: ')
            if nomeCPF == "0":
                print("\tSaindo.\n")
                break
            if nome_existe(nomeCPF, clientes):
                pesquisando_nome(nomeCPF, clientes)
                break
            else:
                print("\tEsse nome não existe!")
    if opcao_nomeCPF == 2:
        while True:
            nomeCPF = input('\nDigite o CPF que deseja pesquisar ou "0" para sair: ')
            if nomeCPF == "0":
                break
            if cpf_existe(nomeCPF, clientes):
                pesquisando_cpf(nomeCPF, clientes)
                break
            else:
                print("Esse CPF não existe!")

def pesquisando_nome(nomeCPF, clientes_verificar):
    for pessoas in clientes_verificar:
        if nomeCPF == pessoas["nome"]:
            print('\n')
            for chave, valor in pessoas.items():
                print(f"{chave}: {valor}")
            print("\n")


def pesquisando_cpf(nomeCPF, clientes_verificar):
    for pessoas in clientes_verificar:
        if nomeCPF == pessoas["cpf"]:
            print('\n')
            for chave, valor in pessoas.items():
                print(f"{chave}: {valor}")
            print('\n')

def excluir_cliente():
    while True:
        cpf = input("Digite o CPF do cliente para a exclusão: ")
        if cpf_existe(cpf, clientes):
            for pessoas in clientes:
                if pessoas["cpf"] == cpf:
                    clientes.remove(pessoas)
            print("\t ______________________________________")
            print("\t|    Cliente excluído com sucesso!    |")
            print("\t|_____________________________________|\n")
            break
        else:
            print("ERRO! CPF não existe.")


def atualizar_cliente():
    while True:
        cpf_para_atualizar = input('Digite o CPF para atualização ou "0" para sair: ')
        if cpf_para_atualizar == "0":
            break
        if cpf_existe(cpf_para_atualizar, clientes):
            break
        else:
            print("ERRO! CPF não existe.")
    if cpf_para_atualizar != "0":
        while True:         
            system("cls")
            print("  ~~~~ O que deseja atualizar? ~~~~")
            print("| 1 - Nome                         |")
            print("| 2 - CPF                          |")
            print("| 3 - Data de nascimneto           |")
            print("| 4 - Telefone                     |")
            print("| 5 - Naturalidade                 |")
            print("| 6 - Endereço                     |")
            print("| 7 - Número                       |")
            print("| 8 - Bairro                       |")
            print("| 9 - Cidade                       |")
            print("| 10 - Estado                      |")
            print("| 11 - Sair                        |")
            print('|----------------------------------|')
            
            try:
                opcao = int(input("Escolha uma opção: "))
                match opcao:
                    case 1: #nome
                        while True:
                            nome = input("Digite o novo nome: ")
                            
                            if validar_nome(nome):
                                for pessoas in clientes:
                                    if pessoas["cpf"] == cpf_para_atualizar:
                                        pessoas["nome"] = nome
                                        print("\t _____________________________________")
                                        print("\t|    Nome atualizado com sucesso!     |")
                                        print("\t|_____________________________________|\n")
                                        input("\tPressione <ENTER> para continuar...\n")
                                break
                            else:
                                print("\tERRO: Digite NOME e SOBRENOME!\n")
                    case 2: #cpf
                        while True:
                            cpf = input("Digite o novo CPF: ")
                            
                            if validar_cpf(cpf):
                                for pessoas in clientes:
                                    if pessoas["cpf"] == cpf_para_atualizar:
                                        pessoas["cpf"] = cpf
                                        print("\t _____________________________________")
                                        print("\t|    CPF atualizado com sucesso!      |")
                                        print("\t|_____________________________________|\n")
                                        input("\tPressione <ENTER> para continuar...\n")
                                break
                            else:
                                print("\tERRO: Formato inválido! Digite 11 NÚMEROS.\n")
                    case 3: #data_nascimento
                        while True:
                            data_nascimento = input("Digite a nova data de nascimento: ")
                            
                            if validar_data_nascimento(data_nascimento):
                                for pessoas in clientes:
                                    if pessoas["cpf"] == cpf_para_atualizar:
                                        pessoas["data_nascimento"] = data_nascimento
                                        print("\t ___________________________________________________")
                                        print("\t|    Data de nascimento atualizada com sucesso!     |")
                                        print("\t|___________________________________________________|\n")
                                        input("\tPressione <ENTER> para continuar...\n")
                                break
                            else:
                                print("\tErro! Digite a data no formato válido: DD/MM/AAAA - (Lembre de usar as barras).\n")
                    case 4: #telefone
                        while True:
                            telefone = input("Digite o novo telefone: ")

                            if validar_telefone(telefone):
                                for pessoas in clientes:
                                    if pessoas["cpf"] == cpf_para_atualizar:
                                        pessoas["telefone"] = telefone
                                        print("\t _________________________________________")
                                        print("\t|    Telefone atualizado com sucesso!     |")
                                        print("\t|_________________________________________|\n")
                                        input("\tPressione <ENTER> para continuar...\n")
                                break
                            else:
                                print("\tErro! Digite o telefone com 9 números.\n")
                    case 5: #naturalidade
                        while True:
                            naturalidade = input("Digite a nova naturalidade: ")

                            for pessoas in clientes:
                                if pessoas["cpf"] == cpf_para_atualizar:
                                    pessoas["naturalidade"] = naturalidade
                                    print("\t _____________________________________________")
                                    print("\t|    Naturalidade atualizado com sucesso!     |")
                                    print("\t|_____________________________________________|\n")
                                    input("\tPressione <ENTER> para continuar...\n")
                            break
                    case 6: #endereço
                        while True:
                            endereço = input("Digite um novo endereço: ")
                            
                            for pessoas in clientes:
                                if pessoas["cpf"] == cpf_para_atualizar:
                                        pessoas["endereco"] = endereço
                                        print("\t _____________________________________________")
                                        print("\t|    Endereço atualizado com sucesso!         |")
                                        print("\t|_____________________________________________|\n")
                                        input("\tPressione <ENTER> para continuar...\n")
                            break
                    case 7: #número da casa/apartamento
                        while True: 
                            número = input("Digite um novo número: ")

                            for pessoas in clientes:
                                if pessoas["cpf"] == cpf_para_atualizar:
                                        pessoas["numero"] = número
                                        print("\t _____________________________________________")
                                        print("\t|    Número atualizado com sucesso!           |")
                                        print("\t|_____________________________________________|\n")
                                        input("\tPressione <ENTER> para continuar...\n")
                            break
                    case 8: #bairro
                        while True:
                            bairro = input("Digite um novo bairro: ")

                            for pessoas in clientes:
                                if pessoas["cpf"] == cpf_para_atualizar:
                                        pessoas["bairro"] = bairro
                                        print("\t _____________________________________________")
                                        print("\t|    Bairro atualizado com sucesso!           |")
                                        print("\t|_____________________________________________|\n")
                                        input("\tPressione <ENTER> para continuar...\n")
                            break
                    case 9: #cidade
                        while True:
                            cidade = input("Digite uma nova cidade: ")
                             
                            for pessoas in clientes:
                                if pessoas["cpf"] == cpf_para_atualizar:
                                        pessoas["cidade"] = cidade
                                        print("\t _____________________________________________")
                                        print("\t|    Cidade atualizado com sucesso!           |")
                                        print("\t|_____________________________________________|\n")
                                        input("\tPressione <ENTER> para continuar...\n")
                            break
                    case 10: #estado
                        while True:
                            estado = input("Digite um novo estado: ")

                            for pessoas in clientes:
                                if pessoas["cpf"] == cpf_para_atualizar:
                                        pessoas["estado"] = estado
                                        print("\t _____________________________________________")
                                        print("\t|    Estado atualizado com sucesso!           |")
                                        print("\t|_____________________________________________|\n")
                                        input("\tPressione <ENTER> para continuar...\n")
                            break
                    case 11:
                        print("\t ______________________________")
                        print("\t|    Voltando para o menu!     |")
                        print("\t|______________________________|\n")
                        break
                    case _:
                        print("\tERRO! Digite uma opção válida.")
                        input("\tPressione <ENTER> para continuar...\n")
            except ValueError:
                print("ERRO! Digite uma opção válida (1 a 10)!")

opcao = 0
while (opcao != 5):
    opcao = Menu()

    system("cls")
    match opcao:
        case 1:
            print("Cadastrando...\n")
            cadastrar()
        case 2:
            print("Pesquisando...\n")
            pesquisar()
        case 3:
            print("Excluindo...\n")
            excluir_cliente()
        case 4:
            print("Atualizando...\n")
            atualizar_cliente()
        case 5:
            print("\tSaindo do programa!\n")
        case 6:
            for pessoas in clientes:
                for valor, chave in pessoas.items():
                    print(f'{valor}: {chave}')
                print('-'*20)
        case _:
            print("\tErro. Escolha um opção válida (1 a 5)!\n")
    if opcao != 5:
        input("\tPressione <ENTER> para continuar...\n")