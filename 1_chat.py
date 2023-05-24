# 1_完成一次问答

import os
os.environ["OPENAI_API_KEY"] = "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"
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)

text = "why elon musk is so smart?"
print(llm(text))