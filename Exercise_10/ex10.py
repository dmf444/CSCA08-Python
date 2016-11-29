import unittest
import squeal
from database import Table


class TestCartesianProduct(unittest.TestCase):

    def test_01_blank_tables(self):
        # start with two tables that will be empty
        t1 = Table()
        t2 = Table()
        # the result of the cartesian product of two empty tables
        # should iteslf be an empty table
        result = squeal.cartesian_product(t1, t2)
        # we'll know it's an empty table if its dictionary is empty
        result_dict = result.get_dict()
        expected = {}
        self.assertEqual(result_dict, expected,
                         "product of two empty tables should be empty")

    def test_02_one_row_table(self):
        dict1 = {"o.movies": ["Titanic"]}
        dict2 = {"m.awards": ["None"]}
        t1 = Table()
        t2 = Table()
        t1.set_dict(dict1)
        t2.set_dict(dict2)
        result = squeal.cartesian_product(t1, t2)
        result_dict = result.get_dict()
        expected = {"o.movies": ["Titanic"], "m.awards": ["None"]}
        self.assertEqual(result_dict, expected, "Product of two tables with "
                                                "one colunm should be one "
                                                "table with one row")

    def test__03_multi_rows_table(self):
        dict1 = {"o.movies": ["Titanic", "Star Wars", "Star Trek"]}
        dict2 = {"m.awards": ["None", "BEST FILM EVER", "Greatest Sci-fi"]}
        t1 = Table()
        t2 = Table()
        t1.set_dict(dict1)
        t2.set_dict(dict2)
        result = squeal.cartesian_product(t1, t2)
        result_dict = result.get_dict()
        expected = {"o.movies": ["Titanic", "Titanic", "Titanic",
                                 "Star Wars", "Star Wars", "Star Wars",
                                 "Star Trek", "Star Trek", "Star Trek"],
                    "m.awards": ["None", "BEST FILM EVER", "Greatest Sci-fi",
                                 "None", "BEST FILM EVER", "Greatest Sci-fi",
                                 "None", "BEST FILM EVER", "Greatest Sci-fi"]}
        self.assertEqual(result_dict, expected, "Product of two tables with "
                                                "multi colunm should be one "
                                                "table with multiple rows")

    def test_04_multi_column_table(self):
        dict1 = {"o.movies": ["Star Trek"], "o.scifi": ["Star Wars"]}
        dict2 = {"m.awards": ["Greatest Sci-fi"], "m.funny": ["No"]}
        t1 = Table()
        t2 = Table()
        t1.set_dict(dict1)
        t2.set_dict(dict2)
        result = squeal.cartesian_product(t1, t2)
        result_dict = result.get_dict()
        expected = {"o.movies": ["Star Trek"], "o.scifi": ["Star Wars"],
                    "m.awards": ["Greatest Sci-fi"], "m.funny": ["No"]}
        self.assertEqual(result_dict, expected, "Product of 2 columns with "
                                                "one row should be one 4 row"
                                                " column")

    def test_05_multi_column_multi_row_table(self):
        dict1 = {"o.movies": ["Star Trek", "Star Wars"],
                 "o.scifi": ["BattleStar Galactica", "Firefly"]}
        dict2 = {"m.awards": ["Greatest Sci-fi", "worst Sci-fi"],
                 "m.funny": ["No", "yes"]}
        t1 = Table()
        t2 = Table()
        t1.set_dict(dict1)
        t2.set_dict(dict2)
        result = squeal.cartesian_product(t1, t2)
        result_dict = result.get_dict()
        expected = {"o.movies": ["Star Trek", "Star Trek", "Star Wars",
                                 "Star Wars"],
                    "o.scifi": ["BattleStar Galactica", "BattleStar Galactica",
                                "Firefly", "Firefly"],
                    "m.awards": ["Greatest Sci-fi", "worst Sci-fi",
                                 "Greatest Sci-fi", "worst Sci-fi"],
                    "m.funny": ["No", "yes", "No", "yes"]}
        self.assertEqual(result_dict, expected, "Product of "
                                                "multi-column/multi-row "
                                                "should be a table with 4 "
                                                "columns and 4 rows")

    def test_06_empty_column_table(self):
        dict1 = {"o.movies": [], "o.scifi": []}
        dict2 = {"m.awards": [], "m.funny": []}
        t1 = Table()
        t2 = Table()
        t1.set_dict(dict1)
        t2.set_dict(dict2)
        result = squeal.cartesian_product(t1, t2)
        result_dict = result.get_dict()
        expected = {"o.movies": [], "o.scifi": [], "m.awards": [],
                    "m.funny": []}
        self.assertEqual(result_dict, expected, "Product of two tables with "
                                                "empty columns should be an "
                                                "empty row")

if(__name__ == "__main__"):
    unittest.main(exit=False)
