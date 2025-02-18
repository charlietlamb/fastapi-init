from weaviate.classes.config import Configure

def store_name(client):
    client.collections.create(
        name="Question",
        vectorizer_config=Configure.Vectorizer.text2vec_ollama(
            model="nomic-embed-text",
        ),
        generative_config=Configure.Generative.ollama(
            model="llama3.2",
        )
    )
