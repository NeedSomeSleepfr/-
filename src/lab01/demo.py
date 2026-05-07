from model import Server

print("--- СЦЕНАРИЙ 1: Создание объектов и сравнение ---")
s1 = Server("Web-Server", priority=5, connections=0)
s2 = Server("Web-Server", priority=5, connections=100)
s3 = Server("DB-Server", priority=10, connections=0)

print(s1)
print(repr(s1))

print(f"\nРавны ли s1 и s2? {s1 == s2}")
print(f"Равны ли s1 и s3? {s1 == s3}")

print(f"\nАтрибут класса (Макс. подключений): {Server.MAX_CONNECTIONS}")
print(f"Доступ через объект: {s1.MAX_CONNECTIONS}")


print("\n--- СЦЕНАРИЙ 2: Работа с подключениями и состояниями ---")
serv = Server("Mail-Server", priority=2)
print(serv)

print(serv.turn_on())
print(serv.add_connections(50))
print(serv.add_connections(200))

serv.connections = 500
print(f"После ручного изменения (setter): {serv}")


print("\n--- СЦЕНАРИЙ 3: Падение сервера (изменение поведения) ---")
main_server = Server("API-Server", priority=8)
main_server.turn_on()
main_server.add_connections(1000)
print(main_server)

print(main_server.crash())
print(f"Текущий статус: {main_server.status}")
print(f"Текущие подключения: {main_server.connections}")

try:
    main_server.add_connections(10)
except RuntimeError as e:
    print(f"[Блокировка] {e}")


print("\n--- СЦЕНАРИЙ 4: Ошибки создания (Валидация) ---")
try:
    Server("")
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    Server("Test", priority=99)
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    Server("Test", priority="высокий")
except TypeError as e:
    print(f"Ошибка: {e}")

try:
    Server("Test", connections=-50)
except ValueError as e:
    print(f"Ошибка: {e}")


print("\n--- СЦЕНАРИЙ 5: Ошибка setter-а ---")
test_serv = Server("Test-2")
test_serv.turn_on()
try:
    test_serv.connections = -10
except ValueError as e:
    print(f"Setter отклонил значение: {e}")