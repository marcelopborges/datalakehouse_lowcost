import os
import pandas as pd
from datetime import datetime


class Transformer:
    def __init__(self, nome_dna, raw_data, date):
        self.raw_data = raw_data
        self.nome_dna = nome_dna
        self.date = date

    def convert_data(self):
        """
        Verifica o dado de entrada, converte para um dataframe pandas e chama a função para converter para parquet.
        :return: o caminho do arquivo gerado já no formato parquet.
        """
        if not isinstance(self.raw_data, dict) or 'dados' not in self.raw_data:
            return pd.DataFrame()
        df = pd.DataFrame(self.raw_data['dados'])
        parquet_file_path = self.save_as_parquet(df, date=self.date)
        return parquet_file_path

    def save_as_parquet(self, df, date):
        """
        Verifica se o ditorio 'tmp' existe, senão cria.
        Monta o arquivo e converte como parquet
        """
        date_obj = datetime.strptime(date,"%d/%m/%Y")
        date_filename = date_obj.strftime("%d%m%Y")
        if not os.path.exists('../tmp'):
            os.makedirs('../tmp')
        file_path = os.path.join('../tmp', f'{self.nome_dna}_{date_filename}.parquet')
        df.to_parquet(file_path)
        return file_path