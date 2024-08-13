from typing import Any
from openapi_client.models import POSTRequest

class DefaultApi:
    def __init__(self, api_client):
        self.api_client = api_client

    def post(self, request: POSTRequest) -> Any:
        url = "/"
        headers = {"Content-Type": "application/json"}
        body = request.to_dict()
        response = self.api_client.post(url, headers=headers, json=body)
        if response.status_code != 200:
            raise Exception(f"API call failed: {response.status_code} {response.text}")
        return response.json()