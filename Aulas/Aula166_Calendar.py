# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo

import calendar

print(calendar.calendar(2026)) #gera o calendario do ano
print(calendar.month(2022, 12)) #calendario do mes

print(calendar.monthrange(2026,5))#monthrange imprime o dia da semana do primeiro dia do mes e o dia do mes do ultimo dia do mes
first_day, last_day = calendar.monthrange(2026, 2) #pega o primeiro e ultimo dia do mes
print(list(enumerate(calendar.day_name))) #enumera os dias da semana
print(calendar.day_name[first_day]) #me fala o nome do primeiro dia do mes
print(calendar.day_name[calendar.weekday(2026, 2, last_day)]) #e aqui me fala o nome do ultimo dia
print(calendar.monthcalendar(2026, 5)) #monthcalendar mostra o mes separado em listas semanais(onde tem 0, representa que nao pertence aquele mes)
for week in calendar.monthcalendar(2026, 5):
    for day in week:
        if day == 0:
            continue
        print(day)