"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
Пример работы программ:
"""

import timeit
import cProfile


def sieve(n):
    size = n * 100
    sieve = [i for i in range(size)]
    sieve[1] = 0

    for i in range(2, size):
        if sieve[i] != 0:
            j = i ** 2
            while j < size:
                sieve[j] = 0
                j += i

    prime = [i for i in sieve if i != 0]
    return prime[n - 1]

print(sieve(333))

# print(timeit.timeit('sieve(10)', number=1000, globals=globals()))    # 0.2332452
# print(timeit.timeit('sieve(20)', number=1000, globals=globals()))    # 0.4886997
# print(timeit.timeit('sieve(40)', number=1000, globals=globals()))    # 1.0005235
# print(timeit.timeit('sieve(80)', number=1000, globals=globals()))    # 2.0277527
# print(timeit.timeit('sieve(160)', number=1000, globals=globals()))   # 4.4422698
# print(timeit.timeit('sieve(320)', number=1000, globals=globals()))   # 9.007475399999999
# print(timeit.timeit('sieve(640)', number=1000, globals=globals()))   # 18.8845668

# Линейная сложность O(n)

# cProfile.run('sieve(10)')
#          6 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task2.py:19(sieve)
#         1    0.000    0.000    0.000    0.000 task2.py:21(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task2.py:31(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def prime(n):
    step = 1
    prime_number = 2
    while step != n:
        prime_number += 1
        for i in range(2, prime_number):
            if prime_number % i == 0:
                break
        else:
            step += 1
    return prime_number


print(prime(333))

# print(timeit.timeit('prime(10)', number=1000, globals=globals()))    # 0.012624900000000001
# print(timeit.timeit('prime(20)', number=1000, globals=globals()))    # 0.0449331
# print(timeit.timeit('prime(40)', number=1000, globals=globals()))    # 0.1786915
# print(timeit.timeit('prime(80)', number=1000, globals=globals()))    # 0.7755918
# print(timeit.timeit('prime(160)', number=1000, globals=globals()))   # 3.8981888
# print(timeit.timeit('prime(320)', number=1000, globals=globals()))   # 18.0289719
# print(timeit.timeit('prime(640)', number=1000, globals=globals()))   # 85.5792453
# Сложность O(2**n)

# cProfile.run('prime(10)')
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task2.py:55(prime)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


######################## Вывод #########################
# Несмотря на то, что второй вариант алгоритма поиска простых чисел работает быстрее для маленьких чисел,
# вариант без решета Эратосфена значительно проигрывает по времени при подсчете больших чисел.


