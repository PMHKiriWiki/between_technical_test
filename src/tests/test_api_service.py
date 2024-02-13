import requests
import unittest
from unittest.mock import patch

from src.Services.ApiService import ApiService

class TestApiService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_url = 'http://mock.url'
    def setUp(self):
        self.api_service = ApiService(self.api_url)

    @patch('requests.get')
    def test_run_success(self, mock_get):
        mock_get.return_value.json.return_value = [{'id': 1, 'title': 'Sample Todo'}]

        result = self.api_service.run()

        self.assertIsNotNone(result)
        self.assertEqual(result, [{'id': 1, 'title': 'Sample Todo'}])

    @patch('requests.get')
    def test_run_failure(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException('Fake error')

        result = self.api_service.run()

        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
