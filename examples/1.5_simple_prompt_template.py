from dotenv import load_dotenv
load_dotenv()

from langchain import LLMChain, PromptTemplate
from langchain.llms import OpenAI

# Before executing the following code, make sure to have
# your OpenAI key saved in the “OPENAI_API_KEY” environment variable.
llm = OpenAI(model_name="text-davinci-003", temperature=0)

template = """Answer the question based on the context below. If the
question cannot be answered using the information provided, answer
with "I don't know".
Context: Quantum computing is an emerging field that leverages quantum mechanics to solve complex problems faster than classical computers.
...
Question: {query}
Answer: """

prompt_template = PromptTemplate(
    input_variables=["query"],
    template=template
)

# Create the LLMChain for the prompt
chain = LLMChain(llm=llm, prompt=prompt_template)

# Set the query you want to ask
input_data = {"query": "What is the main advantage of quantum computing over classical computing?"}

# Run the LLMChain to get the AI-generated answer
response = chain.run(input_data)

print("Question:", input_data["query"])
print("Answer:", response)