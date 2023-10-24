# Criando uma Lista de Compras para organização com o Python.
# Primeiramente Criar as listas, para armazenar as strings:
outros =[]
pet =[]
limpeza = []
alimento = []

#Introdução e apresentação ao Usuário:
print("\nSeja bem vindo!\nPrepare sua lista de compras de forma organizada!\n")
print("\nPara terminar a lista digite: FIM \nPara começar digite o seu primeiro item ")
print("\nTemos as categorias: Alimento, Limpeza, Pet e Outros ")

#Criando um Loop para adicionar itens varias vezes, e só parar quando o usuário digitar fim
# Utilizamos um While e um Break. o lower() serve para a entrada de letras Maiusculas:
while True:
    item = str(input("\nQual item você precisa?\n")) 
    if item.lower() == "fim":
        break
        
# Organizando as Categorias para o usuário notar itens de importância.
    categoria = str(input(f"\n{item} , de qual categoria é?\n"))
    categoria = categoria.lower()
    if categoria == "alimento": 
        alimento.append(item)
        print(alimento)
        
    elif categoria == "limpeza":
        limpeza.append(item)
        print(limpeza)

    elif categoria == "pet":
        pet.append(item)
        print(pet)

    elif categoria == "outros":
        outros.append(item)
        print(outros)
# Redirecionando o usuário para o menu principal
    else:
        print("\nCategoria invalida.\nTemos as categorias: Alimento, Limpeza, Pet e Outros. ")

# Resultado de forma organizada, contando quantos itens de cada categoria e quais itens ele adicionou.
print("\nSua lista de compras:\n")
print("Alimento:", alimento ,"total de: ", len(alimento) , "itens")
print("Limpeza:", limpeza,   "total de: ", len(limpeza) , "itens" )
print("Pet:", pet, "total de: " , len(limpeza) , "itens")
print("Outros:", outros, "total de: ", len(outros), "itens")

# Finalizando
print("\nNão se esqueça e Boas compras!")
   


              


