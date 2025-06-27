import textwrap

# Constantes
LIMITE_SAQUES = 3
AGENCIA = "0001"

# Listas de dados
usuarios = []
contas = []

# Funções do sistema bancário.

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("Valor excede o limite por saque.")
    elif numero_saques >= limite_saques:
        print("Número máximo de saques atingido.")
    elif valor <= 0:
        print("Valor inválido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso.")
    return saldo, extrato, numero_saques


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso.")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Sem movimentações." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=========================================")


def criar_usuario():
    cpf = input("Informe o CPF (somente números): ")
    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("Usuário já cadastrado.")
        return

    nome = input("Informe o nome completo: ")
    nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário cadastrado com sucesso!")


def buscar_usuario(cpf):
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)


def criar_conta():
    cpf = input("Informe o CPF do usuário: ")
    usuario = buscar_usuario(cpf)
    if usuario:
        numero_conta = len(contas) + 1
        contas.append({
            "agencia": AGENCIA,
            "numero_conta": numero_conta,
            "usuario": usuario
        })
        print("Conta criada com sucesso!")
        print(f"Agência: {AGENCIA} | Conta: {numero_conta}")
    else:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")


def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for conta in contas:
        linha = f"""
        Agência: {conta["agencia"]}
        Conta: {conta["numero_conta"]}
        Titular: {conta["usuario"]["nome"]}
        """
        print(textwrap.dedent(linha))


# Execução principal
def main():
    saldo = 0
    extrato = ""
    numero_saques = 0

    while True:
        print("""
        ====== MENU ======
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [u] Criar usuário
        [c] Criar conta
        [l] Listar contas
        [q] Sair
        """)
        opcao = input("Escolha uma opção: ")

        if opcao == 'd':
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=500,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'u':
            criar_usuario()

        elif opcao == 'c':
            criar_conta()

        elif opcao == 'l':
            listar_contas()

        elif opcao == 'q':
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
