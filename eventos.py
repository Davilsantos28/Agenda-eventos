from datetime import datetime

class Evento:
    def __init__(self, titulo, data, hora, local):
        self.titulo = titulo
        self.data = datetime.strptime(data, '%Y-%m-%d')
        self.hora = hora
        self.local = local

    def __str__(self):
        return f"{self.titulo} - {self.data.strftime('%d/%m/%Y')} às {self.hora} - {self.local}"
