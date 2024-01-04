import os
from datetime import timedelta, datetime, date
from dotenv import load_dotenv
from elt.extractor.sianet_extractor import SianetExtractor
from elt.transformer import Transformer

load_dotenv()


def run_elt_process(metodo, date):
    sianet_extractor = SianetExtractor(base_url=os.getenv("SIANET_API_URL"), nome_dna=metodo)
    match metodo:
        case 'dna_kmRodado':
            raw_data = sianet_extractor.extract_km_rodado(date)
        case 'dna_linha':
            raw_data = sianet_extractor.extract_dna_linha(date)
        case 'dna_calendario':
            raw_data = sianet_extractor.extract_dna_calendar(date)
        case 'dna_passageirosTranspArcoSul':
            raw_data = sianet_extractor.extract_dna_passageirosTranspArcoSul(date)
        case _:
            raise ValueError(f"Método desconhecido")
    transformer = Transformer(metodo, raw_data, date)
    transformed_data = transformer.convert_data()
    return transformed_data


if __name__ == "__main__":
    today = (date(2023, 4, 19))
    for _ in range(141):
        # today = datetime.now()

        d1 = (today - timedelta(days=_ )).strftime('%d/%m/%Y')
        run_elt_process("dna_kmRodado", d1)
        print(f"dna_kmRodado {d1}")
        run_elt_process("dna_linha", d1)
        print(f"dna_linha {d1}")
        run_elt_process("dna_calendario", d1)
        print(f"dna_calendario {d1}")
        run_elt_process("dna_passageirosTranspArcoSul", d1)
        print(f"dna_passageirosTranspArcoSul {d1}")
    print("--------FINALIZADO--------")