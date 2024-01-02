from .base import Extractor
import requests


class SianetExtractor(Extractor):
    def __init__(self, base_url):
        self.base_url = base_url

    def extract_data(self, endpoint, params=None):
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        response.raise_for_status()
        return response.json()
