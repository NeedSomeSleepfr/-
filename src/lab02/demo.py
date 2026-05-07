from lab1.model import Server
from lab2.collection import ServerCluster

print("=== СЦЕНАРИЙ 1: Добавление и ошибки ===")

cluster = ServerCluster()

serv1 = Server("Web-Main", priority=10)
serv2 = Server("DB-Primary", priority=9)
serv3 = Server("Cache-1", priority=5)

cluster.add(serv1)
cluster.add(serv2)
cluster.add(serv3)

print("Все серверы в кластере:")
print(cluster)

print("Пробуем добавить сервер с таким же именем:")
try:
    cluster.add(Server("Web-Main", priority=2))
except ValueError as error:
    print(f"Ошибка: {error}")

print("\nПробуем добавить не сервер:")
try:
    cluster.add("Просто строка")
except TypeError as error:
    print(f"Ошибка: {error}")


print("\n=== СЦЕНАРИЙ 2: Итерация, размер и поиск ===")
print(f"Размер кластера (len): {len(cluster)}")

print("\nПеребор через for:")
for s in cluster:
    print(f" -> Имя: {s.name}, Приоритет: {s.priority}")

print("\nПоиск сервера 'Cache-1':")
found = cluster.find_by_name("Cache-1")
print(found)


print("\n=== СЦЕНАРИЙ 3: Работа с индексами и удаление ===")
print(f"Сервер под индексом 1: {cluster[1]}")

print("\nУдаляем сервер по индексу 1...")
deleted = cluster.remove_at(1)
print(f"Был удален: {deleted.name}")

print("\nКластер после удаления:")
print(cluster)

try:
    cluster.remove_at(100)
except IndexError as error:
    print(f"Ошибка удаления: {error}")


print("\n=== СЦЕНАРИЙ 4: Фильтрация (Новые кластеры) ===")
test_cluster = ServerCluster()

s_active1 = Server("App-1", priority=5)
s_active1.turn_on()
s_active1.add_connections(100)

s_active2 = Server("App-2", priority=8)
s_active2.turn_on()

s_crashed = Server("Old-DB", priority=3)
s_crashed.turn_on()
s_crashed.crash()

test_cluster.add(s_active1)
test_cluster.add(s_active2)
test_cluster.add(s_crashed)

active_only = test_cluster.get_active_servers()
print(f"Только активные серверы ({len(active_only)} шт.):")
for s in active_only:
    print(f"- {s.name} (Статус: {s.status})")

crashed_only = test_cluster.get_crashed_servers()
print(f"\nУпавшие серверы ({len(crashed_only)} шт.):")
for s in crashed_only:
    print(f"- {s.name} (Статус: {s.status})")


print("\n=== СЦЕНАРИЙ 5: Сортировка ===")
sort_cluster = ServerCluster()
sort_cluster.add(Server("Node-A", priority=4))
sort_cluster.add(Server("Node-B", priority=1))
sort_cluster.add(Server("Node-C", priority=9))

print("До сортировки по приоритету:")
for s in sort_cluster:
    print(f"{s.name} - {s.priority}")

sort_cluster.sort_by_priority()

print("\nПосле сортировки по приоритету:")
for s in sort_cluster:
    print(f"{s.name} - {s.priority}")