import json

import pytest
from unittest.mock import patch, MagicMock
from elt.extractor.sianet_extractor import SianetExtractor


@pytest.fixture
def sianet_extractor():
    return SianetExtractor(base_url="https://fakeapi.com/", nome_dna='dna_fake')


def test_sianet_extractor_data_dna_km_rodado():
    test_date = '01/01/2023'
    test_params = {
        'nomeDNA': 'dna_fake',
        'data': test_date
    }

    response_data = {'result': 'success'}
    response_json = json.dumps(response_data)
    response_mock = MagicMock()
    response_mock.content.decode.return_value = response_json

    with patch('elt.extractor.sianet_extractor.requests.get', return_value=response_mock) as mock_get:
        sianet_extractor = SianetExtractor(base_url='https://fakeapi.com/data', nome_dna='dna_fake')
        data = sianet_extractor.extract_km_rodado(date=test_date)
        mock_get.assert_called_once_with(f'https://fakeapi.com/data', params=test_params)
        assert data == response_data


def test_extract_dna_linha(sianet_extractor):
    date = '01/01/2023'
    test_params = {
        'nomeDNA': 'dna_fake',
        'data_inicio': date,
        'data_final': date
    }

    response_data = {'result': 'success for dna_linha'}
    response_json = json.dumps(response_data)
    response_mock = MagicMock()
    response_mock.content.decode.return_value = response_json

    with patch('elt.extractor.sianet_extractor.requests.get', return_value=response_mock) as mock_get:
        data = sianet_extractor.extract_dna_linha(date)
        mock_get.assert_called_once_with(f'https://fakeapi.com/', params=test_params)
        assert data == response_data


def test_extract_dna_calendar(sianet_extractor):
    date = '01/01/2023'
    test_params = {
        'nomeDNA': 'dna_fake',
        'data_inicio': date,
        'data_final': date
    }

    response_data = {'result': 'success for dna_linha'}
    response_json = json.dumps(response_data)
    response_mock = MagicMock()
    response_mock.content.decode.return_value = response_json

    with patch('elt.extractor.sianet_extractor.requests.get', return_value=response_mock) as mock_get:
        data = sianet_extractor.extract_dna_calendar(date)
        mock_get.assert_called_once_with(f'https://fakeapi.com/', params=test_params)
        assert data == response_data



