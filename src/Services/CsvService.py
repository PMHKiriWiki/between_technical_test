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
            
        except FileNotFoundError as file_not_found_error:
            logger.error(f'Error creating CSV file. File not found error: {file_not_found_error}')
        except PermissionError as permission_error:
            logger.error(f'Error creating CSV file. Permission error: {permission_error}')
        except csv.Error as csv_error:
            logger.error(f'Error creating CSV file. CSV error: {csv_error}')
        except Exception as e:
            logger.error(f'Error creating CSV file: {e}')

    def run(self, todos):
        if not todos: 
            logger.info(f'There is no TODO records to be processed')
            return
        
        for todo in todos:
            self.convert_to_csv(todo)
        