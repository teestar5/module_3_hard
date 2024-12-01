# Создаём функцию подсчёта данных строк и чисел
def calculate_structure_sum(data_structure):
    summa = 0
    # Прописываем условие при помощи цикла 1 summa для key и value
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)
            # иначе выполняется цикл 2 add к summa - список,кортеж,множества
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            summa += calculate_structure_sum(item)
            # иначе выполняется действие 3 add к summa - целое число и число с плавающей запятой
    elif isinstance(data_structure, (int, float)):
        summa += data_structure
        # иначе выполняется действие 4 add k summa - фу-цию len
    elif isinstance(data_structure, str):
        summa += len(data_structure)
        # возврат из функции значения summa
    return summa

# данные взятые из условия задачи
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
# вывод результата программы
result = calculate_structure_sum(data_structure)
print(result)