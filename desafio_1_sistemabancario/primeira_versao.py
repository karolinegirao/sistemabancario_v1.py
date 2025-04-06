##depósito, saque e extrato
from datetime import datetime

saldo = 0.0
historico = []
LIMITE_SAQUE = 500.00
LIMITE_SAQUES_DIARIOS = 3
saques_diarios = 0

while True:
    try:
        opcao = int(input("Escolha uma opção: \n[1] Extrato \n[2] Sacar \n[3] Depositar \n[0] Sair \n"))
        
        if opcao == 1:
            print("\n ---> Extrato <---")
            if not historico:
                print("Nenhuma transação realizada.")
            else:
                for transacao in historico:
                    print(f"{transacao['data']} | {transacao['tipo']: <10} | R$ {transacao['valor']:.2f}")
            print(f"Saldo atual: R${saldo:.2f}")
            print("---------------------")
    
        elif opcao == 2:
            if saques_diarios >= LIMITE_SAQUES_DIARIOS:
                print("Limite de saques diários atingido (3 saques por dia).")
                break

            try:
                sacar = float(input("Digite o valor que deseja sacar: R$ "))
                if sacar > 0:
                    if sacar > LIMITE_SAQUE:
                         print(f"Valor excede o limite de R$ {LIMITE_SAQUE:.2f} por saque.")
                    elif saldo >= sacar:
                        saldo -= sacar
                        saques_diarios += 1
                        print(f"Saque de {sacar:.2f} realizado com sucesso! Seu extrato atual é de {saldo:.2f}!")
                        historico.append({
                            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "tipo": "Saque",
                            "valor": -sacar
                        })
                    else:
                        print("Saldo insuficiente para realizar saque.")
                else:
                    print("O valor do saque deve ser maior que zero.")
            except ValueError:
                print("Valor inváido. Digite um número válido para saque")


    
        elif opcao == 3:
            try:
                valor = float(input("Digite o valor que deseja depositar: R$ "))
                if valor > 0:
                   saldo += valor
                   print(f"Seu depósito de R$ {valor:.2f} foi realizado com sucesso! Seu extrato atual é de {saldo:.2f}!")
                   historico.append({
                            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "tipo": "Depósito",
                            "valor": valor
                        })
                else:
                    print("O valor do depósito deve ser maior que zero")
            except ValueError:
                print("Valor inváido. Digite um número válido para depósito")    
        elif opcao == 0:
            print("Obrigada por usar nosso sistema bancário!")
            break
        else:
            print("Opção inválida. Por favor, selecione uma opção válida (0 a 3).")
    
    except ValueError:
        print("Entrada inválida. Digite apenas números!")


    

