from locust import HttpUser, task
import time, json

class FlaskMLUser(HttpUser):
    @task
    def home_page(self):
        self.client.get("/")

    @task
    def prediction(self):
        data = {
            "CHAS": {
                "0": 0
            },
            "RM": {
                "0": 6.575
            },
            "TAX": {
                "0": 296.0
            },
            "PTRATIO": {
                "0": 15.3
            },
            "B": {
                "0": 396.9
            },
            "LSTAT": {
                "0": 4.98
            }
        }
        headers = {'content-type': 'application/json'}
        self.client.post("/predict", data = json.dumps(data), headers = headers)