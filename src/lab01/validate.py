def validate_name(name):
    if type(name) == str:
        if name.strip() != "":
            pass
        else:
            raise ValueError("Имя сервера не может быть пустым")
    else:
        raise TypeError("Имя должно быть строкой")

def validate_priority(priority):
    if type(priority) == int:
        if 1 <= priority <= 10:
            pass
        else:
            raise ValueError("Приоритет должен быть от 1 до 10")
    else:
        raise TypeError("Приоритет должен быть целым числом")

def validate_connections(connections):
    if type(connections) == int:
        if connections >= 0:
            pass
        else:
            raise ValueError("Количество подключений не может быть отрицательным")
    else:
        raise TypeError("Подключения должны быть целым числом")