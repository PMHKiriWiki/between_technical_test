from src.Services.ApiService import ApiService
from src.Services.CsvService import CsvService

API_URL = 'https://jsonplaceholder.typicode.com/todos/'
STORAGE_FOLDER = 'storage'

class App:
    def __init__(self):
        self._api_service = ApiService(API_URL)
        self._csv_service = CsvService(STORAGE_FOLDER)

    def api_service(self) -> ApiService:
        return self._api_service
    
    def csv_service(self) -> CsvService:
        return self._csv_service
