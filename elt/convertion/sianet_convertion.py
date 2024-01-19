from io import BytesIO
import pandas as pd


class Conversor:
    def __init__(self, nome_dna, raw_data, date):
        self.raw_data = raw_data
        self.nome_dna = nome_dna
        self.date = date

    def convert_data(self):
        """
        Verifica o dado de entrada, converte para um dataframe pandas e chama a função para converter para parquet.
        :return: o caminho do arquivo gerado já no formato parquet.
        """
        if isinstance(self.raw_data, dict) and 'dados' in self.raw_data:
            df = pd.DataFrame(self.raw_data['dados'])
        else:
            raise ValueError("Formato de raw_data não suportado ou chave 'dados' não encontrada.")

        return df

    def save_raw_as_parquet(self, df, date):
        output = BytesIO()
        df.to_parquet(output, index=False)
        output.seek(0)  # Retorna ao início do stream

        date_str = pd.to_datetime(date, dayfirst=True).strftime("%Y%m%d")
        filename = f"{self.nome_dna}_{date_str}.parquet"
        return output, filename


    def save_transf_as_parquet(self, df, date, filename_prefix):
        output = BytesIO()
        df.to_parquet(output, index=False)
        output.seek(0)  # Retorna ao início do stream

        date_str = pd.to_datetime(date, dayfirst=True).strftime("%Y%m%d")
        filename = f"{filename_prefix}_{date_str}.parquet"
        return output, filename

