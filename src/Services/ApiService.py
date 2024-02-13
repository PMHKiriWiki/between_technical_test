#!/usr/bin/env python

import requests
import logging

logger = logging.getLogger(__name__)

class ApiService:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_todos(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            todos = response.json()
            return todos
        except requests.exceptions.RequestException as e:
            logger.error(f'Error retrieving TODOs: {e}')
            return None

    def run(self):
        return self.get_todos()