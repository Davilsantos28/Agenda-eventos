from eventos import Evento

class AgendaEventos:
    def __init__(self):
        self.eventos = []

    def add_event(self, event):
        self.eventos.append(event)

    def edit_event(self, event_index, event):
        if 0 <= event_index < len(self.eventos):
            self.eventos[event_index] = event
        else:
            raise IndexError("Invalid event index")

    def remove_event(self, event_index):
        if 0 <= event_index < len(self.eventos):
            self.eventos.pop(event_index)
        else:
            raise IndexError("Invalid event index")

    def list_events(self):
        for i, event in enumerate(self.eventos):
            print(f"{i + 1}. {event}")
