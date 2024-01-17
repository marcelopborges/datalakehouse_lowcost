from google.cloud import storage
import logging
from dotenv import load_dotenv

load_dotenv()


class GCPStorageClient:
    def __init__(self):
        # Configuração do logging
        self.logger = logging.getLogger('GCPStorageClient')
        logging.basicConfig(level=logging.INFO)

        try:
            # Criação do cliente de armazenamento
            self.storage_client = storage.Client()
            self.logger.info("Cliente do Google Cloud Storage inicializado com sucesso.")
        except Exception as e:
            self.logger.error(f"Erro ao inicializar o cliente do Google Cloud Storage: {e}")
            raise

    def upload_blob_from_memory(self, bucket_name, destination_blob_name, data):
        try:
            bucket = self.storage_client.bucket(bucket_name)
            blob = bucket.blob(destination_blob_name)

            if isinstance(data, bytes):
                blob.upload_from_string(data, content_type='application/octet-stream')
            else:
                self.logger.error("Tipo de dados não suportado para upload.")
        except Exception as e:
            self.logger.error(f"Erro ao fazer upload do arquivo: {e}")
            raise

