# Import necessary modules
from dotenv import load_dotenv
from langchain import PromptTemplate, FewShotPromptTemplate, LLMChain
from langchain.llms import OpenAI

# Load .env variables
load_dotenv()

# Initialize OpenAI's language model
# Explicit variable naming can increase code readability
language_model = OpenAI(model_name="text-davinci-003", temperature=0)

# Define examples as a constant
# Constants are usually declared at the top of the file and have all capital letters
EXAMPLES = [
    {"color": "red", "emotion": "passion"},
    {"color": "blue", "emotion": "serenity"},
    {"color": "green", "emotion": "tranquility"},
]

# Define template for formatting examples
# Moved the newline to make it clearer, it is part of the template
example_formatter_template = """Color: {color}
Emotion: {emotion}
"""

# Define the prompt template based on the formatter
example_prompt = PromptTemplate(
    input_variables=["color", "emotion"],
    template=example_formatter_template,
)

# Define a few shot prompt template, using the examples and the example prompt defined above
# This template also includes a prefix, a suffix, input variables, and an example separator
few_shot_prompt = FewShotPromptTemplate(
    examples=EXAMPLES,
    example_prompt=example_prompt,
    prefix="Here are some examples of colors and the emotions associated with them:\n\n",
    suffix="\n\nNow, given a new color, identify the emotion associated with it:\n\nColor: {input}\nEmotion:",
    input_variables=["input"],
    example_separator="\n",
)

# Use the template to format a new prompt
formatted_prompt = few_shot_prompt.format(input="purple")

# Create an LLMChain using the formatted prompt and the language model
# This sets up the chain to use the model and prompt together
chain = LLMChain(llm=language_model, prompt=PromptTemplate(template=formatted_prompt, input_variables=[]))

# Run the LLMChain to get the model's response
# This is the output from the AI model, corresponding to the emotion for the input color
response = chain.run({})

# Print the results
print("Color: purple")
print("Emotion:", response)
