import os
from datetime import timedelta, datetime, date
from dotenv import load_dotenv
from elt.extractor.sianet_extractor import SianetExtractor
from elt.transformer.sianet_transformer import Transformer
from elt.loading.gcp_connector import GCPStorageClient

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
        case 'dna_passageirosTranspArcoSul':
            raw_data = sianet_extractor.extract_dna_passageirosTranspArcoSul(date_input)
        case _:
            raise ValueError(f"Método desconhecido")
    transformer = Transformer(metodo, raw_data, date_input)
    df = transformer.convert_data()
    data_in_memory, filename = transformer.save_as_parquet(df, date_input)

    # Gerar caminho completo do arquivo no GCP
    full_path = get_gcp_path(date_input, metodo, filename)

    storage_client = GCPStorageClient()
    bucket_name = os.getenv("SIANET_BUCKET_NAME")
    storage_client.upload_blob_from_memory(bucket_name, full_path, data_in_memory.getvalue())
    return print(f"Os dados do dia {date_input} do {metodo} foi enviado com sucesso")


def get_gcp_path(date_input, metodo, filename):
    """
    Gera o caminho completo do arquivo para o upload no GCP com base na data, no método e no nome do arquivo.
    """
    date_obj = datetime.strptime(date_input, "%d/%m/%Y")
    ano = date_obj.strftime("%Y")
    mes = date_obj.strftime("%m")
    return f"{metodo}/{ano}/{mes}/{filename}"


if __name__ == "__main__":
    today = (date(2022, 5, 4))
    for _ in range(854):
        # today = datetime.now()
        d1 = (today - timedelta(days=_ )).strftime('%d/%m/%Y')
        run_elt_process("dna_kmRodado", d1)
        run_elt_process("dna_linha", d1)
        run_elt_process("dna_calendario", d1)
        run_elt_process("dna_passageirosTranspArcoSul", d1)
