#检索向量数据库中，从中得出问题参考了哪些数据

import pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import os
os.environ["OPENAI_API_KEY"] = "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"
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

    def query_data(self, vec):
        q = self.pineconeIndex.query(
            vector=vec,
            top_k=3,
            include_values=False,
            include_metadata=True,
        )
        for i in range(len(q['matches'])):
            print(f"id:{q['matches'][i]['id']},score:{q['matches'][i]['score']},data:{q['matches'][i]['metadata']}")
        return q


if __name__ == '__main__':
    p = PineconeDB()

    # 查询
    query = "孙狗出来一下"
    vec = embeddings.embed_query(query)
    answer = p.query_data(vec)
    print(answer)
