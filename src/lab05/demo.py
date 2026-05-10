from lab3.base import Server
from lab3.model2 import DatabaseServer, WebServer
from lab5.Collection4 import FunctionalServerCluster
import lab5.Strategie as strat
print("\n")
print("  === СЦЕНАРИЙ 1 — Базовая сортировка и фильтрация (Встроенные) ===")
print("\n")

servers_list = [
    Server("Proxy-A", priority=5, connections=10),
    DatabaseServer("DB-Main", priority=10, db_type="SQL", storage_gb=500),
    WebServer("Front-1", priority=8, framework="React"),
    Server("Proxy-B", priority=2, connections=50),
    WebServer("Front-2", priority=4, framework="Vue")
]

for s in servers_list:
    if s.name != "Proxy-B": # Один оставим выключенным для тестов
        s.turn_on()

print("Сортировка по имени (sorted + by_name):")
for s in sorted(servers_list, key=strat.by_name):
    print(f"  - {s.name}")

print("\nСортировка по приоритету (sorted + by_priority):")
for s in sorted(servers_list, key=strat.by_priority):
    print(f"  - {s.name} (Приоритет: {s.priority})")

print("\nФильтрация только активных (filter + is_active):")
active_only = list(filter(strat.is_active, servers_list))
for s in active_only:
    print(f"  - {s.name} (Статус: {s.status})")


print("\n")
print("  === СЦЕНАРИЙ 2 — Использование map() и Фабрики функций ===")
print("\n")

names_only = list(map(lambda s: s.name, servers_list))
print(f"Имена серверов (через map): {names_only}")

high_priority_filter = strat.make_priority_filter(7)
important_servers = list(filter(high_priority_filter, servers_list))

print("\nСерверы с приоритетом >= 7 (через Фабрику функций):")
for s in important_servers:
    print(f"  - {s.name} (Приоритет: {s.priority})")

print("\n")
print(" === СЦЕНАРИЙ 3 — Методы коллекции и использование lambda ===")
print("\n")

cluster = FunctionalServerCluster()
for s in servers_list:
    cluster.add(s)

print("Сортировка кластера по подключениям (через lambda):")
sorted_cluster = cluster.sort_by(lambda s: s.connections)
print(sorted_cluster)

print("\n")
print("  === СЦЕНАРИЙ 4 — Паттерн Стратегия (Callable-объекты) ")
print("\n")

print("Состояние Front-1 ДО стратегии:")
print(cluster.filter_by(lambda s: s.name == "Front-1"))

add_150_load = strat.AddLoadStrategy(150)

cluster.apply(add_150_load)

print("\nСостояние Front-1 ПОСЛЕ применения стратегии нагрузки:")
print(cluster.filter_by(lambda s: s.name == "Front-1"))


print("\n")
print("  ==== СЦЕНАРИЙ 5 — Цепочка вызовов (Method Chaining) ===")
print("\n")
print("Цепочка: Взять базы данных -> Отсортировать по имени -> Применить перезагрузку")

restart_strat = strat.RestartStrategy()

final_result = (cluster
    .filter_by(strat.is_database)   # 1. Оставляем только БД
    .sort_by(strat.by_name)         # 2. Сортируем их
    .apply(restart_strat)           # 3. Перезагружаем (сброс подключений)
)

print(final_result)