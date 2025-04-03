import time
import os
from locust import events
from locust.runners import MasterRunner

from datetime import datetime
from locust import HttpUser, task, between
# from common.utils import rename_locust_report
from endpoints.get_vin_info import GetBodies
from endpoints.get_vin_info import GetVinInfo

# Define the global variable
global_variables = {}

def generate_report_filename():
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    return f"report_{timestamp}.html"

# Function to save a variable
def save_variable(key, value):
    global global_variables
    global_variables[key] = value


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    if not isinstance(environment.runner, MasterRunner):
        print("Beginning test setup")
    else:
        print("Started test from Master node")

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


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    if not isinstance(environment.runner, MasterRunner):
        print("Cleaning up test data")
    else:
        print("Stopped test from Master node")
        
if __name__ == "__main__":
    os.system(f"locust -f locustfile.py --headless --host=https://car-api2.p.rapidapi.com -u 5 -r 5 --run-time 10s --html={generate_report_filename()}")
