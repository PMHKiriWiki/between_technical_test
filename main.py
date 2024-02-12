import logging

from src.Services.ApiService import ApiService
from src.Services.CsvService import CsvService

API_URL = 'https://jsonplaceholder.typicode.com/todos/'
STORAGE_FOLDER = 'storage'


def convert_todos_to_csv(todos): 
    if not todos:
        return
    
    for todo in todos:
         csv_service.convert_to_csv(todo)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    api_service = ApiService(api_url=API_URL)
    csv_service = CsvService(storage_folder=STORAGE_FOLDER)

    todos = api_service.get_todos()

    convert_todos_to_csv(todos)

           