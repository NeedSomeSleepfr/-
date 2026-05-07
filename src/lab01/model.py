from lab1.validate import validate_name, validate_priority, validate_connections

class Server:
    MAX_CONNECTIONS = 5000  

    def __init__(self, name, priority=1, connections=0):
        validate_name(name)
        validate_priority(priority)
        validate_connections(connections)

        self._name = name
        self._priority = priority
        self._connections = connections
        self._status = "выключен"  # Состояние по умолчанию (apagado)

    @property
    def name(self):
        return self._name

    @property
    def priority(self):
        return self._priority

    @property
    def connections(self):
        return self._connections

    @property
    def status(self):
        return self._status
    
    @connections.setter
    def connections(self, value):
        validate_connections(value)
        if self._status != "активен":
            raise RuntimeError("Нельзя менять подключения: сервер не активен")

        if value > Server.MAX_CONNECTIONS:
            self._connections = Server.MAX_CONNECTIONS
        else:
            self._connections = value

    def turn_on(self):
        if self._status == "выключен":
            self._status = "активен"
            return f"Сервер {self._name} успешно запущен."
        else:
            raise RuntimeError("Сервер уже работает или находится в состоянии ошибки")

    def crash(self):
        self._status = "ошибка"
        self._connections = 0
        return f"КРИТИЧЕСКАЯ ОШИБКА! Сервер {self._name} упал."

    def add_connections(self, count):
        if self._status == "активен":
            if count < 0:
                raise ValueError("Количество новых подключений должно быть больше нуля")

            self.connections = self._connections + count 
            return f"Добавлено {count} подключений. Всего: {self._connections}"
        else:
            raise RuntimeError(f"Невозможно подключиться. Статус сервера: '{self._status}'")

    def __str__(self):
        return f"Сервер '{self._name}' | Приоритет: {self._priority} | Подключения: {self._connections} | Статус: {self._status}"

    def __repr__(self):
        return f"Server(name='{self._name}', priority={self._priority}, connections={self._connections})"

    def __eq__(self, other):
        if type(other) == Server:
            return self._name == other._name and self._priority == other._priority
        else:
            return False