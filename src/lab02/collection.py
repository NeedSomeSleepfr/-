from lab1.model import Server
from lab1.validate import validate_name, validate_priority, validate_connections

class ServerCluster:
    def __init__(self):
        self._servers = []

    def add(self, server):
        if type(server) == Server:
            for s in self._servers:
                if s.name == server.name:
                    raise ValueError(f"Сервер с именем '{server.name}' уже существует в кластере!")
 
            self._servers.append(server)
        else:
            raise TypeError("В кластер можно добавлять только объекты класса Server")

    def remove(self, server):
        if server in self._servers:
            self._servers.remove(server)
        else:
            raise ValueError(f"Сервер '{server.name}' не найден в кластере")

    def get_all(self):
        return self._servers
    
    def find_by_name(self, target_name):
        for s in self._servers:
            if s.name == target_name:
                return s
        return None  

    def __len__(self):
        return len(self._servers)

    def __iter__(self):
        return iter(self._servers)

    def __getitem__(self, index):
        return self._servers[index]

    def remove_at(self, index):
        if index >= 0 and index < len(self._servers):
            removed_server = self._servers[index]
            self._servers.pop(index)
            return removed_server
        else:
            raise IndexError("Неверный индекс! Такого сервера нет.")

    def get_active_servers(self):
        result = ServerCluster()
        for s in self._servers:
            if s.status == "активен":
                result.add(s)
        return result

    def get_crashed_servers(self):
        result = ServerCluster()
        for s in self._servers:
            if s.status == "ошибка":
                result.add(s)
        return result

    def get_high_priority(self, min_priority):
        result = ServerCluster()
        for s in self._servers:
            if s.priority >= min_priority:
                result.add(s)
        return result
    
    def sort_by_priority(self):
        count = len(self._servers)
        for i in range(count):
            for j in range(0, count - i - 1):
                if self._servers[j].priority > self._servers[j + 1].priority:
                    temp = self._servers[j]
                    self._servers[j] = self._servers[j + 1]
                    self._servers[j + 1] = temp

    def sort_by_connections(self):
        count = len(self._servers)
        for i in range(count):
            for j in range(0, count - i - 1):
                if self._servers[j].connections > self._servers[j + 1].connections:
                    temp = self._servers[j]
                    self._servers[j] = self._servers[j + 1]
                    self._servers[j + 1] = temp

    def __str__(self):
        if len(self._servers) == 0:
            return "Кластер пуст."
        else:
            text = f"--- Кластер серверов ({len(self._servers)} шт.) ---\n"
            for i in range(len(self._servers)):
                text += f"[{i}] {self._servers[i].name} (Приоритет: {self._servers[i].priority})\n"
            return text