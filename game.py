import numpy as np

upper_bound = int(input("Введите верхнюю границу: "))
times_run = int(input("Введите количество запусков: "))

print(f"Компьютер загадал целое число от 1 до {upper_bound}")


def score_game(game_core):
    """Запускаем игру {times_run} раз, чтобы узнать за какое количество попыток
    алгоритм угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED для воспроизводимости
    random_array = np.random.randint(1, upper_bound + 1, size=times_run)
    for number in random_array:
        count_ls.append(game_core(number))
    score = np.mean(count_ls)
    print(f"Алгоритм находит загаданное число в среднем за {score} попыток")
    return score


def game_core_v3(number):
    """Сначала устанавливаем половину от верхней границы, а потом уменьшаем \
    или увеличиваем шаг в зависимости от того, больше это число или меньше \
    нужного. Функция принимает загаданное число и возвращает число попыток"""
    count = 1
    predict = upper_bound // 2  # половина от верней границы
    while number != predict:
        count += 1

        """шаг поиска - верхняя граница поделённая на 2 в степени количество \
        попыток минус 1"""
        step = round(upper_bound / (2 ** (count - 1)))

        if number > predict:
            predict += step
        elif number < predict:
            predict -= step
    return count  # выход из цикла, если число угадано


score_game(game_core_v3)
