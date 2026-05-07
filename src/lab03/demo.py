from lab3.base import Server
from lab3.model2 import DatabaseServer, WebServer
from lab3.collection2 import ExtendedServerCluster
print("\n")
print("  === СЦЕНАРИЙ 1 — Создание серверов разных типов ===")
print("\n")
serv_base = Server("Proxy-1", priority=3)
serv_base.turn_on()

db1 = DatabaseServer("Main-DB", priority=10, db_type="PostgreSQL", storage_gb=500)
db1.turn_on()

db2 = DatabaseServer("Log-DB", priority=2, db_type="MongoDB", storage_gb=2000)
db2.turn_on()

web1 = WebServer("Frontend-1", priority=5, framework="Django", is_https=True)
web1.turn_on()

web2 = WebServer("Static-File", priority=4, framework="Apache", is_https=False)
web2.turn_on()

print(serv_base)
print(db1)
print(web1)

print("\n-- get_info() каждого сервера --")
print(serv_base.get_info())
print(db1.get_info())
print(web1.get_info())

print("\n-- Проверка через isinstance() --")
print(f"db1 это Server?         {isinstance(db1, Server)}")
print(f"db1 это DatabaseServer? {isinstance(db1, DatabaseServer)}")
print(f"web1 это DatabaseServer? {isinstance(web1, DatabaseServer)}")

print("\n")
print("  === СЦЕНАРИЙ 2 — Уникальные методы классов ===" )
print("\n")

print("-- База данных --")
print(db2)
print(db2.backup_data())

print("\n-- Веб-сервер --")
web2.add_connections(50)
print(web2)
print(web2.restart_service())
print(f"Подключения после рестарта: {web2.connections}")

print("\n")
print(" === СЦЕНАРИЙ 3 — Коллекция и полиморфизм без условий ===")
print("\n")

cluster = ExtendedServerCluster()
cluster.add(serv_base)
cluster.add(db1)
cluster.add(db2)
cluster.add(web1)
cluster.add(web2)

print(cluster)

print("-- Вызов process_task() для всех (без if/else) --")
for s in cluster:
    print(f"  {s.process_task()}")

print("\n")
print("  === СЦЕНАРИЙ 4 — Состояния и ошибки ===")
print("\n")

broken_db = DatabaseServer("Old-SQL", priority=1, db_type="MySQL", storage_gb=50)
broken_db.turn_on()
print(broken_db)

broken_db.crash()
print(f"Статус: {broken_db.status}")

try:
    broken_db.backup_data()
except RuntimeError as e:
    print(f"[Блокировка] {e}")

print("\n")
print("  === СЦЕНАРИЙ 5 — Фильтрация по типам ===")
print("\n")

only_db = cluster.get_only_databases()
print(f"Только базы данных ({len(only_db)} шт.):")
print(only_db)

only_web = cluster.get_only_web_servers()
print(f"Только веб-серверы ({len(only_web)} шт.):")
print(only_web)

only_base = cluster.get_only_base_servers()
print(f"Только базовые серверы ({len(only_base)} шт.):")
print(only_base)