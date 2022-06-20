#if date = ("exit or task = ("exit") or name = ("exit")
#  print("Спасибо за использование! До свидания!")
#else:
days = ['Сегодня', 'Завтра', 'Послезавтра']
name = input('Введи имя\n')
try:
  age = int(input('Введи свой возраст\n'))
except ValueError as err:
  print("Введи число!")
if age == 2022-1980: # Проверка 
  print('Привет, %s. ' % name + "Доступ подтвержден!\n")
  task_dict = {} # Создаем пустой словарь, в который затем будем добавлять записи
else:
  print("Access denied!\n")
  sys.exit(n) # Если возраст неподтвержден, выполнение программы завершается


today = input('Введите сегодняшнюю дату: \n')
task = input('Введите задачу: \n')
task_dict[today] = task
print((days)[0] + ' запланировано: ' + task + ' \nХорошего дня!\n') # Добавляем вывод на экран после ввода)

tomorrow = input('Введите дату: ')
task = input('Введите задачу: ')
task_dict[tomorrow] = task
print((days)[1] + ' запланировано: ' + task + ' \nЗапланируем что-то стоящее на послезавтра!\n') # Добавляем вывод на экран после ввода)


afttomorrow = input('Введите дату: \n')
task = input('Введите задачу: \n')
task_dict[afttomorrow] = task
print((days)[2] + ' запланировано: ' + task + ' \nУспехов!\n') # Добавляем вывод на экран после ввода)

#date = ///
#task = input('Введите задачу: \n')
#task_dict[date] = task
#print(date, task)
# print(date, task)
# print(task_dict)
# Переменные date и task изменяются, но данные в словаре task_dict остаются 