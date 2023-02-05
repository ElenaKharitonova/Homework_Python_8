# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год.
# Каждому месяцу соответствует своя строка.
# Определите самый жаркий и самый холодный 7-дневный промежуток каждого месяца. 
# Выведите их даты.

import random

def periods_for_month(temperature_in_month, period, month):
    # print(f'Все температуры {temperature_in_month}')
    max_temperature = 0
    day_max_temperature = 1
    min_temperature = 1000
    day_min_temperature = 1
    period = 7

    for day in range(len(temperature_in_month) - period + 1):
        temperature_in_period = temperature_in_month[day:day + period]
        sum_temperature_in_period = sum(temperature_in_month[day:day + period])
        # print(f'{day + 1} - {day + period}.{temperature_in_period} {sum_temperature_in_period}')
        if sum_temperature_in_period > max_temperature:
            max_temperature = sum_temperature_in_period
            day_max_temperature = day
        elif sum_temperature_in_period < min_temperature:
            min_temperature = sum_temperature_in_period
            day_min_temperature = day

    print(f'Средняя максимальная температура была с {day_max_temperature + 1} по {day_max_temperature + period} {month}')
    print(f'Средняя минимальная температура была с {day_min_temperature + 1} по {day_min_temperature + period} {month}')


def zadacha3():
    
    period = 7
    month = 'None'
    day_count = 0
    for j in range(1, 13):
        if j == 1: 
            month = 'января'
            day_count = 31
        elif j == 2: 
            month = 'февраля' 
            day_count = 28
        elif j == 3: 
            month = 'марта'
            day_count = 31
        elif j == 4: 
            month = 'апреля'
            day_count = 30
        elif j == 5: 
            month = 'мая'
            day_count = 31
        elif j == 6: 
            month = 'июня'
            day_count = 30
        elif j == 7: 
            month = 'июля'
            day_count = 31
        elif j == 8: 
            month = 'августа'
            day_count = 31
        elif j == 9: 
            month = 'сентября'
            day_count = 30
        elif j == 10: 
            month = 'октября'
            day_count = 31
        elif j == 11: 
            month = 'ноября'
            day_count = 30
        elif j == 12: 
            month = 'декабря'
            day_count = 31
        
        temperature_in_month = [random.randint(18, 32) for _ in range(day_count)]
        periods_for_month(temperature_in_month, period, month)

zadacha3()