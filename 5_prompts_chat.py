#根据提示词完成回答。

import os
os.environ["OPENAI_API_KEY"] = "xxx"

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
llm = OpenAI(temperature=0.9)

top_temp = """
    你回答时不要返回对话记录。 
    回答内容尽量简洁。
    你是人类。你是马斯克，你的回答都要遵循马斯克的风格。
"""
template = (
    top_temp + "\n\n"
    "=====BEGIN DOCUMENT=====\n"
    "{context}\n"
    "=====END DOCUMENT=====\n\n"
    "=====BEGIN CONVERSATION=====\n"
    "Human: {human_input}\n"
    "AI:"
)
prompt = PromptTemplate(
    input_variables=["human_input", "context"],
    template=template
)

print(llm(prompt.format(human_input="你是谁？你最喜欢哪个国家？",context="你最喜欢的国家是中国")))