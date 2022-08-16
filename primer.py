math_values = [] # делаем 3 пустых списка с оценками
physics_values = []
russian_values = []
with open('dataset_3363_4.txt', 'r') as in_file: # открываем файл с оценками
    for line in in_file: # для каждой строки записываем в математику элемент с индексом 1, в физику 2, в русский 3, т.е наполняем списки оценками
        current_line = line.strip().split(';') # предварительно парсим каждую строку через ; и убираем перенос строки
        math_values.append(int(current_line[1]))
        physics_values.append(int(current_line[2]))
        russian_values.append(int(current_line[3]))
out_file = open('statistic.txt', 'w') # записываем в файл
for i in range(len(math_values)): # для каждого элемента в списке математики считаем среднее арифметическое оценок и переносим строку
    out_file.write(str((math_values[i] + physics_values[i] + russian_values[i]) / 3) + '\n')
if len(math_values) > 0: # пока длина списка больше 0 мы записываем в файл среднее число по математике из всех, и так по каждому списку, через пробел. В конце закрываем файл
    out_file.write(str(sum(math_values) / len(math_values)) + ' ' +
                   str(sum(physics_values) / len(physics_values)) + ' ' +
                   str(sum(russian_values) / len(russian_values)))
out_file.close()