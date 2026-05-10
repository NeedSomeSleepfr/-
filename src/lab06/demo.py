from lab6.model4 import Server, DatabaseServer, WebServer
from lab6.container import TypedCollection, Displayable, Scorable

print("\n")
print("  === СЦЕНАРИЙ 1 — Базовая типизированная коллекция === ")
print("\n")

коллекция: TypedCollection[Server] = TypedCollection()

коллекция.add(Server("Proxy-1", priority=5))
коллекция.add(Server("Proxy-2", priority=8))
коллекция.add(DatabaseServer("Main-DB", priority=10, storage_gb=500))
коллекция.add(WebServer("Front-1", priority=7, framework="React"))

print(коллекция)

все_серверы = коллекция.get_all()
print(f"Всего серверов получено через get_all(): {len(все_серверы)}")


print("\n")
print("  ==== СЦЕНАРИЙ 2 — find(), filter() и map()=== ")
print("\n")

найден = коллекция.find(lambda s: s.priority >= 8)
print(f"find(приоритет >= 8): {найден.name if найден else None}")

не_найден = коллекция.find(lambda s: s.priority == 99)
print(f"find(приоритет == 99): {не_найден}")

высокий_приоритет = коллекция.filter(lambda s: s.priority >= 7)
print(f"\nfilter(приоритет >= 7) — {len(высокий_приоритет)} серверов:")
for s in высокий_приоритет:
    print(f"  {s.name} | приоритет {s.priority}")

имена = коллекция.map(lambda s: s.name)
print(f"\nmap -> список имён (list[str]): {имена}")

приоритеты = коллекция.map(lambda s: s.priority)
print(f"map -> список приоритетов (list[int]): {приоритеты}")

print("\n")
print("   =====СЦЕНАРИЙ 3 — Protocol Displayable ===")
print("\n")

s1 = Server("Node-A", priority=3)
db1 = DatabaseServer("Data-Lake", storage_gb=1000)
web1 = WebServer("API-Gate", framework="Django")

print("Вызов show() для каждого типа напрямую:")
print(s1.show())
print(db1.show())
print(web1.show())

коллекция_d: TypedCollection[Displayable] = TypedCollection()
коллекция_d.add(s1)
коллекция_d.add(db1)
коллекция_d.add(web1)

print("\nКоллекция Displayable — вызов show() для всех в цикле:")
for obj in коллекция_d:
    print(f"  {obj.show()}")

тексты = коллекция_d.map(lambda obj: obj.show())
print("\nmap(show) возвращает list[str]:")
for t in тексты:
    print(f"  {t}")


print("\n")
print(" === СЦЕНАРИЙ 4 — Protocol Scorable ===" )
print("\n")

коллекция_s: TypedCollection[Scorable] = TypedCollection()
коллекция_s.add(Server("Backup-Node", priority=2))
коллекция_s.add(DatabaseServer("Archive-DB", storage_gb=200))
коллекция_s.add(WebServer("Static-Web", priority=5))

print("get_score() каждого объекта:")
for obj in коллекция_s:
    print(f"  Очки = {obj.get_score()}")

очки_список = коллекция_s.map(lambda obj: obj.get_score())
print(f"\nmap(get_score) возвращает list[float]: {очки_список}")

лучший = коллекция_s.find(lambda obj: obj.get_score() == max(очки_список))
if лучший:
    print(f"\nЛучший результат в коллекции имеет счет: {лучший.get_score()}")

мощные = коллекция_s.filter(lambda obj: obj.get_score() >= 100)
print(f"\nfilter(score >= 100) — найдено {len(мощные)}:")
for obj in мощные:
    print(f"  Очки = {obj.get_score()}")