# 将数据插入向量数据库

import pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import os
os.environ["OPENAI_API_KEY"] = "xxx"
embeddings = OpenAIEmbeddings()

class PineconeDB():
    def __init__(self, key=None, environment=None, index=None):
        DEFAULTS = {
            "key": "ae091e8f-89d4-4c8e-bd2d-1e7315acf8b4",
            "environment": "us-central1-gcp",
            "index": "greyson"
        }
        self.key = key or DEFAULTS["key"]
        self.environment = environment or DEFAULTS["environment"]
        self.index = index or DEFAULTS["index"]
        self.pineconeIndex = self.creatPineconeIndex()

    def creatPineconeIndex(self):
        pinecone.init(api_key=self.key,environment=self.environment)
        index = pinecone.Index(self.index)
        return index

    def insert_data(self, data_list):
        self.pineconeIndex.upsert(data_list)


if __name__ == '__main__':
    import uuid
    p = PineconeDB()

    # 插入
    query = "我是孙狗，今年18岁"
    vec = embeddings.embed_query(query)
    data = {
        "id": uuid.uuid4().hex,
        "values": vec,
        "metadata": {
            "text": query,
        }
    }
    p.insert_data([data])