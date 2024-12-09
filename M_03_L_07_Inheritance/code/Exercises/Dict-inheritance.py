# Наследование от встроенного типа dict.
#
# Создайте класс, который наследует от встроенного типа dict и добавляет дополнительные методы.
# Используйте функцию issubclass() для проверки, является ли созданный класс подклассом dict.
#
# Шаги:
# Создайте класс CustomDict, который наследует от dict.
# Добавьте метод invert, который возвращает новый словарь с инвертированными ключами и значениями.
# Добавьте метод merge, который объединяет текущий словарь с другим словарем.
# Напишите функцию, которая принимает класс и проверяет, является ли он подклассом dict с помощью issubclass().
# Протестируйте функцию и методы CustomDict.

class CustomDict(dict):

    def invert(self):
        return {value: key for key, value in self.items()}

    def merge(self, other_dict):
        merged = self.copy()
        merged.update(other_dict)
        return merged

def is_subclass_dict(cls):
    return issubclass(cls, dict)

if __name__ == "__main__":
    custom_dict = CustomDict(a=1, b=2, c=3)
    inverted_dict = custom_dict.invert()
    merged_dict = custom_dict.merge(other_dict=({"d": 4, "e": 5}))
    print("CustomDict is subclass:", is_subclass_dict(CustomDict))

