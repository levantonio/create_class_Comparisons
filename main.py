from functools import total_ordering

@total_ordering
class Comparisons:
    """
    реализация всех методов сравнения:
    __lt__();__le__();__gt__();__ge__();__eq__()
    """

    def __init__(self, value):
        self.__value = value

    # Оператор ==
    def __eq__(self, other):
        """
        :param other: object class
        :return: ? self.__value1 == other.__value2
        """
        if isinstance(other, Comparisons):
            return self.__value == other.__value
        else:
            raise TypeError("Not a Comparisons object or not integer")

    # Оператор >
    def __gt__(self, other):
        """
        :param other: object class
        :return: ? self.__value > other.__value
        """
        if isinstance(other, (int, Comparisons)):
            return self.__value > other.__value
        else:
            raise TypeError("Not a Comparisons object or not integer")

    # Обнуление
    def zeroing_out(self):
        """
        :return: 0
        """
        self.__value = 0

val1 = Comparisons(500)
val2 = Comparisons(100)

print(val1 > val2)
print(val1 < val2)
print(val1 == val2)
print(val1 != val2)
print(val1 >= val2)
print(val1 <= val2)

val1.zeroing_out()
val2.zeroing_out()
print(val1 == val2)