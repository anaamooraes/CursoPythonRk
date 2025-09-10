#Dicionario no Python é uma coleção não ordenada de pares, chaves e valores. 
""" Não ordenada: Não temos ordem como a lista e a tupla. 
"""

#Criando um dicionario de exemplo: 
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo" }
print("Meu dicionario de exemplo:", pessoa)

#Acessando valores por chave: 
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

#Se eu quiser atribuir um novo valor para o meu dicionario já criado: 
pessoa["sobrenome"] = "Silva"
print("Sobrenome:", pessoa["sobrenome"])
print("Meu dicionario de exemplo:", pessoa)

#O dicionario aceita criarmos tudo, textos, inteiros, float, booleanos, lista e até outro dicionario. 

#Para alterar ou atualizar um valor já existente: 
pessoa["idade"] = 31
print("Idade atualizada:", pessoa["idade"])

#Para remover uma chave e valor existente: 
del pessoa["sobrenome"]
print("Meu dicionario de exemplo:", pessoa)

#Métodos: keys(retorno de todas as chaves do dicionario), values(retorno da lista de todos os valores), items(retorna uma lista de tuplas com chaves e valores)

#Keys 
chaves = list(pessoa.keys())
print("Chaves do dicionario:", chaves)
print("Primeira chave:", chaves[0])

#Values
valores = list(pessoa.values())
print("Valores do dicionario:", valores)
print("Primeiro valor do dicionario:", valores[0])

#Items
itens = list(pessoa.items())
print("Pares de chave e valor do dicionario:", itens)
print("Primeira tupla do dicionario:", itens[0]) 
print("Para acessar o primeiro valor da tupla:", itens[0] [1])
print("Para acessar chave-valor: %s = %s" % (itens[0] [0], itens[0] [1]))
