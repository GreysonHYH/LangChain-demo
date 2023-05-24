# 根据导入的数据 完成一次回答

import os
os.environ["OPENAI_API_KEY"] = "xxx"
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
from langchain.vectorstores import Pinecone

class Chat(object):

    # 提问，获取回答
    def get_response(self,query:str)->str:
        chain = self.get_pro_chain()
        response = chain({"input_documents": self.get_documents(query),"human_input": query}, return_only_outputs=True)
        return response.get("output_text").strip()

    # 新建一条大语言模型交互链 
    def get_pro_chain(self):
        return load_qa_chain(
            llm=ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0.9,max_tokens=1024),
            chain_type="stuff",
        )

    # 检索向量数据库，获取检索到的数据
    def get_documents(self,query):
        docsearch = self.load_vector_store()
        return docsearch.similarity_search(query)

    # 获取向量数据库
    def load_vector_store(self) -> Pinecone:
        print("Loading vector store...")

        pinecone.init(
            api_key="ae091e8f-89d4-4c8e-bd2d-1e7315acf8b4",
            environment="us-central1-gcp",
        )

        index_name = "greyson"
        embeddings = OpenAIEmbeddings()

        docsearch = Pinecone.from_existing_index(index_name, embeddings)
        
        print("Loaded vector store")
        return docsearch

