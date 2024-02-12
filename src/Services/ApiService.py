import os
import csv
import logging
import requests

from sys import stderr
from datetime import datetime

logger = logging.getLogger(__name__)


class ApiService:
    def __init__(self, api_url):
        self.api_url = api_url
        self.storage_folder = 'storage'

    def get_todos(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()

            todos = response.json()

            return todos
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving TODOs: {e}", file=stderr)
            logger.info(f"Error retrieving TODOs: {e}", file=stderr)
            return None
        
    def convert_to_csv(self, todo):
        datetime_format = '%Y_%m_%d'
        todo_id = todo.get('id', 'unknown')

        try:
            csv_filename = f"{datetime.now().strftime(datetime_format)}_{todo_id}.csv"
            csv_path = os.path.join(self.storage_folder, csv_filename)

            with open(csv_path, 'w', newline='') as csvfile:
                fieldnames = todo.keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerow(todo)

            print(f"CSV file '{csv_path}' created successfully.")
        except Exception as e:
            print(f"Error creating CSV file: {e}", file=stderr)
            
    def extract_todos_to_storage(self, todos): 
        if not todos:
            return

        for todo in todos:
            self.convert_to_csv(todo)

    def run(self):
        print('Running ApiService', file=stderr)

        todos = self.get_todos()

        self.extract_todos_to_storage(todos)
    
