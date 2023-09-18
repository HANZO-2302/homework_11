"""Защищенная функция"""


def _is_leap_year(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True


"""Проверка даты на существования"""


def is_date_valid(date):
	day, month, year = map(int, date.split('.'))

	if year < 1 or year > 9999:
		return False

	if month < 1 or month > 12:
		return False

	if month in [1, 3, 5, 7, 8, 10, 12]:
		max_day = 31
	elif month == 2:
		if _is_leap_year(year):
			max_day = 29
		else:
			max_day = 28
	else:
		max_day = 30

	if day < 1 or day > max_day:
		return False

	return True



