# Exemplo 
def saudacao(nome):
  print(f"Olá, {nome}!")

print("\nChamando a função saudação:")
saudacao("Alice")
saudacao("Bob")

#Função com retorno
def quadrado(numero):
  resultado = numero ** 2
  return resultado 
print("\nChamando a função quadrado: ")
resultado_quadrado = quadrado(5)
print("Resultado da função quadrado:", resultado_quadrado)

#Chamando uma função com multiplos parametros: 
def soma(numero1, numero2):
  resultado = numero1 + numero2 
  return resultado
print("\nChamanado a função soma: ")
resultado_soma = soma(20, 50)
print("A soma do numero 20 e numero 50 é:", resultado_soma)