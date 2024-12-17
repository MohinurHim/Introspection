# Домашнее задание по теме "Интроспекция"
import inspect

def introspection_info(obj):
    info = {}
    # Тип объекта
    info['Type'] = type(obj).__name__
    # Атрибуты объекта
    info['Attributs'] = [attribut for attribut in dir(obj) if not callable(getattr(obj, attribut))]
    #  Методы объекта
    info['Methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    # Модуль, к которому объект принадлежит
    info['Module'] = inspect.getmodule(obj)
    # Другие интересные свойства объекта, учитывая его тип
    if isinstance(obj, (int, float)):
        info['Value'] = obj
    return info

number_info = introspection_info(42)
print(number_info)
