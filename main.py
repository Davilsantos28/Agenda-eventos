from eventos import Evento
from agendaeventos import AgendaEventos

def show_menu():
    print("1. Adicionar evento")
    print("2. Listar todos os eventos")
    print("3. Editar um evento")
    print("4. Remover um evento")
    print("5. Sair")

def main():
    agenda = AgendaEventos()


    while True:
        show_menu()
        choice = int(input("Entre com a sua escolha: "))
        if choice == 1:
            titulo = input("Título: ")
            data = input("Data (YYYY-MM-DD): ")
            hora = input("Hora: ")
            local = input("Local: ")
            event = Evento(titulo, data, hora, local)
            agenda.add_event(event)
        elif choice == 2:
            agenda.list_events()
        elif choice == 3:
            event_index = int(input("Índice do evento a ser editado: "))
            event_index -= 1
            titulo = input("Título: ")
            data = input("Data (YYYY-MM-DD): ")
            hora = input("Hora: ")
            local = input("Local: ")
            event = Evento(titulo, data, hora, local)
            agenda.edit_event(event_index, event)
        elif choice == 4:
            event_index = int(input("Índice do evento a ser removido: "))
            event_index -= 1
            agenda.remove_event(event_index)
        elif choice == 5:
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()