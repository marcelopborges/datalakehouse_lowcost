import os
from datetime import timedelta, datetime, date
import pandas as pd
from dotenv import load_dotenv
from elt.extractor.sianet_extractor import SianetExtractor
from elt.convertion.sianet_convertion import Conversor
from elt.loading.gcp_connector import GCPStorageClient
from elt.transforming.sianet_tranforming import TransformingData
from google.cloud import bigquery
import subprocess
load_dotenv()


def run_elt_process(metodo, date_input):
    sianet_extractor = SianetExtractor(base_url=os.getenv("SIANET_API_URL"), nome_dna=metodo)
    match metodo:
        case 'dna_kmRodado':
            raw_data = sianet_extractor.extract_km_rodado(date_input)
        case 'dna_linha':
            raw_data = sianet_extractor.extract_dna_linha(date_input)
        case 'dna_calendario':
            raw_data = sianet_extractor.extract_dna_calendar(date_input)
        # case 'dna_passageirosTranspArcoSul':
        #     raw_data = sianet_extractor.extract_dna_passageirosTranspArcoSul(date_input)
        case _:
            raise ValueError(f"Método desconhecido")
    conversor = Conversor(metodo, raw_data, date_input)
    df = conversor.convert_data()
    data_in_memory, filename = conversor.save_raw_as_parquet(df, date_input)

    # Gerar caminho completo do arquivo no GCP
    full_path = gcp_path_staging(date_input, metodo, filename)
    storage_client = GCPStorageClient()
    bucket_staging_name = os.getenv("SIANET_BUCKET_STAGING")
    storage_client.upload_blob_from_memory(bucket_staging_name, full_path, data_in_memory.getvalue())

    bucket_transformed_name = os.getenv("SIANET_BUCKET_TRANSFORMED")
    df_nomes = ['km', 'carros', 'horarios'] if metodo == 'dna_kmRodado' else [metodo]

    df_transf = TransformingData(df, date_input, metodo).transforming_metodo()

    # Verifica se df_transf é um único DataFrame ou uma lista de DataFrames
    if isinstance(df_transf, pd.DataFrame):
        # Para um único DataFrame, cria uma lista com um único item
        df_transf = [df_transf]
        df_nomes = [metodo]
    elif isinstance(df_transf, list):
        # Para múltiplos DataFrames, ajusta os nomes conforme necessário
        if metodo == 'dna_kmRodado':
            df_nomes = ['km', 'carros', 'horarios']

    # Loop para processar cada DataFrame
    for df, df_nome in zip(df_transf, df_nomes):
        data_in_memory, filename = conversor.save_transf_as_parquet(df, date_input, df_nome)
        full_path = gcp_path_transforming(date_input, metodo, df_nome)
        storage_client.upload_blob_from_memory(bucket_transformed_name, full_path, data_in_memory.getvalue())
    return




def gcp_path_staging(date_input, metodo, filename):
    """
    Gera o caminho completo do arquivo para o upload no GCP com base na data, no método e no nome do arquivo.
    """
    date_obj = datetime.strptime(date_input, "%d/%m/%Y")
    ano = date_obj.strftime("%Y")
    mes = date_obj.strftime("%m")
    return f"{metodo}/{ano}/{mes}/{filename}"


def gcp_path_transforming(date_input, metodo, df_nome):
    date_obj = datetime.strptime(date_input, "%d/%m/%Y")
    ano = date_obj.strftime("%Y")
    mes = date_obj.strftime("%m")
    dia = date_obj.strftime("%d")
    if metodo == 'dna_kmRodado':
        folder = df_nome  # Aqui 'df_nome' será o nome do DataFrame específico (km, carros, horarios)
    elif metodo == 'dna_linha':
        folder = 'linha'
    elif metodo == 'dna_calendario':
        folder = 'calendario'
    elif metodo == 'dna_passageirosTranspArcoSul':
        folder = 'passageiros'
    else:
        raise ValueError(f"Método desconhecido")

    filename = f"{df_nome}_{ano}{mes}{dia}.parquet"
    return f"{folder}/{ano}/{mes}/{filename}"



if __name__ == "__main__":
    today = datetime.now()
    for _ in range(1):
        d1 = (today - timedelta(days=_ +2)).strftime('%d/%m/%Y')
        hour = datetime.now().time()
        print(f'inicio: {hour}')
        run_elt_process("dna_kmRodado", d1)
        hour = datetime.now().time()
        print(f'extração, transformação e carga do KM: {hour}')
        run_elt_process("dna_linha", d1)
        hour = datetime.now().time()
        print(f'extração, transformação e carga de Linhas: {hour}')
        run_elt_process("dna_calendario", d1)
        hour = datetime.now().time()
        print(f'extração, transformação e carga do Calendário: {hour}')
        # run_elt_process("dna_passageirosTranspArcoSul", d1)
    reprocessing_tables_gpc = [
        'bq load --source_format=PARQUET --replace dados_hp.km gs://mvp-hp-transformed/km/*.parquet',
        'bq load --source_format=PARQUET --replace dados_hp.tmp_carros gs://mvp-hp-transformed/carros/*.parquet',
        'bq load --source_format=PARQUET --replace dados_hp.tmp_horarios gs://mvp-hp-transformed/horarios/*.parquet',
        'bq load --source_format=PARQUET --replace dados_hp.tmp_linha gs://mvp-hp-transformed/linha/*.parquet',
        'bq load --source_format=PARQUET --replace dados_hp.calendario gs://mvp-hp-transformed/calendario/*.parquet'
    ]
    client = bigquery.Client()
    for command in reprocessing_tables_gpc:
        subprocess.run(command, shell=True, check=True)
    print('Todos os arquivos PARQUET foram carregados no BigQuery.')

