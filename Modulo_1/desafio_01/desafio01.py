
def add_contact(contacts: list):
    contact_name = input("Nome do contato: ")
    contact_phone = input("Número do contato: ")
    contact_email = input("E-mail do contato: ")
    contact = {"name": contact_name, "phone": contact_phone, "email": contact_email, "isFavorite": False}
    contacts.append(contact)
    print(f"Contato {contact_name} adicionado com sucesso!")
    return

def get_contact_list(contacts: list):
    print("\nLista de Contatos: ")
    for index, contact in enumerate(contacts, start=1):
        favorite = " ★ " if contact["isFavorite"] else " "
        contact_name = contact["name"]
        contact_phone = contact["phone"]
        contact_email = contact["email"]
        print(f"{index}.{favorite}{contact_name} | {contact_phone} | {contact_email}")
    return

def edit_contact(contacts: list, contact_index):
    formatted_index = int(contact_index) - 1
    if(formatted_index >= 0 and formatted_index < len(contacts)):
        contacts[formatted_index]["name"] = input("Digite novo nome: ")
        contacts[formatted_index]["phone"] = input("Digite novo número: ")
        contacts[formatted_index]["email"] = input("Digite novo email: ")
        print(f"Contato {contact_index} atualizado!")
    else: 
        print("Indice de contato inválido!")
    return

def change_favorite_status(contacts: list, contact_index):
    formatted_index = int(contact_index) - 1
    if(formatted_index >= 0 and formatted_index < len(contacts)):
        if contacts[formatted_index]["isFavorite"]:
            contacts[formatted_index]["isFavorite"] = False
            print(f"Contato {contact_index} removido dos favoritos!")
        else:
            contacts[formatted_index]["isFavorite"] = True
            print(f"Contato {contact_index} adicionado dos favoritos!")
    else:
        print("Indice de contato inválido!")
    return   

def get_favorite_contact_list(contacts: list):
    print("\nLista de Contatos Favoritos: ")
    for contact in contacts:
        if contact["isFavorite"]:
            contact_name = contact["name"]
            contact_phone = contact["phone"]
            contact_email = contact["email"]
            print(f"★. {contact_name} | {contact_phone} | {contact_email}")
    return

def delete_contact(contacts: list, contact_index):
    formatted_index = int(contact_index) - 1
    contacts.pop(formatted_index)
    print(f"Contato {contact_index} removido com sucesso!")
    return

contacts = []
while True:
    print("\nMenu da Agenda de Contatos:")
    print("1. Adicionar um contato")
    print("2. Visualizar os contatos")
    print("3. Editar um contato")
    print("4. Adicionar/Remover um contato dos favoritos")
    print("5. Visualizar os contatos favoritos")
    print("6. Apagar um contato")
    print("7. Sair")
    
    selected_option = input("Digite sua escolha: ")
    
    if selected_option == "1":
        add_contact(contacts)
    elif selected_option == "2":
        get_contact_list(contacts)
    elif selected_option == "3":
        get_contact_list(contacts)
        selected_contact_index = input("Digite o número do contato que deseja atualizar: ")
        edit_contact(contacts, selected_contact_index)
    elif selected_option == "4":
        get_contact_list(contacts)
        selected_contact_index = input("Digite o número do contato que deseja adicionar/remover dos favoritos: ")
        change_favorite_status(contacts, selected_contact_index)
    elif selected_option == "5":
        get_favorite_contact_list(contacts)
    elif selected_option == "6":
        get_contact_list(contacts)
        selected_contact_index = input("Digite o número do contato que deseja DELETAR: ")
        delete_contact(contacts, selected_contact_index)
    elif selected_option == "7":
        break
    
print("Programa finalizado!")