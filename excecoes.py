print("Exemplo de captura de exeções:")
while True:
  try:  
    numero = int(input("Digite um número inteiro:"))
    resultado = 10 / numero
  except ValueError as e:
    print(f"Erro de value error: {e}")  
    raise ValueError("Tipo de variaveis incompativeis")
  except Exception as e:
    print(f"Erro: {e}")
  else: 
    print(f"Resultado {resultado}")
  finally:
    print("Operação finalizada.")

#Aqui conseguimos fazer uma tratativa em caso de erros. Com while True impedimos o programa de ser interrompido, com try e except conseguimos tratar o erro do usuario. raise permite que vc interrompa propositalmente o código. finally é utilizado para executar algo dando certo ou errado. 

