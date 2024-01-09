from datetime import datetime

import pandas as pd
import pytest
from elt.transformer.sianet_transformer import Transformer
from unittest.mock import patch
import os


@pytest.fixture
def example_data():
    return {
        "dados": [
            {"coluna1": 1, "coluna2": 2},
            {"coluna1": 3, "coluna2": 4}
        ]
    }

@pytest.fixture
def date():
    return datetime.strptime('02/01/2024', '%d/%m/%Y').strftime('%d/%m/%Y')


def test_convert_data_with_valid_input(example_data, date):
    transformer = Transformer("test_dna", example_data, date)
    result = transformer.convert_data()

    # Cria um DataFrame a partir de example_data['dados'] para a comparação
    expected_dataframe = pd.DataFrame(example_data['dados'])

    assert not result.empty
    assert result.equals(expected_dataframe)
