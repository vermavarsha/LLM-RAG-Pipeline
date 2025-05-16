import requests
from langchain.schema import Embeddings

class GeminiEmbeddings(Embeddings):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.endpoint = "https://gemini.api.endpoint/embeddings"  # Replace with actual URL

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        # Call Gemini API to get embeddings for a list of texts
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.post(
            self.endpoint,
            json={"texts": texts},
            headers=headers
        )
        response.raise_for_status()
        embeddings = response.json()["embeddings"]
        return embeddings

    def embed_query(self, text: str) -> list[float]:
        # Call Gemini API for a single query embedding
        return self.embed_documents([text])[0]
