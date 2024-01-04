import os
import pandas as pd
from datetime import datetime


class Transformer:
    def __init__(self, nome_dna, raw_data):
        self.raw_data = raw_data
        self.nome_dna = nome_dna
        self.today = datetime.today().strftime('%Y%m%d')

    def convert_data(self):
        """
        Verifica o dado de entrada, converte para um dataframe pandas e chama a função para converter para parquet.
        :return: o caminho do arquivo gerado já no formato parquet.
        """
        if not isinstance(self.raw_data, dict) or 'dados' not in self.raw_data:
            raise ValueError("Formato JSON inválido ou chave 'dados' não encontrada")
        df = pd.DataFrame(self.raw_data['dados'])
        parquet_file_path = self.save_as_parquet(df)
        return parquet_file_path

    def save_as_parquet(self, df):
        """
        Verifica se o ditorio 'tmp' existe, senão cria.
        Monta o arquivo e converte como parquet
        """
        if not os.path.exists('tmp'):
            os.makedirs('tmp')
        file_path = os.path.join('tmp', f'{self.nome_dna}_{self.today}.parquet')
        df.to_parquet(file_path)
        return file_path