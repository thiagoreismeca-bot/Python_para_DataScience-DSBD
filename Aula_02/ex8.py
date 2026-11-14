while True:
    try:
 
        idade = int(input("Digite sua idade: "))
   
        if(idade<0):
            print('Digite uma idade valida')
        else:
            print(f"Sua idade é {idade} anos")
            break
 
 
    except:
 
        print("Erro: digite um número inteiro válido")