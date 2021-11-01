# Expense

Expense is a console application for tracking expenses.


## Installation

git clone
cd expense

## Usage

```bash
python3 expense.py add 100 - добавлене расхода с сумой 100 без категории и на сегодня
python3 expense.py add 100 Еда - добавлене расхода с сумой 100 с категорией Еда на сегодня
python3 expense.py add 100 Еда 2021-12-13 - добавлене расхода с сумой 100 с категорией Еда на 13 декабря 2021

python3 expense.py list - статистика по всем категориям
python3 expense.py list <name-of-the-category> - статистика по выбраной категории
python3 expense.py list --day <day> - статистика за день
python3 expense.py list --month <month> - статистика за месяц
python3 expense.py list --year <year> - статистика за год

python3 expense.py delete - очистить все данные
```
