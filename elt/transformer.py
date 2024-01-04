import json
import os
import pandas as pd
from datetime import datetime
import io

class Transformer:
    def __init__(self, nome_dna, raw_data):
        self.raw_data = raw_data
        self.nome_dna = nome_dna
        self.today = datetime.today().strftime('%Y%m%d')

    def convert_data(self):
        # Verifica se os dados estão no formato esperado
        if not isinstance(self.raw_data, dict) or 'dados' not in self.raw_data:
            raise ValueError("Formato JSON inválido ou chave 'dados' não encontrada")

        # Converte os dados JSON para DataFrame
        df = pd.DataFrame(self.raw_data['dados'])

        # Salva o DataFrame como um arquivo Parquet
        parquet_file_path = self.save_as_parquet(df)

        return parquet_file_path

    def save_as_parquet(self, df):
        # Verifica se o diretório 'tmp' existe, se não, cria
        if not os.path.exists('tmp'):
            os.makedirs('tmp')

        # Monta o caminho do arquivo Parquet
        file_path = os.path.join('tmp', f'{self.nome_dna}_{self.today}.parquet')

        # Salva o DataFrame como Parquet
        df.to_parquet(file_path)

        return file_path