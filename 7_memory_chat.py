# 拥有记忆的聊天

import os
os.environ["OPENAI_API_KEY"] = "xxx"

from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryBufferMemory


class Chat(object):
    
    def __init__(self) -> None:
         self.session_state = dict()

    def get_response(self,query:str,uid: str)->str:
        chain = self.get_pro_chain(uid) 
        response = chain({"human_input": query})
        return response.get("output_text").strip()

    def get_pro_chain(self,uid: str):
        return load_qa_chain(
            llm=ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0.9,max_tokens=1024),
            chain_type="stuff",
            memory=self.get_memory(uid)
        )

    def get_memory(self,uid: str) -> ConversationSummaryBufferMemory:
        memory_name = f"memory_{uid}"
        if memory_name not in self.session_state:
            self.session_state[memory_name] = self.new_memory(uid)
        return self.session_state[memory_name]

    def new_memory(self,uid: str) -> ConversationSummaryBufferMemory:
        memory = ConversationSummaryBufferMemory(
            llm=ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0.9,max_tokens=1024),
            memory_key=f"chat_history_{uid}",
            input_key="human_input",
            max_token_limit=1000,
        )
        return memory

