from locust import HttpUser, task, between
from endpoints.get_vin_info import GetBodies
from endpoints.get_vin_info import GetVinInfo

# Define the global variable
global_variables = {}

# Function to save a variable
def save_variable(key, value):
    global global_variables
    global_variables[key] = value

class TestProject(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        self.get_top_bodies = GetBodies(self.client)
        self.get_vin_info = GetVinInfo(self.client)

    @task
    def test_get_top_bodies(self):
        self.get_top_bodies.fetch_data()
    @task
    def test_get_vin_info(self):
        self.get_vin_info.fetch_data()