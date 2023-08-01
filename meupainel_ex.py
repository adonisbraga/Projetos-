menu = """ 

Bem vindo ao nosso sistema bancario, Selecione a opção que deseja:

[1] Depositar
[2] Sacar 
[3] Extrato
[0] Sair

Digite aqui: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3 



while True:
    
   opcao = input(menu)
   
   if opcao == "1": 
       valor = float(input("Informe o valor do deposito:"))
       
       if valor > 0:
           saldo += valor
           extrato += f"Depósito no valor de R$: {valor:.2f}\n"
       
       else:
           print("Valor indisponivel para saque, por favor refaça a operação.")
   

   elif opcao == "2":
       valor = float(input("Informe o valor que deseja sacar:"))
           
       excedeu_saldo = valor > saldo
           
       excedeu_limite = valor > limite
           
       excedeu_saques = numero_saques >= LIMITE_SAQUES
       
       if excedeu_saldo:
           print("Operação falhou ! Você não tem saldo suficiente")
           
       elif excedeu_limite:
           print("Operação falhou ! O valor do saque excede o limite")
           
       elif excedeu_saques:
           print("Operação falhou ! Número máximo de saque excedido ")
           
           
       if valor > 0:
        saldo -= valor
        extrato += f"saque R$: {valor:.2f}\n"
        numero_saques += 1
               
       else:
           print("Operação falhou valor indisponivel, refaça a operação")
       
       
   elif opcao == "3":
    print("\n===============Extrato===============")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nsaldo: R$ {saldo:.2f}")
    print("=======================================") 
        
   
   elif opcao == "0":
        break 
   
   
   else:
       print("Opção inválida, Por favor selecione novamente a opção desejada.")
            

  