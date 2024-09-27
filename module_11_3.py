def introspection(obj):
    # Определение типа объекта
    obj_type = type(obj).__name__

    # Получение атрибутов объекта
    attributes = [attribute for attribute in dir(obj)
                  if not callable(getattr(obj, attribute))]

    # Получение методов объекта
    methods = [method for method in attributes if callable(getattr(obj, method))]

    # Определение модуля, к которому объект принадлежит
    module = obj.__class__.__module__

    # Другие интересные свойства объекта (в данном примере не добавлены)
    # other_properties = {}

    # Создание словаря с информацией об объекте
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module},
            # 'other_properties': other_properties}

    return info

# Интроспекция числа
number_info = introspection(42)
print(number_info)

# Интроспекция строки
string_info = introspection('Hello, World!')
print(string_info)

# Интроспекция списка
list_info = introspection(['1', 2, 3, 4.0])
print(list_info)
