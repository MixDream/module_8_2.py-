def personal_sum(numbers):
  result = 0
  incorrect_data = 0
  for num in numbers:
    try:
      result += num
    except TypeError:
      incorrect_data += 1
      print(f"Некорректный тип данных для подсчёта суммы - {num}")
  return result, incorrect_data

def calculate_average(numbers):
  try:
    sum, incorrect_data = personal_sum(numbers)
    if incorrect_data > 0:
      print("В numbers записан некорректный тип данных")
      return None
    if len(numbers) == 0:
      return 0
    return sum / len(numbers)
  except TypeError:
    print("В numbers записан некорректный тип данных")
    return None
  except ZeroDivisionError:
    return 0
print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
