import unittest
from unittest.mock import patch

from src import hello_world


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_hello_world() -> None:
        with patch('builtins.print') as mock_print:
            hello_world.hello()
            mock_print.assert_called_with("Hello, World!")


if __name__ == '__main__':
    unittest.main()
