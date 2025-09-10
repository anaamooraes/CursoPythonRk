#Loops: é uma extrutura que permite repetirmos um bloco de código enquanto uma condição for verdadeira, utilizamos para automatizar tarefas repetitivas e executar ações repetidas vezes. 

#For: é utilizado para iterar uma sequencia de elementos, repetir a mesma ação para cada elemento. 

print("\nFor utilizando lista:")
lista = [1, 2, 3, 4, 5]
for elemento in lista: 
  print(elemento)
#A cada elemento, temos um print diferente

print("\nFor utilizando tupla:")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
  print(elemento)

print("\nFor utilizando dicionario - chaves:")
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
for chave in pessoa.keys():
  print(chave)

print("\nFor utilizando dicionario - valores:")
for valor in pessoa.values():
  print(valor)

print("\nFor utilizando dicionario - itens(tuplas):")
for chave, valor in pessoa.items():
  print(f"{chave}: {valor}")

#Utilizando o loop for com a função range: 
#range(): retorna um intervalo numérico em formato de lista: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\nFor utilizando a função range:")
for numero in range(0,5):
  print("Número:", numero)

print("\nFor utilizando a função range() com len():")
lista = [1, 2, 3, 4, 5]
print(lista)
for indice in range(0, len(lista)):
  if indice == 3:
    lista[indice] = 5
  else:
    lista[indice] = 0
  print(lista)
#Utilizamos essa estrategia geralmente quando queremos alterar o valor dentro desta lista. 

#Utilizado para extrair as duas informações, indice e valor
print("\nFor utilizando a função enumerate():")
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
  print(f"{indice}: {valor}")
  #Caso eu queira trocar um valor:
  if indice == 1:
    print("Indice 1:")
