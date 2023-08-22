menu = """ 

Bem vindo ao nosso sistema de cotações , escolha uma das opções para ver a cotação atual da moeda 

[1] - Dolar
[2] - Euro
[0] - Sair

Digite aqui: """

real = 5.42
dolar = 4.87
euro = 5.43

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        real = float(input('Informe o valor em R$ que deseja ser cotado:'))
        
        if dolar > 4.87:
            dolar / real
            
        print(f"\nO valor em Real de R${real} cotadado para o dolar é de: US$ {real/dolar:.2f}") 
        
    if opcao == "2":
        real = float(input('Informe o valor em R$ que deseja ser cotado para o euro:'))    
            
        if euro > 5.36:
            euro / real 
        
        print(f"\nO valor em Real R$ {real} convertido para o euro é de: {real/euro:.2f}")    
            
            
    
    
    if opcao == "0":
        break    
            