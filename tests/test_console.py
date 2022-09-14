#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
from io import StringIO

import os
from os import getenv
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """this will test the console"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.console = HBNBCommand()

    def setUp(self):
        """Sets up test cases."""
        if os.path.isfile("file.json"):
            os.remove("file.json")

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual('', f.getvalue())

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db",
                     "can't run if storage is db")
    def test_create(self):
        """Test create command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create asdfsfsd")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
            self.assertEqual(
                "[[User]", f.getvalue()[:7])

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db",
                     "can't run if storage is db")
    def test_create_v2(self):
        """Test create command with parameters."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State name="California"')
            id = f.getvalue()[:-1]
            self.assertEqual(len(id), 36)
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show State {}".format(id))
            self.assertTrue("'name': 'California'" in f.getvalue())
            self.assertEqual(
                "[State]", f.getvalue()[:7])
        with patch('sys.stdout', new=StringIO()) as f:
            self.console\
                .onecmd('create City name="San_Francisco state_id="{}"'
                        .format(id))
            id = f.getvalue()[:-1]
            self.assertEqual(len(id), 36)
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create Place latitude=7.89')
            id = f.getvalue()[:-1]
            self.assertEqual(len(id), 36)
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Place {}".format(id))
            self.assertTrue("'latitude': 7.89" in f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create Place max_guest=5')
            id = f.getvalue()[:-1]
            self.assertEqual(len(id), 36)
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Place {}".format(id))
            self.assertTrue("'max_guest': 5" in f.getvalue())

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db',
                     "can't run if storage is file")
    def test_create_v2_params(self):
        """Test create command with several parameters"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create User email="ilovetim@google.com"\
                               password="timisboss"\
                               first_name="Farrukh" last_name')
            id = f.getvalue()[:-1]
            self.assertEqual(len(id), 36)
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User {}".format(id))
            print(f.getvalue())
            self.assertTrue("'email': 'ilovetim@google.com'" in f.getvalue())
            self.assertTrue("'password': 'timisboss'" in f.getvalue())

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db',
                     "can't run if storage is file")
    def test_show(self):
        """Test show command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show asdfsdrfs")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel abcd-123")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())
