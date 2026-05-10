def by_name(server):
    return server.name

def by_priority(server):
    return server.priority

def by_connections(server):
    return server.connections

def is_active(server):
    return server.status == "активен"

def is_database(server):
    from lab3.model2 import DatabaseServer 
    return isinstance(server, DatabaseServer)

def make_priority_filter(min_priority):

    def filter_fn(server):
        return server.priority >= min_priority
    return filter_fn

class AddLoadStrategy:
    def __init__(self, connections_to_add):
        self.connections_to_add = connections_to_add

    def __call__(self, server):
        if server.status == "активен":
            server.add_connections(self.connections_to_add)

class RestartStrategy:
    def __call__(self, server):
        from lab3.model2 import WebServer
        if isinstance(server, WebServer) and server.status == "активен":
            server.restart_service()
        else:
            server.connections = 0