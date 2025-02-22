# Создайте класс TrackedDict, который наследует от встроенного типа dict и добавляет новые методы
# для отслеживания изменений в словаре. Используйте private и protected атрибуты для хранения состояния и
# добавьте методы для работы с этими атрибутами. Также проверьте, является ли TrackedDict подклассом dict с
# помощью функции issubclass() и используйте super() для вызова методов суперкласса.
#
# Шаги:
# Создайте класс TrackedDict, который наследует от dict.
# Добавьте private атрибут для хранения количества изменений (добавление/удаление элементов).
# Добавьте protected атрибут для хранения разрешенного количества изменений.
# Переопределите методы __setitem__ и __delitem__, чтобы увеличивать счетчик изменений и проверять его значение.
# Напишите методы для получения значений private и protected атрибутов.
# Проверьте, является ли TrackedDict подклассом dict с помощью функции issubclass().
