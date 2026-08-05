# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps

import calendar, locale

locale.setlocale(locale.LC_ALL, '') #locale muda as caracteristicas para a mesma do sistema operacional (tanto de tempo quanto de dinheiro etc)
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8') #mesma coisa mas colocando o locale manualmente
print(locale.getlocale())#imprime qual é o locale (pt_BR) e a configuracao de caracteres
print(calendar.calendar(2026))
