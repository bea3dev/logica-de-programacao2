lista_de_compras=[]

while True:
    item=input("Adicionar Item a Lista: ")
    
    if item=="0":
        break
    lista_de_compras.append(item)
print(lista_de_compras)