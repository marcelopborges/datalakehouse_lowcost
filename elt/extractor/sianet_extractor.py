import json

from .base import Extractor
import requests
from datetime import datetime, timedelta


class SianetExtractor(Extractor):
    def __init__(self, base_url, nome_dna):
        self.base_url = base_url
        self.nome_dna = nome_dna

    def extract_km_rodado(self, date):
        params = {
            'nomeDNA': self.nome_dna,
            'data': date
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        response = response.content.decode('utf-8')
        return json.loads(response)

    def extract_dna_linha(self, date):
        params = {
            'nomeDNA': self.nome_dna,
            'data_inicio': str(date),
            'data_final': str(date)
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        response = response.content.decode('utf-8')
        return json.loads(response)

    def extract_dna_calendar(self, date):
        params = {
            'nomeDNA': self.nome_dna,
            'data_inicio': str(date),
            'data_final': str(date)
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        response = response.content.decode('utf-8')
        return json.loads(response)

