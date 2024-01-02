import pytest
from elt.loader import Loader
from elt.extractor.sianet_contracts import expected_columns


def test_loader_create_dataframe():
    loader = Loader()
    raw_data ={
            "PREFIXO_CARRO": "20144",
            "ID_EQUIPAMENTO": "911",
            "DATA": "28/12/2023",
            "ID_LINHA": "-2",
            "DS_TIPO_CHASSI": "17-230 EOD",
            "DS_TIPO_MOTOR": "MWM 6.12 TCAE-EURO III",
            "DS_TIPO_CAMBIO": "MANUAL",
            "CARRO_AUXILIAR": "NAO",
            "FX_HORARIA": "REAB",
            "FX_SIGLA": "REAB",
            "FX_NOME": "REAB",
            "KM_OCIOSA": "235",
            "LITROS_LINHA": "72,1",
            "KM_LINHA": "235",
            "ABS_CARRO_KM_TOTAL_DIA": "235",
            "ABS_CARRO_LITROS_TOTAL_DIA": "72,1"
        }
    dataframe = loader.load_to_dataframe(raw_data)
    for column in expected_columns:
        assert column in dataframe.columns