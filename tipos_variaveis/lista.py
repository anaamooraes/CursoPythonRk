#Declaração 
minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

#Exibindo a lista
print("Minha lista de exemplo", minha_lista)

#Exibindo os elementos da lista 
#Para exibiri apenas 1 elemento da lista: 
print("minha_lista[0]:", minha_lista[0]) 
print("minha_lista[5]:", minha_lista[5]) 

#Para exibir do elemento 1 ao elemento 7: 
print("minha_lista[1:7]", minha_lista[1:7])

#Para exibir do começo da lista até o alvo: 
print("minha_lista[:5]", minha_lista[:6])

#Para exibir de 1 elemento selecionado para o final:
print("minha_lista[2:]", minha_lista[2:])

#Para modificar os elementos na lista: 
minha_lista[0] = "python"
print("minha lista de exemplo", minha_lista)

#Métodos de lista: 
#Método append(): Adiciona um elemento ao final da lista
minha_lista.append(6)
minha_lista.append("macbock")
minha_lista.append(6)
minha_lista.append("baton")
print("Após append(6):", minha_lista)

#Método index
#Retorna o indice do primeiro elemento = ao valor especificado
indice = minha_lista.index(6)
print("Indice do elemento 6:", indice)
#Selecionei um elemento e consigo visualizar onde está localizado na minha lista. 

#Método insert: Insere um elemento em um indice espacifico, acrescentar um elemento na onde eu quiser.
minha_lista.insert(2, 10)
print("Após o insert(2, 10):", minha_lista)

#Método pop: excluir um elemento especifico 
elemento_removido = minha_lista.pop(3)
print("Elemento removido:", elemento_removido)
print("Minha lista após o .pop(3:)", minha_lista)

#Método remove: remove o primeiro elemento com o valor especifico:
minha_lista.remove(True)
print("Minha lista após o remove(True):", minha_lista)

#Método sort: Para deixar minha lista em ordem crescente: 
''' minha_lista.sort()
print("Após o sort():", minha_lista) '''
#Irá dar erro pois temos mais de um tipo de elemento, para dar certo precisamos ter somente numéros ou strings.. 