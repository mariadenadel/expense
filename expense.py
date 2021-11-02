import sys
import sqlite3
import datetime

def execute_query(db_name, *args):
    connection = sqlite3.connect(db_name)
    cursor_connect = connection.cursor()
    connection.commit()
    return cursor_connect.execute(*args)

execute_query('production.db', 'CREATE TABLE IF NOT EXISTS expense (amount REAL, category TEXT, date DATE)')

def add_expense(list_of_arguments, db_name):
    amount = list_of_arguments[2]
    if len(list_of_arguments) == 5:
        category = list_of_arguments[3]
        date = list_of_arguments[4]

    elif len(list_of_arguments) == 4:
        category = list_of_arguments[3]
        date = datetime.date.today()

    elif len(list_of_arguments) == 3:
        category = 'uncategorized'
        date = datetime.date.today()

    params = (amount, category, date)

    connection = sqlite3.connect(db_name)
    cursor_connect = connection.cursor()
    cursor_connect.execute('INSERT INTO expense VALUES (?, ?, ?)', params)
    connection.commit()


def delete_expense(db_name):
    execute_query(db_name, 'DROP TABLE IF EXISTS expense')
    return 'You deleted all your records'

def list_all_expense(db_name):
    list_all_expenses = execute_query(db_name, 'SELECT * FROM expense').fetchall()

    if len(list_all_expenses) == 0:
        return 'You have no records'
    return f'Here is all your records:\n{list_all_expenses}'

def list_expenses_for_category(list_of_arguments, db_name):
    category = (list_of_arguments[2], )
    list_expenses_by_category = execute_query(db_name, 'SELECT * FROM expense WHERE category=?', category).fetchall()

    return list_expenses_by_category

def list_expenses_for_day(list_of_arguments, db_name):
    date = (list_of_arguments[3], )
    list_expenses_by_date = execute_query(db_name, 'SELECT * FROM expense WHERE date=?', date).fetchall()
    return list_expenses_by_date

def list_expenses_for_month(list_of_arguments, db_name):
    date = (list_of_arguments[3], )
    list_expenses_by_month = execute_query(db_name, 'SELECT * FROM expense WHERE strftime("%Y-%m", date) = ?', date).fetchall()
    return list_expenses_by_month

def list_expenses_for_year(list_of_arguments, db_name):
    date = (list_of_arguments[3], )
    list_expenses_by_year = execute_query(db_name, 'SELECT * FROM expense WHERE strftime("%Y", date) = ?', date).fetchall()
    return list_expenses_by_year


def invoke(cli_arguments, db_name='production.db'):
    # python3 expense.py add 100 food 2021-12-12
    if len(cli_arguments) == 5:
        if cli_arguments[1] == 'add' and cli_arguments[3] and cli_arguments[4]:
            add_expense(cli_arguments, db_name)
            return f'You added {cli_arguments[2]} to expenses for category {cli_arguments[3]} for {cli_arguments[4]}'

    elif len(cli_arguments) == 4:
        # python3 expense.py add 100 food
        if cli_arguments[1] == 'add' and cli_arguments[3]:
            add_expense(cli_arguments, db_name)
            return f'You added {cli_arguments[2]} to expenses for category {cli_arguments[3]} for today'
        # python3 expense.py list --day 2021-12-12
        elif cli_arguments[1] == 'list' and cli_arguments[2] == '--day':
            return f'Here is records for {cli_arguments[3]}\n{list_expenses_for_day(cli_arguments, db_name)}'

        # python3 expense.py list --month 2021-12
        elif cli_arguments[1] == 'list' and cli_arguments[2] == '--month':
            return f'Here is records for {cli_arguments[3]}\n{list_expenses_for_month(cli_arguments, db_name)}'

        # python3 expense.py list --year 2021
        elif cli_arguments[1] == 'list' and cli_arguments[2] == '--year':
            return f'Here is records for {cli_arguments[3]}\n{list_expenses_for_year(cli_arguments, db_name)}'

    # python3 expense.py add 100
    elif len(cli_arguments) == 3:
        if cli_arguments[1] == 'add':
            add_expense(cli_arguments, db_name)
            return f'You added {cli_arguments[2]} to expenses with no category for today'
        # python3 expense.py list food
        elif cli_arguments[1] == 'list':
            return f'Here is records for category {cli_arguments[2]}:\n{list_expenses_for_category(cli_arguments, db_name)}'

    # python3 expense.py delete
    elif len(cli_arguments) == 2:
        if cli_arguments[1] == 'delete':
            return delete_expense(db_name)

        # python3 expense.py list
        elif cli_arguments[1] == 'list':
            return list_all_expense(db_name)
        # python3 expense.py --help
        elif cli_arguments[1] == '--help':
            return 'Need help?\npython3 expense.py add 100 - добавлене расхода с сумой 100 без категории и на сегодня\npython3 expense.py add 100 Еда - добавлене расхода с сумой 100 с категорией Еда на сегодня\npython3 expense.py add 100 Еда 2021-12-13 - добавлене расхода с сумой 100 с категорией Еда на 13 декабря 2021\npython3 expense.py list - статистика по всем категориям\npython3 expense.py list <name-of-the-category> - статистика по выбраной категории\npython3 expense.py list --day <day> - статистика за день / <day> в формате YYYY-MM-DD\npython3 expense.py list --month <month> - статистика за месяц  / <month> в формате YYYY-MM\npython3 expense.py list --year <year> - статистика за год / <year> в формате YYYY\npython3 expense.py delete - очистить все данные'



def main():
    print(invoke(sys.argv))


if __name__ == "__main__":
    main()