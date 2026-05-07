# demo.py
from lab4.model3 import Server, DatabaseServer, WebServer
from lab4.collection3 import InterfaceServerCluster
from lab4.interface import IMonitorable, IComparable

print("   === СЦЕНАРИЙ 1 — Интерфейс IMonitorable (Мониторинг) === ")
print("\n")

serv = Server("Proxy-1", priority=3)
db   = DatabaseServer("Main-DB", priority=10, db_type="PostgreSQL", storage_gb=500)
web  = WebServer("Frontend", priority=5, framework="Django", is_https=True)

print(serv.get_metrics())
print(db.get_metrics())
print(web.get_metrics())

print("\nПроверка реализации интерфейса (isinstance):")
print(f"serv это IMonitorable?  {isinstance(serv, IMonitorable)}")
print(f"db это IMonitorable?    {isinstance(db, IMonitorable)}")


print("\n")
print("  === СЦЕНАРИЙ 2 — Интерфейс IComparable (Сравнение) ===")
print("\n")

serv2 = Server("Proxy-2", priority=8)
db2   = DatabaseServer("Log-DB", priority=2, db_type="MongoDB", storage_gb=200)

web.turn_on()             
web.add_connections(100)  

web2  = WebServer("Static", priority=4, framework="React", is_https=False)
web2.turn_on()            
web2.add_connections(50)  

if serv2.compare(serv) > 0:
    print(f"{serv2.name} важнее, чем {serv.name}")
else:
    print(f"{serv.name} важнее, чем {serv2.name}")

if db.compare(db2) > 0:
    print(f"{db.name} больше (ГБ), чем {db2.name}")

if web.compare(web2) > 0:
    print(f"У {web.name} больше подключений, чем у {web2.name}")
print("\n")
print("  === СЦЕНАРИЙ 3 — Универсальная функция ===")
print("\n")
def print_system_status(objects_list):
    for obj in objects_list:
        if isinstance(obj, IMonitorable):
            print(f" -> {obj.get_metrics()}")

mixed_list = [serv, db, web, serv2, db2]
print("Вызов метрик через универсальную функцию:")
print_system_status(mixed_list)


print("\n")
print("  === СЦЕНАРИЙ 4 — Фильтрация коллекции по интерфейсам ===")
print("\n")

cluster = InterfaceServerCluster()
cluster.add(serv)
cluster.add(db)
cluster.add(web)
cluster.add(serv2)

print("Вызов print_all_metrics() из коллекции:")
cluster.print_all_metrics()

monitorables = cluster.get_monitorables()
print(f"\nОбъектов с интерфейсом IMonitorable: {len(monitorables)}")

comparables = cluster.get_comparables()
print(f"Объектов с интерфейсом IComparable: {len(comparables)}")


print("\n")
print("  === СЦЕНАРИЙ 5 — Сортировка через IComparable ===")
print("\n")

sort_cluster = InterfaceServerCluster()
sort_cluster.add(Server("Node-A", priority=9))
sort_cluster.add(Server("Node-B", priority=2))
sort_cluster.add(Server("Node-C", priority=5))
sort_cluster.add(Server("Node-D", priority=1))

print("До сортировки:")
for s in sort_cluster:
    print(f"  {s.name} (Приоритет: {s.priority})")

sort_cluster.sort_by_compare()

print("\nПосле сортировки по приоритету (через compare()):")
for s in sort_cluster:
    print(f"  {s.name} (Приоритет: {s.priority})")