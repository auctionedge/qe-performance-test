import os
from common.base_page import BasePage
import config.staging as config


global_variables = {}


def save_variable(key, value):
    global global_variables
    global_variables[key] = value

class AssetsByStockNumber(BasePage):
    def graphql_query(self):
        query = """
        query documentList($auctionId: String!, $stockNumber: String!) 
        {
            SparkDocs_Document(id: $auctionId) 
            {
                assetsByStockNumber(auctionId: $auctionId, stockNumber: $stockNumber) 
                {
                    assetId
                    consignorAccountId
                }
            }
        }
        """
        variables = {
            "auctionId": config.AUCTION_ID,
            "stockNumber": config.STOCK_NUMBER
        }
        headers = {
            "Authorization": config.AUCTION_API_BEARER_TOKEN,
            "Content-Type": "application/json"
        }
        
        response = self.post("/graphql", json={"query": query, "variables": variables}, headers=headers)
        save_variable('assets_response', response.json())
        return self.post("/graphql", json={"query": query, "variables": variables}, headers=headers)
