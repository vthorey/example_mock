from django.test import TestCase
from mock import patch
from some_app.my_module import function


class Test(TestCase):

    @patch('some_app.my_module.function.other_function')
    def function_test(self, mock_other_function):
        func()
