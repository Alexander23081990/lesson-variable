number_homework = 12  # #:выподненные ДЗ
number_hours_spent = 1.5  # #:затраченные часы
course_name = 'Python'  # #:имя курса
time_on_one_task = number_hours_spent / number_homework  # #:время на одно задание
print('Курс: ' + course_name + ',', 'всего задач: ' + str(number_homework) + ',',
      'затрачено часов: ' + str(number_hours_spent) + ',', 'среднее время выполнения: ' + str(time_on_one_task))
