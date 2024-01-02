from datetime import timedelta, datetime
from elt.extractor.sianet_extractor import SianetExtractor
from dotenv import load_dotenv
import os

load_dotenv()


def run_elt_process(metodo, date):
    # today = datetime.now()
    # d1 = (today - timedelta(days=10)).strftime('%d/%m/%Y')
    sianet_extractor = SianetExtractor(base_url=os.getenv("SIANET_API_URL"), nome_dna=metodo)
    match metodo:
        case 'dna_kmRodado':
            raw_data = sianet_extractor.extract_km_rodado(date)
        case 'dna_linha':
            raw_data = sianet_extractor.extract_dna_linha(date)
        case 'dna_calendario':
            raw_data = sianet_extractor.extract_dna_calendar(date)
        case _:
            raise ValueError(f"Método desconhecido")
    return raw_data


if __name__ == "__main__":
    # for i in range(31):
    #     today = datetime.now()
    #     d1 = (today - timedelta(days=i)).strftime('%d/%m/%Y')
    #     run_elt_process(i)

    today = datetime.now()
    d1 = (today - timedelta(days=10)).strftime('%d/%m/%Y')
    # run_elt_process(d1)
    print(run_elt_process(metodo='dna_calendario', date=d1))