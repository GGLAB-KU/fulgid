from langchain import HuggingFaceHub
from dotenv import load_dotenv
from langchain import PromptTemplate, LLMChain


load_dotenv()

repo_id = "google/flan-t5-xl"

llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature": 0, "max_length": 64})


template = """Question: {question}

Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "Who won the FIFA World Cup in the year 1994? "

print(llm_chain.run(question))
