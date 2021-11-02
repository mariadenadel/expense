import unittest
import sqlite3
import datetime
import os
from expense import invoke, execute_query, list_all_expense, delete_expense

execute_query('test.db', 'CREATE TABLE IF NOT EXISTS expense (amount REAL, category TEXT, date DATE)')

class TestExpense(unittest.TestCase):

    def test_add_full_expense(self):
        full_comand = invoke(['expense.py', 'add', 999, 'testcategory', '2021-12-12'], 'test.db')
        wanted_result = "You added 999 to expenses for category testcategory for 2021-12-12"
        self.assertEqual(full_comand, wanted_result)

        comand_without_date = invoke(['expense.py', 'add', 999, 'testcategory', datetime.date.today()], 'test.db')
        wanted_result = f"You added 999 to expenses for category testcategory for {datetime.date.today()}"
        self.assertEqual(comand_without_date, wanted_result)

        comand_without_date_without_category = invoke(['expense.py', 'add', 999, 'uncategorized', datetime.date.today()], 'test.db')
        wanted_result = f"You added 999 to expenses for category uncategorized for {datetime.date.today()}"
        self.assertEqual(comand_without_date_without_category, wanted_result)


    def test_list_records(self):
        wanted_result = "Here is all your records:\n[(999.0, 'testcategory', '2021-12-12'), (999.0, 'testcategory', '2021-11-02'), (999.0, 'uncategorized', '2021-11-02')]"
        self.assertEqual(list_all_expense('test.db'), wanted_result)

if __name__ == "__main__":
    unittest.main()