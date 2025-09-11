#Módulos são arquivos que contêm definições e instruções que podem ser reutilizadas por outros programas. Existem módulos padrão, que já vem com Python, e módulos de terceiros, criados por outros programadores.
#Aprendendo a importar e utilizar módulos padrão, como o módulo math, que contém funções matematicas, como a função sqrt para calcular a raiz quadrada.
print("Exemplo de importação de um módulo padrão:")
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"A raiz quadrada de 25 é: {raiz_quadrada}")

print("\nExemplo de criação e utilização de um módulo personalizado")
from meu_modulo import saudacao, dobro

mensagem = saudacao("Ana")
resultado_dobro = dobro(5)
print(mensagem)
print(f"O dobro de 5 é: {resultado_dobro}")