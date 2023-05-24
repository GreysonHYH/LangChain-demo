# 1_完成一次问答

import os
os.environ["OPENAI_API_KEY"] = "xxx"
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)

text = "why elon musk is so smart?"
print(llm(text))