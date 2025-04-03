from common.base_page import BasePage
from common.utils import rename_locust_report
# from common.utils import update_text_file


folderPath = '/TestProject/reports'
class GetVinInfo(BasePage):
    def fetch_data(self):
        headers = {
            'Connection': 'keep-alive',
            'X-RapidAPI-Host': 'car-api2.p.rapidapi.com',
            'X-Rapidapi-Key': 'sR8DcyVfoamshPKhZsLiu8otpSYTp1y5K8qjsnq3EHL2ikb4vm',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x-rapidapi-ua': 'RapidAPI-Playground',
            'Host': 'car-api2.p.rapidapi.com'
        }
        response = self.get("/api/vin/1GTG6CEN0L1139305", headers=headers)
        return response
    
class GetBodies(BasePage):
    def fetch_data(self):
        headers = {
            'Connection': 'keep-alive',
            'X-RapidAPI-Host': 'car-api2.p.rapidapi.com',
            'X-Rapidapi-Key': 'sR8DcyVfoamshPKhZsLiu8otpSYTp1y5K8qjsnq3EHL2ikb4vm',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x-rapidapi-ua': 'RapidAPI-Playground',
            'Host': 'car-api2.p.rapidapi.com'
        }
        response = self.get("/api/bodies?sort=id&verbose=yes&direction=asc", headers=headers)
        
        # if response.status_code == 200:
        #     self.environment.runner.quit()
        rename_locust_report(folderPath, 'get_vin_info')
        return response

# update_text_file(folderPath)
rename_locust_report(folderPath, 'get_vin_info')