# Expense

Expense is a console application for tracking expenses.


## Installation
```bash
git clone https://github.com/mariadenadel/expense.git
cd expense
```

## Usage

```bash
python3 expense.py add 100 - добавлене расхода с сумой 100 без категории и на сегодня
python3 expense.py add 100 Еда - добавлене расхода с сумой 100 с категорией Еда на сегодня
python3 expense.py add 100 Еда 2021-12-13 - добавлене расхода с сумой 100 с категорией Еда на 13 декабря 2021

python3 expense.py list - статистика по всем категориям
python3 expense.py list <name-of-the-category> - статистика по выбраной категории
python3 expense.py list --day <day> - статистика за день / <day> в формате YYYY-MM-DD
python3 expense.py list --month <month> - статистика за месяц / <month> в формате YYYY-MM
python3 expense.py list --year <year> - статистика за год / <year> в формате YYYY-MM

python3 expense.py delete - очистить все данные
python3 expense.py --help - помощь
```

## Did not do

1. Нет возможности добавления нескольких пользователей
2. Не в табличном формате выдается статистика
3. Не дописаны unit tests