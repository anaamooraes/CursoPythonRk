# Declaração 
nome_completo = "Ana Lívia Moraes"

nome_completo_aspas = """Ana Lívia 
Moraes"""

nome_completo_quebra = "Ana Lívia \
  Moraes"

nome = "Ana Lívia"
sobrenome = "Moraes"

# Formatação 
print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo)
print("Nome completo (3a forma):" + "Ana Lívia" + "Moraes")
print("Nome completo (4a forma):" + "Ana Lívia", "Moraes")
print("Nome completo (5a forma):", nome_completo_aspas)
print("Nome completo (6a forma):", nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome_completo)
print("Nome completo (8a forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9a forma): {nome} {sobrenome}")
print("Nome completo (10a forma): {} {}".format(nome, sobrenome))

#nome.uper()  TORNA TODAS AS LETRAS PARA VISUALIZAÇÃO MAIUSCULA.
#nome.lower() torna todas as letras para visualização minuscula.
#nome.count("a")  conta quantas letras A tem na variável nome. 
#nome.find("a")  me diz em qual posição da variável a letra A está. (sempre começamos com o 0)
#nome.replace("a", "b")  irá trocar a letra A pela letra B.
""" 
EXEMPLO DE REPLACE EM NÚMERO DE TELEFONE: 
(19) 99845-0321
telefone.replace("(", "").replace (")", "").replace("-","") 
19998450321
"""
#nome.strip("a")  remove todas as letras A do inicio e do fim da variável.
#nome.rstrip("a") remove todas as letras A do fim da variável. 