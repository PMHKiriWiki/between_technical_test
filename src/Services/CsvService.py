import os
import csv
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class CsvService:
    def __init__(self, storage_folder):
        self.storage_folder = storage_folder

        if not os.path.exists(self.storage_folder):
            os.makedirs(self.storage_folder)

    def convert_to_csv(self, todo):
        datetime_format = '%Y_%m_%d'
        todo_id = todo.get('id', 'unknown')

        try:
            csv_filename = f'{datetime.now().strftime(datetime_format)}_{todo_id}.csv'
            csv_path = os.path.join(self.storage_folder, csv_filename)

            with open(csv_path, 'w', newline='') as csvfile:
                fieldnames = todo.keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerow(todo)

            logger.info(f'CSV file \'{csv_path}\' created successfully.')
        except Exception as e:
            logger.error(f'Error creating CSV file: {e}')
