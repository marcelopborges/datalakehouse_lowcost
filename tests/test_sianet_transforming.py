import pytest
from google.cloud import storage
from dotenv import load_dotenv

load_dotenv()


def test_google_cloud_storage():
    storage_client = storage.Client()
    buckets = list(storage_client.list_buckets())
    try:
        assert len(buckets) > 0
        assert "mvp-hp-staging" in [bucket.name for bucket in buckets]
        assert "mvp-hp-transformed" in [bucket.name for bucket in buckets]
    except AssertionError:
        pytest.fail("Não foi possível conectar ao Google Cloud Storage")

