import sys
import sqlite3
import datetime

conn = sqlite3.connect("production.db")
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS expense (amount REAL, category TEXT, date DATE)')

def add_expense(list_of_arguments):
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
    c.execute('INSERT INTO expense VALUES (?, ?, ?)', params)
    conn.commit()

def delete_expense():
    c.execute('DROP table expense')
    conn.commit()
    return 'You deleted all your records'

def list_all_expense():
    c.execute('SELECT * FROM expense')
    list_all_expenses = c.fetchall()
    if len(list_all_expenses) == 0:
        return 'You have no records'
    return f'Here is all your records:\n{list_all_expenses}'

def list_expenses_for_category(list_of_arguments):
    category = (list_of_arguments[2], )
    c.execute('SELECT * FROM expense WHERE category=?', category)
    list_expenses_by_category = c.fetchall()
    return list_expenses_by_category

def list_expenses_for_day(list_of_arguments):
    date = (list_of_arguments[3], )
    c.execute('SELECT * FROM expense WHERE date=?', date)
    list_expenses_by_date = c.fetchall()
    return list_expenses_by_date

def list_expenses_for_month(list_of_arguments):
    date = (list_of_arguments[3], )
    c.execute('SELECT * FROM expense WHERE strftime("%Y-%m", date) = ?', date)
    list_expenses_by_month = c.fetchall()
    return list_expenses_by_month

def list_expenses_for_year(list_of_arguments):
    date = (list_of_arguments[3], )
    c.execute('SELECT * FROM expense WHERE strftime("%Y", date) = ?', date)
    list_expenses_by_year = c.fetchall()
    return list_expenses_by_year


def invoke(cli_arguments, db_name='production.db'):
    # python3 expense.py add 100 food 2021-12-12
    if len(cli_arguments) == 5:
        if cli_arguments[1] == 'add' and cli_arguments[3] and cli_arguments[4]:
            add_expense(cli_arguments)
            return f'You added expenses {cli_arguments[2]} for category {cli_arguments[3]} for {cli_arguments[4]}'

    elif len(cli_arguments) == 4:
        # python3 expense.py add 100 food
        if cli_arguments[1] == 'add' and cli_arguments[3]:
            add_expense(cli_arguments)
            return f'You added expenses {cli_arguments[2]} for category {cli_arguments[3]} for today'
        # python3 expense.py list --day 2021-12-12
        elif cli_arguments[1] == 'list' and cli_arguments[2] == '--day':
            return f'Here is records for {cli_arguments[3]}\n{list_expenses_for_day(cli_arguments)}'

        # python3 expense.py list --month 2021-12
        elif cli_arguments[1] == 'list' and cli_arguments[2] == '--month':
            return f'Here is records for {cli_arguments[3]}\n{list_expenses_for_month(cli_arguments)}'

        # python3 expense.py list --year 2021
        elif cli_arguments[1] == 'list' and cli_arguments[2] == '--year':
            return f'Here is records for {cli_arguments[3]}\n{list_expenses_for_year(cli_arguments)}'

    # python3 expense.py add 100
    elif len(cli_arguments) == 3:
        if cli_arguments[1] == 'add':
            add_expense(cli_arguments)
            return f'You added expenses {cli_arguments[2]} with no category for today'
        # python3 expense.py list food
        elif cli_arguments[1] == 'list':
            return f'Here is records for category {cli_arguments[2]}:\n{list_expenses_for_category(cli_arguments)}'

    # python3 expense.py delete
    elif len(cli_arguments) == 2:
        if cli_arguments[1] == 'delete':
            return delete_expense()

        # python3 expense.py list
        elif cli_arguments[1] == 'list':
            return list_all_expense()


def main():
    print(invoke(sys.argv))


if __name__ == "__main__":
    main()