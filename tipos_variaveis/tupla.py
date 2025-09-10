#Tupla é muito semelhante a lista, com a diferença de ser ordenada e imutavel. Diferente da lista, depois de declarar uma tupla, não podemos adicionar, remover, atribuir outro valor...

# Tupla de exemplo: 
minha_tupla = (1, 2, 2, 3 , 4)
print("Minha tupla:", minha_tupla)

#Para exibir 1 elemento da tupla
print("minha tupla[0]:", minha_tupla[0])
print("minha tupla[2]:", minha_tupla[2])

#Para acessar o ultimo elemento: 
print("minha tupla[-1]:", minha_tupla[-1])

#Método count: retorna a quantidade de vezes que aperece o mesmo elemento na tupla.
contagem = minha_tupla.count(2)
print("Quantidade vezes que aparece o elemento:", contagem)

#Método index: onde o meu elemento está localizado na lista: 
indice = minha_tupla.index(3)
print("Onde está localizado o elemento 3?:", indice )