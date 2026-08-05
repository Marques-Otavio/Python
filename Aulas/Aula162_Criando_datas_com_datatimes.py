# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

# Instalando o pytz
# pip install pytz types-pytz


from datetime import datetime
from pytz import timezone

data = datetime.now()
print(datetime.fromtimestamp(1780849077.739638)) #timestamp é o numero de segundos desde 1970
# data = datetime.now(timezone('Asia/Tokyo'))
# data_str_data = '2026/07/30 09:41:49'
# data_str_formato = '%Y/%m/%d %H:%M:%S'#esse é o formato para ficar igual a linha de cima


# data = datetime(2026, 7, 30, 9, 41, 49)
# data = datetime.strptime(data_str_data, data_str_formato)
print(data)