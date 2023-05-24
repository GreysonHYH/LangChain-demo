# 读取本地材料并做出总结

from langchain.document_loaders import UnstructuredFileLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "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"

# 导入文本
loader = UnstructuredFileLoader("/localData/local_material.txt")
# 将文本转成 Document 对象
document = loader.load()
print(f'documents:{len(document)}')

# 初始化文本分割器
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0
)

# 切分文本
split_documents = text_splitter.split_documents(document)
print(f'documents:{len(split_documents)}')

# 加载 llm 模型
llm = OpenAI()

# 创建总结链
chain = load_summarize_chain(llm, chain_type="refine", verbose=True)

# 执行总结链，（为了快速演示，只总结前5段）
print(chain.run(split_documents[:5]))