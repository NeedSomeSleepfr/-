from lab3.base import Server

class DatabaseServer(Server):
    def __init__(self, name, priority=1, connections=0, db_type="SQL", storage_gb=100):
        super().__init__(name, priority, connections) 

        self._db_type = db_type
        self._storage_gb = storage_gb

    @property
    def db_type(self):
        return self._db_type

    @property
    def storage_gb(self):
        return self._storage_gb

    def backup_data(self):
        if self._status == "активен":
            return f"{self._name} делает бэкап базы {self._db_type} размером {self._storage_gb} ГБ."
        else:
            raise RuntimeError("Нельзя сделать бэкап: сервер не активен")
        
    def process_task(self):
        return f"{self._name} обрабатывает тяжелые {self._db_type} запросы."

    def get_info(self):
        return f"Сервер БД '{self._name}' | Тип: {self._db_type} | Диск: {self._storage_gb} ГБ"

    def __str__(self):
        return f"DatabaseServer '{self._name}' | Приоритет: {self._priority} | Подключения: {self._connections} | Тип: {self._db_type} | Объем: {self._storage_gb}ГБ | Статус: {self._status}"

class WebServer(Server):
    def __init__(self, name, priority=1, connections=0, framework="Nginx", is_https=True):
        super().__init__(name, priority, connections) 
        self._framework = framework
        self._is_https = is_https

    @property
    def framework(self):
        return self._framework

    def restart_service(self):
        if self._status == "активен":
            self.connections = 0 
            return f"{self._name} перезапускает службу {self._framework}. Все подключения разорваны."
        else:
            raise RuntimeError("Нельзя перезапустить службу: сервер не активен")

    def process_task(self):
        protocol = "HTTPS" if self._is_https else "HTTP"
        return f"{self._name} отдает веб-страницы по {protocol} через {self._framework}."

    def get_info(self):
        return f"Веб-сервер '{self._name}' | Фреймворк: {self._framework} | Защита: {self._is_https}"

    def __str__(self):
        return f"WebServer '{self._name}' | Приоритет: {self._priority} | Подключения: {self._connections} | Фреймворк: {self._framework} | HTTPS: {self._is_https} | Статус: {self._status}"