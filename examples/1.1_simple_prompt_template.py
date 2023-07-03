from dotenv import load_dotenv
load_dotenv()

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

prompt = PromptTemplate(template="Question: {question}\nAnswer:", input_variables=["question"])

llm = OpenAI(model_name="text-davinci-003", temperature=.9)
chain = LLMChain(llm=llm, prompt=prompt)

output = chain.run("What is the meaning of life for a surfer?")
print(output)


