#Condicionais: if(se), elif(se não outra condição) e else(se não)
#Exemplo de if: 
idade = 18 
print("Exemplo de comando if:")
if idade >= 18:
  print("Você é maior de idade.")
if idade == 19:
  print("Você tem 19 anos.")
if idade <= 18:
  print("você é menor de idade")
if idade != 10:
  print("Você não tem 10 anos.")

#Exemplo do else: 
idade = 17 
print("Exemplo de comando else:")
if idade >= 18:
  print("Você é maior de idade.")
else:
  print("Você é menor de idade.")

#Exemplo do elif e else: 
idade = 18 
print("Exemplo de comando else:")
if idade >= 18:
  print("Você é maior de idade.")
elif idade >= 12:
  print("Você é um adolescente.")
else:
  print("Você é menor de idade.")

#Como construir em apenas uma linha: 
mensagem = "Você pode tirar a carteira de habilitação" if idade >= 18 else "Você não pode tirar a carteira de hebilitação" 
print(mensagem)

#Entrada de dados: utilizamos a função input para interagir com o usuario 
idade = int(input("Quantos anos você tem?"))
print(idade)