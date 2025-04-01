import os
from locust import HttpUser, task, between
from EdgePipeline.endpoints.post_eblock_auth import PostEblockAuth
from EdgePipeline.endpoints.post_eblock_auth import PostCognitoAuth


# Load environment configuration
env = os.getenv('ENV', 'development')
if env == 'development':
    import config.development as config
elif env == 'staging':
    import config.staging as config
# elif env == 'production':
#     import config.production as config


# Define the global variable
global_variables = {}

# Function to save a variable
def save_variable(key, value):
    global global_variables
    global_variables[key] = value

class TestProject(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        self.post_eblock_auth = PostEblockAuth(self.client)
        self.post_cognito_auth = PostCognitoAuth(self.client)

    @task
    def test_post_eblock_auth(self):
        self.post_eblock_auth.fetch_data()
    @task
    def test_post_cognito_auth(self):
        self.post_cognito_auth.on_start()

def stop_locust(environment):
    environment.runner.quit()