from lab2.collection import ServerCluster as BaseCluster
from lab3.model2 import DatabaseServer, WebServer
from lab3.base import Server

class ExtendedServerCluster(BaseCluster):

    def add(self, server):
        if isinstance(server, Server):
            for s in self._servers:
                if s.name == server.name:
                    raise ValueError(f"Сервер с именем '{server.name}' уже существует!")
            self._servers.append(server)
        else:
            raise TypeError("Можно добавлять только объекты Server и его дочерние классы")

    def get_only_databases(self):
        result = ExtendedServerCluster()
        for s in self._servers:
            if isinstance(s, DatabaseServer):
                result.add(s)
        return result

    def get_only_web_servers(self):
        result = ExtendedServerCluster()
        for s in self._servers:
            if isinstance(s, WebServer):
                result.add(s)
        return result

    def get_only_base_servers(self):
        result = ExtendedServerCluster()
        for s in self._servers:
            if type(s) == Server:
                result.add(s)
        return result