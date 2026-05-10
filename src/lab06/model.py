from lab1.model import Server as BaseServer
from lab3.model2 import DatabaseServer as BaseDB
from lab3.model2 import WebServer as BaseWeb

class Server(BaseServer):
    def __init__(self, name: str, priority: int = 1, connections: int = 0) -> None:
        super().__init__(name, priority, connections)
        self._name: str = name
        self._priority: int = priority
        self._connections: int = connections

    def show(self) -> str:
        return f"[Базовый Сервер] {self._name} | Приоритет: {self._priority}"

    def get_score(self) -> float:
        return float(self._priority * 10.0)


class DatabaseServer(BaseDB):
    def __init__(self, name: str, priority: int = 1, db_type: str = "SQL", storage_gb: int = 100) -> None:
        super().__init__(name, priority, 0, db_type, storage_gb)
        self._db_type: str = db_type
        self._storage_gb: int = storage_gb

    def show(self) -> str:
        return f"[Сервер БД] {self._name} ({self._db_type}) | Память: {self._storage_gb} ГБ"

    def get_score(self) -> float:
        return float(self._storage_gb * 1.5)


class WebServer(BaseWeb):
    def __init__(self, name: str, priority: int = 1, framework: str = "Nginx", is_https: bool = True) -> None:
        # ВАЖНОЕ ИСПРАВЛЕНИЕ: передаем 0 в качестве параметра connections
        super().__init__(name, priority, 0, framework, is_https)
        self._framework: str = framework
        self._is_https: bool = is_https

    def show(self) -> str:
        return f"[Веб-Сервер] {self._name} | Фреймворк: {self._framework}"

    def get_score(self) -> float:
        bonus: float = 50.0 if self._is_https else 0.0
        return float(self._priority * 5.0 + bonus)