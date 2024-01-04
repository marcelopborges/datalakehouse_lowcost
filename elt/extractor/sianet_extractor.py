import json
import os
from base64 import b64encode
from .base import Extractor
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

token_data = {
    "token": None,
    "expiry": None
}


class SianetExtractor(Extractor):

    def __init__(self, base_url, nome_dna):
        self.base_url = base_url
        self.nome_dna = nome_dna
        self.token, self.token_expiry = self.get_auth_token()

    def get_auth_token(self):
        global token_data
        current_time = datetime.now()
        if token_data["token"] and token_data["expiry"] > current_time:
            return token_data["token"]
        auth_url = os.getenv("SIANET_AUTH_URL")
        username = os.getenv("SIANET_USERNAME")
        password = os.getenv("SIANET_PASSWORD")
        # Codifica as credenciais em base64 para Basic Auth
        credentials = f"{username}:{password}"
        token = b64encode(credentials.encode()).decode('utf-8')
        headers = {
            'Authorization': f'Basic {token}'
        }
        response = requests.post(auth_url,  headers=headers)
        response.raise_for_status()
        token_info = response.json()
        if not token_info["sucesso"]:
            raise Exception("Falha na autenticação com o sianet.")
        token_data["token"] = token_info["token"]
        token_data["expiry"] = datetime.strptime(token_info["fim"], "%d/%m/%Y %H:%M:%S")
        return token_data["token"], token_data["expiry"]

    def is_token_expired(self):
        return datetime.now() >= self.token_expiry

    def get_headers(self):
        if self.is_token_expired():
            self.token, self.token_expiry = self.get_auth_token()
        return {"Authorization": f"Bearer {self.token}"}

    def extract_km_rodado(self, date):
        url = f'http://siannet.gestaosian.com/api/BI_Extrator?nomeDNA={self.nome_dna}&data={date}'
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f'Erro na requisição {self.nome_dna}: {response.status_code}')
        return response.json()

    def extract_dna_linha(self, date):
        url = f'http://siannet.gestaosian.com/api/BI_Extrator?data_inicio={date}&data_final={date}&nomeDNA={self.nome_dna}'
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f'Erro na requisição {self.nome_dna}: {response.status_code}')
        return response.json()

    def extract_dna_calendar(self, date):
        url = f'http://siannet.gestaosian.com/api/BI_Extrator?data_inicio={date}&data_final={date}&nomeDNA={self.nome_dna}'
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        if response.status_code != 200:
            raise Exception(f'Erro na requisição: {response.status_code}')
        return response.json()

    def extract_dna_passageirosTranspArcoSul(self, date):
        url = f'http://siannet.gestaosian.com/api/BI_Extrator?nomeDNA={self.nome_dna}&data={date}'
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        if response.status_code != 200:
            raise Exception(f'Erro na requisição {self.nome_dna}: {response.status_code}')
        return response.json()