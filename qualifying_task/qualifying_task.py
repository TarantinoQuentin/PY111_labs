# 1.	Оценить асимптотическую сложность приведенного ниже алгоритма:
# a = len(arr) – 1  # O(1)
# out = list()  # # O(1)
# while a > 0:  # O(log_1.7 (n)) — (m)
#     out.append(arr[a])  # O(1)
#     a = a // 1.7
# out.merge_sort()  # O(log (m))

"""
O(log_1.7 (n) * log (m)) -> O(log (n) * log (log (n)))

Ответ: O(log (n) * log (log (n)))
"""

# 5.	Задача консенсуса DNA ридов
# При чтении DNA последовательностей могут возникать единичные ошибки, выражающиеся в неверной букве в строке.
# Для решения данной проблемы требуемое место читается несколько раз, после чего строится консенсус-строка,
# в которой на каждом месте будет стоять тот символ, что чаще всего встречался в этом месте суммарно
# во всех чтениях. Т.е. для строк
# ATTA
# ACTA
# AGCA
# ACAA
# консенсус-строка будет ACTA (в первой ячейке чаще всего встречалась A,
# во второй – C, в третьей – Т, в четвертой – снова А).
# Для входного списка из N строк одинаковой длины построить консенсус-строку.

# Решение:

from collections import Counter


def get_consensus_dna(strs: list[str]) -> str:
    """
    Функция, читающая последовательность строк strs и возвращающая консенсус-строку,
    где на каждом месте будет стоять тот символ, что чаще всего
    встречался в этом месте суммарно во всех чтениях.

    :param strs: DNA последовательности.
    :return: Консенсус-строка.
    """

    result_string = []

    for i, chars in enumerate(zip(*strs)):

        if len(set(chars)) == 1:
            result_string += chars[0]
        else:
            result_string += Counter(chars).most_common(1)[0][0]

    return ''.join(result_string)


print(get_consensus_dna(['ATTA', 'ACTA', 'AGCA', 'ACAA']))  # ACTA

# 7.	Сорт
# Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
# Задача: отсортировать массив наиболее эффективным способом

# Решение:

from random import randint


nums = [randint(13, 25) for num in range(10 ** 6)]


def counting_sort(nums: list[int]) -> list[int]:
    """
    Сортировка подсчетом, считает количество встретившихся одинаковых
    элементов, далее восстанавливает массив в правильно порядке.

    :param nums: Неотсортированный массив.
    :return: Отсортированный массив.
    """

    if not nums:
        return nums

    first_element = min(nums)
    last_element = max(nums)
    counted_nums = {number: 0 for number in range(first_element, last_element + 1)}

    for num in nums:
        counted_nums[num] += 1

    result = []
    for num in counted_nums:
        result.extend([num] * counted_nums[num])

    return result

# print(counting_sort(nums))

# 6.	Аренда ракет
# Вы – компания, дающая в аренду ракеты. Каждый день к вам приходит список заявок на использование ракет
# в виде: (час_начала, час_конца), (час_начала, час_конца), ...
# Если аренда ракеты заканчивается в час X, то в этот же час ее уже можно взять в аренду
# снова (т.е. час_начала может начинаться с Х).
# Дано: список заявок на использование ракет
# Задача: вывести ответ, хватит ли вам одной ракеты, чтобы удовлетворить все заявки на этот день

# Решение:

def missile_rent(time_list: list[tuple]) -> bool:
    """
    Функция для определения перекрытий по времени заявок
    на аренду ракеты, если одной ракеты хватит на
    удовлетворение всех заявок в течение дня, возвращает
    True.

    :param time_list: Список кортежей из двух значений,
    времени начала аренды и времени ее окончания.
    :return: bool
    """

    if not time_list:
        return True

    start_hours_list, _ = zip(*time_list)
    if len(start_hours_list) > len(set(start_hours_list)):
        return False

    time_dict = dict(time_list)

    finish_hour = -1
    for start_hour in range(25):
       if start_hour in time_dict:
           if start_hour < finish_hour:
               return  False
           finish_hour = time_dict[start_hour]

    return True


print(missile_rent([(1, 2), (2, 4), (4, 5), (5, 9)]))  # True
print(missile_rent([(1, 3), (2, 4), (4, 5), (5, 9)]))  # False
