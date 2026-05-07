from lab3.base import Server as BaseServer
from lab3.model2 import DatabaseServer as BaseDB
from lab3.model2 import WebServer as BaseWeb

from lab4.interface import IMonitorable, IComparable

class Server(BaseServer, IMonitorable, IComparable):
    def get_metrics(self):
        return f"[Базовые метрики] {self._name} | Приоритет: {self._priority} | Подключения: {self._connections}"

    def compare(self, other):
        return self._priority - other.priority

class DatabaseServer(BaseDB, IMonitorable, IComparable):
    def get_metrics(self):
        return f"[Метрики БД] {self._name} ({self._db_type}) | Диск занят: {self._storage_gb} ГБ"

    def compare(self, other):
        return self._storage_gb - other.storage_gb

class WebServer(BaseWeb, IMonitorable, IComparable):
    def get_metrics(self):
        return f"[Метрики Веб] {self._name} ({self._framework}) | Защита HTTPS: {self._is_https}"

    def compare(self, other):
        return self._connections - other.connections