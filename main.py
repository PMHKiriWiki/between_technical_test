import logging

from src.Application.App import App

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

app = App()

todos = app.api_service().run()
app.csv_service().run(todos)

           