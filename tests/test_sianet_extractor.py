from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock
import pytest
from elt.extractor.sianet_extractor import SianetExtractor

@pytest.fixture
def mock_auth_token():
    with patch("elt.extractor.sianet_extractor.SianetExtractor.get_auth_token",
               return_value=("fake_token", datetime.now() + timedelta(minutes=30))):
        yield


@patch("requests.get")
def test_sianet_extractor_data_dna_km_rodado(mock_get, mock_auth_token):
    test_date = '01/01/2023'
    expected_response_data = {'result': 'success'}
    name_dna = 'dna_kmRodado'
    expected_url = f'http://siannet.gestaosian.com/api/BI_Extrator?nomeDNA={name_dna}&data={test_date}'
    expected_headers = {'Authorization': 'Bearer fake_token'}

    response_mock = MagicMock()
    response_mock.status_code = 200
    response_mock.json.return_value = expected_response_data
    mock_get.return_value = response_mock

    sianet_extractor = SianetExtractor(base_url='http://siannet.gestaosian.com/api/BI_Extrator', nome_dna=name_dna)
    actual_response = sianet_extractor.extract_km_rodado(test_date)

    mock_get.assert_called_once_with(expected_url, headers=expected_headers)
    assert actual_response == expected_response_data
    assert 'Authorization' in mock_get.call_args.kwargs['headers']


@patch("requests.get")
def test_extract_dna_linha(mock_get, mock_auth_token):
    test_date = '01/01/2023'
    expected_response_data = {'result': 'success'}
    name_dna = 'dna_linha'
    expected_url = f'http://siannet.gestaosian.com/api/BI_Extrator?data_inicio={test_date}&data_final={test_date}&nomeDNA={name_dna}'
    expected_headers = {'Authorization': 'Bearer fake_token'}

    response_mock = MagicMock()
    response_mock.status_code = 200
    response_mock.json.return_value = expected_response_data
    mock_get.return_value = response_mock

    sianet_extractor = SianetExtractor(base_url='http://siannet.gestaosian.com/api/BI_Extrator', nome_dna=name_dna)
    actual_response = sianet_extractor.extract_dna_linha(test_date)

    mock_get.assert_called_once_with(expected_url, headers=expected_headers)
    assert actual_response == expected_response_data
    assert 'Authorization' in mock_get.call_args.kwargs['headers']


@patch("requests.get")
def test_extract_dna_calendar(mock_get, mock_auth_token):
    test_date = '01/01/2023'
    expected_response_data = {'result': 'success'}
    name_dna = 'dna_calendario'
    expected_url = f'http://siannet.gestaosian.com/api/BI_Extrator?data_inicio={test_date}&data_final={test_date}&nomeDNA={name_dna}'
    expected_headers = {'Authorization': 'Bearer fake_token'}

    response_mock = MagicMock()
    response_mock.status_code = 200
    response_mock.json.return_value = expected_response_data
    mock_get.return_value = response_mock

    sianet_extractor = SianetExtractor(base_url='http://siannet.gestaosian.com/api/BI_Extrator', nome_dna=name_dna)
    actual_response = sianet_extractor.extract_dna_calendar(test_date)

    mock_get.assert_called_once_with(expected_url, headers=expected_headers)
    assert actual_response == expected_response_data
    assert 'Authorization' in mock_get.call_args.kwargs['headers']


@patch("requests.get")
def test_extract_dna_passageirosTranspArcoSul(mock_get, mock_auth_token):
    test_date = '01/01/2023'
    expected_response_data = {'result': 'success'}
    name_dna = 'dna_passageirosTranspArcoSul'
    expected_url = f'http://siannet.gestaosian.com/api/BI_Extrator?nomeDNA={name_dna}&data={test_date}'
    expected_headers = {'Authorization': 'Bearer fake_token'}

    response_mock = MagicMock()
    response_mock.status_code = 200
    response_mock.json.return_value = expected_response_data
    mock_get.return_value = response_mock

    sianet_extractor = SianetExtractor(base_url='http://siannet.gestaosian.com/api/WSLogin', nome_dna=name_dna)
    actual_response = sianet_extractor.extract_dna_passageirosTranspArcoSul(test_date)

    mock_get.assert_called_once_with(expected_url, headers=expected_headers)
    assert actual_response == expected_response_data
    assert 'Authorization' in mock_get.call_args.kwargs['headers']