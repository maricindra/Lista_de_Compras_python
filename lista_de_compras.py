outros =[]
pet =[]
limpeza = []
alimento = []

print("\nSeja bem vindo!\nPrepare sua lista de compras de forma organizada!\n")
print("\nPara terminar a lista digite: FIM \nPara começar digite o seu primeiro item ")
print("\nTemos as categorias: Alimento, Limpeza, Pet e Outros ")

while True:
    item = str(input("\nQual item você precisa?\n")) 
    if item.lower() == "fim":
        break

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

    else:
        print("\nCategoria invalida.\nTemos as categorias: Alimento, Limpeza, Pet e Outros. ")

print("\nSua lista de compras:\n")
print("Alimento:", alimento ,"total de: ", len(alimento) , "itens")
print("Limpeza:", limpeza,   "total de: ", len(limpeza) , "itens" )
print("Pet:", pet, "total de: " , len(limpeza) , "itens")
print("Outros:", outros, "total de: ", len(outros), "itens")


print("\nNão se esqueça e Boas compras!")
   


              


