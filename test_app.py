import unittest
from app import app, main

class TestApplication(unittest.TestCase):

    def test_main(self):
        self.assertEqual(main(), "Hello world")

    def test_home_route(self):
        client = app.test_client()
        response = client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello world")

if __name__ == "__main__":
    unittest.main()
