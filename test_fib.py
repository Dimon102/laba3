
import main
import pytest

# Тест функции, которая выводит первые "n" чисел Фибоначчи
class TestFib:

    # Тестируем программу на коррктных данных. Функция возвращает список элементов.
    def test_on_positive(self):
        assert main.fib(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    # Тестируем программу на некоррктных данных. Функция возвращает список элементов.
    def test_on_negative(self):
        assert main.fib(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    # Тестируем программу на некорретных данных. Функция вызывает исключение IndexError.
    def test_on_negative1(self):
        with pytest.raises(IndexError):
            main.fib(-10)