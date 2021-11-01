import unittest
# import sqlite3
import datetime
import os

# conn = sqlite3.connect(":memory:")
# c = conn.cursor()
# c.execute('CREATE TABLE IF NOT EXISTS expense (amount REAL, category TEXT, date DATE)')



class TestExpense(unittest.TestCase):

    def test_add_expense(self):
        self.assertEqual(self.test_add_expense, 0)

        test_second_comand = os.system('python3 expense.py add 999 testcategory')
        self.assertEqual(test_second_comand, 0)

        test_third_comand = os.system('python3 expense.py add 999')
        self.assertEqual(test_third_comand, 0)

    def test_list_expenses(self):
        test_comand_all = os.system('python3 expense.py list')
        self.assertEqual(test_comand_all, 0)

        test_comand_day = os.system('python3 expense.py list --day 2021-11-01')
        self.assertEqual(test_comand_day, 0)

        test_comand_month = os.system('python3 expense.py list --month 2021-11')
        self.assertEqual(test_comand_month, 0)

        test_comand_year = os.system('python3 expense.py list --year 2021')
        self.assertEqual(test_comand_year, 0)

    def test_delete_all_expenses(self):
        test_comand_delete = os.system('python3 expense.py delete')
        self.assertEqual(test_comand_delete, 0)

if __name__ == "__main__":
    unittest.main()