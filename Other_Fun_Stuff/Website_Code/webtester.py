import os, sys

import MySQLdb

t


def test_assignment_code(unittest_name: str) -> None:
    """
    Funtion is called by a button press on the website page and tests the
    submitted code. Produces files to tell students how much they've failed.
    :param unittest_name: file name of the uniittest
    :return: None
    REQ: name must not be none
    """
    testing_dir = sys.path[0] + "\\unittest\\"
    temp_path_unittest = sys.path[0] + "\\" + unittest_name
    # Move Unittest file to Testing Directory
    os.rename(temp_path_unittest, testing_dir + unittest_name)
    conn = MySQLdb.connect(host="localhost", password="", user="root",
                           database="marker")

    curr = conn.cursor()
    curr.execute("SELECT * FROM _ WHERE _ == _")
    data = curr.fetchall()
    curr.close()
