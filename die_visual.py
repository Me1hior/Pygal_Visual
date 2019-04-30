from die import Die
import pygal

# Бросок двух кубиков
die_1 = Die()
die_2 = Die()

# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_num in range(500000):
	result = die_1.roll() + die_2.roll()
	results.append(result)
	
# Анализ результатов.
frequencies = []
max_result = 1 + die_1.num_sides + die_2.num_sides
min_result = Die.numb
for value in range(min_result, max_result):
	frequency = results.count(value)
	frequencies.append(frequency)
print(frequencies)

# Построение гистограммы
# Имея список частот, можно построить гистограмму результатов. 

# Визуализация результатов.
hist = pygal.Bar()						# построить столбцовую диаграмму, мы создаем экземпляр 
hist.title = "Results of rolling tree D6 dice 500000 times."
hist.x_labels = [str(i) for i in range(min_result, max_result)] 
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D6', frequencies)		# Метод add() используется для добавления на гистограмму серии значений
hist.render_to_file('die_visual.svg')	# диаграмма записывается в файл SVG




