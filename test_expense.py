import unittest
import sqlite3
import datetime
import os
from expense import invoke, execute_query, list_all_expense


execute_query('test.db', 'CREATE TABLE IF NOT EXISTS expense (amount REAL, category TEXT, date DATE)')


class TestExpense(unittest.TestCase):

    def test_add_expense(self):
        invoke(['expense.py add 999 testcategory 2021-12-12'], 'test.db') # разобраться почему не работает инвоук
        result= list_all_expense('test.db')
        self.assertEqual(result, [(999, 'testcategory', '2021-12-12')])


        result = add(2, 3)

        assertEqual(result, 5)

    #     test_second_comand = invoke('python3 expense.py add 999 testcategory', 'test.db')
    #     self.assertEqual(test_second_comand, 0)

    #     test_third_comand = invoke('python3 expense.py add 999', 'test.db')
    #     self.assertEqual(test_third_comand, 0)

    # def test_list_expenses(self):
    #     test_comand_all = invoke('python3 expense.py list', 'test.db')
    #     self.assertEqual(test_comand_all, 0)

    #     test_comand_day = invoke('python3 expense.py list --day 2021-11-01', 'test.db')
    #     self.assertEqual(test_comand_day, 0)

    #     test_comand_month = invoke('python3 expense.py list --month 2021-11', 'test.db')
    #     self.assertEqual(test_comand_month, 0)

    #     test_comand_year = invoke('python3 expense.py list --year 2021', 'test.db')
    #     self.assertEqual(test_comand_year, 0)

    # def test_delete_all_expenses(self):
    #     test_comand_delete = invoke('python3 expense.py delete', 'test.db')
    #     self.assertEqual(test_comand_delete, 0)

if __name__ == "__main__":
    unittest.main()