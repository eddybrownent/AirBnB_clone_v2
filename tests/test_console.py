import os
import sys
import unittest
from console import HBNBCommand
from unittest.mock import patch
from models.base_model import BaseModel


class TestCreateCommand(unittest.TestCase):
    """
    Test cases for the create command in the HBNBCommand class
    """

    def setUp(self):
        """
        Set up the test environment before each test case
        """
        self.console = HBNBCommand()

    def test_create_when_missing_class_name(self):
        """
        Test behavior when class name is missing
        """
        with patch('builtins.print') as mock_print:
            self.console.do_create("")
            mock_print.assert_called_with("** class name missing **")

    def test_create_when_invalid_class_name(self):
        """
        Test behavior when an invalid class name is provided
        """
        with patch('builtins.print') as mock_print:
            self.console.do_create("InvalidClassName")
            mock_print.assert_called_with("** class doesn't exist **")

    def test_create_base_model(self):
        """
        Test creating an instance of the BaseModel class
        """
        with patch('builtins.print') as mock_print:
            self.console.do_create("BaseModel")
            mock_print.assert_called_with("{}".format(BaseModel().id))

    def test_create_with_integer_parameter(self):
        """
        Test creating an instance with an integer parameter
        """
        with patch('builtins.print') as mock_print:
            self.console.do_create("BaseModel int_param=42")
            instance = self.console.classes["BaseModel"]()
            instance.int_param = 42
            instance.save()
            mock_print.assert_called_with("{}".format(instance.id))

    def test_create_with_float_parameter(self):
        """
        Test creating an instance with a float parameter
        """
        with patch('builtins.print') as mock_print:
            self.console.do_create("BaseModel float_param=3.14")
            instance = self.console.classes["BaseModel"]()
            instance.float_param = 3.14
            instance.save()
            mock_print.assert_called_with("{}".format(instance.id))

    def test_create_with_string_parameter(self):
        """
        Test creating an instance with a string parameter
        """
        with patch('builtins.print') as mock_print:
            self.console.do_create('BaseModel str_param="Hello_World"')
            instance = self.console.classes["BaseModel"]()
            instance.str_param = "Hello World"
            instance.save()
            mock_print.assert_called_with("{}".format(instance.id))


if __name__ == '__main__':
    unittest.main()
