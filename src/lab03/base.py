from lab1.model import Server
def get_info(self):
    return f"Базовый сервер '{self._name}'"

Server.get_info = get_info

def process_task(self):
    return f"{self._name} выполняет базовую системную задачу"

Server.process_task = process_task