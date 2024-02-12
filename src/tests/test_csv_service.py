import unittest
import shutil
from unittest.mock import patch
from datetime import datetime
import os

from src.Services.CsvService import CsvService


class TestCsvService(unittest.TestCase):
    def setUp(self):
        self.storage_folder = 'test_storage'
        self.csv_service = CsvService(storage_folder=self.storage_folder)

    def tearDown(self):
        if os.path.exists(self.storage_folder):
            shutil.rmtree(self.storage_folder)

    @patch('src.Services.CsvService.datetime')
    def test_convert_to_csv_success(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 1, 1, 12, 0, 0)
        
        todo = {'id': 1, 'title': 'Test Todo', 'completed': False}
        self.csv_service.convert_to_csv(todo)

        csv_path = os.path.join(self.storage_folder, '2024_01_01_1.csv')

        self.assertTrue(os.path.exists(csv_path))

@patch('src.Services.CsvService.datetime')
@patch('builtins.open', side_effect=Exception('Simulated error'))
def test_convert_to_csv_failure(self, mock_open, mock_datetime):
    mock_datetime.now.return_value = datetime(2024, 1, 1, 12, 0, 0)

    todo = {'id': 1, 'title': 'Test Todo', 'completed': False}
    with self.assertRaises(Exception):
        self.csv_service.convert_to_csv(todo)


if __name__ == '__main__':
    unittest.main()
