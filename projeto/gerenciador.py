def adicionar_tarefa(tarefas, nome_tarefa):

  #Tarefas: nome da tarefa 
  #Completada: indica se essa tarefa foi completada ou não
  tarefa = {"tarefa": nome_tarefa, "completada": False}
  tarefas.append(tarefa)
  print(f"A tarefa {nome_tarefa} foi adicionada com sucesso!")
  return

tarefas = []
while True:
  print("\nMenu do Gerenciador de Lista de Tarefas:") 
  print("\n1. Adicionar uma tarefa")
  print("2. Ver tarefa")
  print("3. Atualizar tarefa")
  print("4. Completar tarefa")
  print("5. Deletar tarefas completadas")
  print("6. Sair")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome_tarefa = input("Digite qual tarefa deseja adicionar: ")
    adicionar_tarefa(tarefas, nome_tarefa)

  elif escolha == "6":
    break
  
  print("Programa finalizado.")