import unittest
from app import main


class TestApplication(unittest.TestCase):

    def test_main(self):
        self.assertEqual(main(), "Hello world")


if __name__ == "__main__":
    unittest.main()
