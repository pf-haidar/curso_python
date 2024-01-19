
def adicionar_tarefa(tarefas: list, nome_tarefa):
  tarefa = {"tarefa": nome_tarefa, "completada": False}
  tarefas.append(tarefa)
  print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
  return

def ver_tarefas(tarefas: list):
  print("\nLista de Tarefas:")
  for indice, tarefa in enumerate(tarefas, start=1):
    status = "✓" if tarefa["completada"] else " "
    nome_tarefa = tarefa["tarefa"]
    print(f"{indice}. [{status}] {nome_tarefa}")
  return

def atualizar_nome_tarefa(tarefas: list, indice_tarefa, novo_nome_tarefa):
  indice_tarefa_ajustado = int(indice_tarefa) - 1
  if(indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas)):
    tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
    print(f"Tarefa {indice_tarefa} atualizada para \"{novo_nome_tarefa}\"")
  else:
    print("Indice de tarefa invalido.")
  return

def completar_tarefa(tarefas: list, indice_tarefa):
  indice_tarefa_ajustado = int(indice_tarefa) - 1
  if(indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas)):
    tarefas[indice_tarefa_ajustado]["completada"] = True
    print(f"Tarefa {indice_tarefa} marcada como completada!")
  elif tarefas[indice_tarefa_ajustado]["completada"] == True:
    print(f"Tarefa {indice_tarefa} já está marcada como completada!")
  else:
    print("Indice de tarefa invalido.")
  return

def deletar_tarefas_completadas(tarefas: list):
  for tarefa in enumerate(tarefas):
    if tarefa["completada"]:
      tarefas.remove(tarefa)
      
  print("Tarefas completadas foram deletadas!")
  return

tarefas = []
while True:
  print("\nMenu do Gerenciador de Lista de tarefas:")
  print("1. Adicionar Tarefa")
  print("2. Ver Tarefa")
  print("3. Atualizar Tarefa")
  print("4. Completar Tarefa")
  print("5. Deletar tarefas completadas")
  print("6. Sair")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
    adicionar_tarefa(tarefas, nome_tarefa)
  elif escolha == "2":
    ver_tarefas(tarefas)
  elif escolha == "3":
    ver_tarefas(tarefas)
    indice_tarefa = input("Digite o numero da tarefa que deseja atualizar: ")
    novo_nome = input("Digite o novo nome da tarefa: ")
    atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome) 
  elif escolha == "4":
    ver_tarefas(tarefas)
    indice_tarefa = input("Digite o numero da tarefa que deseja atualizar: ")
    completar_tarefa(tarefas, indice_tarefa)
  elif escolha == "5":
    deletar_tarefas_completadas(tarefas)
    ver_tarefas(tarefas)
  elif escolha == "6":
    break

print("Programa finalizado!")