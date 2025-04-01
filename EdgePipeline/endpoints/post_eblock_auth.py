import os
from common.base_page import BasePage
import config.staging as config


# Define the global variable
global_variables = {}

# Function to save a variable
def save_variable(key, value):
    global global_variables
    global_variables[key] = value

class PostEblockAuth(BasePage):
    def fetch_data(self):
        headers = {
            'Connection': 'keep-alive',
            'Authorization': 'Token token=74ca558f-76eb-4447-ab80-b676750b1704',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Host': 'staging.edgepipeline.com'
        }
        response = self.get("/eblock/passport/"+config.EBLOCK_PASSPORT_TOKEN, headers=headers)
        # print(global_variables)
        return response

class PostCognitoAuth(BasePage):
    def on_start(self):
        post_data = {
            "AuthParameters": {
                "USERNAME": config.PUBLIC_API_PIPELINE_USERNAME,
                "PASSWORD": config.PUBLIC_API_PIPELINE_PASSWORD
            },
            "AuthFlow": "USER_PASSWORD_AUTH",
            "ClientId": config.PUBLIC_API_PIPELINE_CLIENT_ID
        }
        headers = {
            'X-Amz-Target': 'AWSCognitoIdentityProviderService.InitiateAuth',
            'Content-Type': 'application/x-amz-json-1.1'
        }
        response = self.post('https://cognito-idp.us-west-2.amazonaws.com', json=post_data, headers=headers)
        save_variable('auth_response', response.json())
        return response


