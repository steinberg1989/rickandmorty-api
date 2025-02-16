import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"

class TestRickAndMortyAPI(unittest.TestCase):

    def test_healthcheck(self):
        """Test if the healthcheck endpoint returns status OK"""
        response = requests.get(f"{BASE_URL}/healthcheck")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "OK"})

    def test_characters(self):
        """Test if the /characters endpoint returns a list of characters"""
        response = requests.get(f"{BASE_URL}/characters")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json(), list))
        self.assertGreater(len(response.json()), 0)

    def test_docs(self):
        """Test if the Swagger documentation page is accessible"""
        response = requests.get(f"{BASE_URL}/docs")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
