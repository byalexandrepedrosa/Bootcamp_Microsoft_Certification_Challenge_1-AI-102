import os
import streamlit as st

from azure.storage.blob import BlobServiceClient
from utils.config import config

def upload_blob(file, file_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(config.AZURE_STORAGE_CONNECTION_STRING)

        blob_client = blob_service_client.get_blob_client(container=config.CONTAINER_NAME, blob=file_name)

        blob_client.upload_blob(file, overwrite=True)

        return blob_client.url
    except Exception as e:
        st.error(f"Erro ao enviar o arquivo para o Azure Blob Storage: {e}")
        return None
