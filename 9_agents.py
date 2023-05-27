import requests
from langchain import OpenAI
from langchain.agents import initialize_agent, load_tools, Tool
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.tools import DuckDuckGoSearchRun

OPENAI_API_KEY = "sk-..."
llm = OpenAI(
    openai_api_key=OPENAI_API_KEY,
    temperature=0.8,
    model_name="text-davinci-003"
)

prompt = PromptTemplate(
  input_variables=["query"],
  template="You are New Native Internal Bot. Help users with their important tasks, like a professor in a particular field. Query: {query}"
)

llm_chain = LLMChain(llm=llm, prompt=prompt)


# 算数学题工具
class WA:
  def __init__(self, app_id):
    self.url = f"http://api.wolframalpha.com/v1/result?appid={app_id}&i="

  def run(self, query):
    query = query.replace("+", " plus ").replace("-", " minus ")
    result = requests.post(f"{self.url}{query}")

    if not result.ok:
      raise Exception("Cannot call WA API.")

    return result.text
  
WA_API_KEY = "<WA_API_KEY>"
wa = WA(app_id=WA_API_KEY)

wa_tool = Tool(
    name="Wolfram|Alpha API",
    func=wa.run,
    description="Wolfram|Alpha API. It's super powerful Math tool. Use it for simple & complex math tasks."
)

# 在线搜索工具
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name = "Web Search",
    func=search.run,
    description="A useful tool for searching the Internet to find information on world events, issues, etc. Worth using for general topics. Use precise questions."
)

agent = initialize_agent(
    agent="zero-shot-react-description",
    tools=[wa_tool, search_tool],
    llm=llm,
    verbose=True,
    max_iterations=3
)

question_1 = agent("how much is bitcoin price right now??")
print(question_1['output'])

question_2 = agent("Integral of x * (log(x)^2)")
print(question_2['output'])