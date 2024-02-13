import unittest
import os
import shutil
from datetime import datetime
from unittest.mock import patch, mock_open

from src.Services.CsvService import CsvService


class TestCsvService(unittest.TestCase):

    def setUp(self):
        self.storage_folder = 'test_folder'
        self.csv_service = CsvService(self.storage_folder)

    def tearDown(self):
        if os.path.exists(self.storage_folder):
            shutil.rmtree(self.storage_folder)


    def test_convert_to_csv_success(self):
        # Create a sample todo
        todo = {'id': '123', 'task': 'Sample Task', 'status': 'Pending'}

        # Get the expected CSV path and filename
        expected_filename = f"{datetime.now().strftime('%Y_%m_%d')}_{todo['id']}.csv"
        expected_path = os.path.join(self.storage_folder, expected_filename)

        # Perform the convert_to_csv operation
        self.csv_service.convert_to_csv(todo)

        # Check if the CSV file was created correctly
        self.assertTrue(os.path.exists(expected_path))
    

    @patch('src.Services.CsvService.CsvService.convert_to_csv')
    def test_run_no_todos(self, mock_convert_to_csv):
        # Call the run method with an empty todos list
        self.csv_service.run([])

        # Ensure that convert_to_csv is not called
        mock_convert_to_csv.assert_not_called()
        

    @patch('src.Services.CsvService.CsvService.convert_to_csv')
    def test_run_with_todos(self, mock_convert_to_csv):
        # Create a sample todo
        sample_todo = {'id': '123', 'task': 'Sample Task', 'status': 'Pending'}

        # Call the run method with a list containing the sample todo
        self.csv_service.run([sample_todo])

        # Ensure that convert_to_csv is called once with the expected todo
        mock_convert_to_csv.assert_called_once_with(sample_todo)



if __name__ == '__main__':
    unittest.main()
