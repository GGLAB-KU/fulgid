from langchain import HuggingFaceHub
from dotenv import load_dotenv
from langchain import PromptTemplate, LLMChain

load_dotenv()

repo_id = "Salesforce/codet5p-770m"

llm = HuggingFaceHub(repo_id=repo_id)

template = """{procedure}

I have the above procedural text. Create a python code for it which has different classes for the participants and their relationship with each other.
"""
prompt = PromptTemplate(template=template, input_variables=["procedure"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

procedure = """Erosion by the ocean:
1. Wind creates waves in the ocean. 
2. The waves wash onto the beaches. 
3. The waves hit rocks on the beach. 
4. Tiny parts of the rock break off.
5. The rocks become smaller."""

print(llm_chain.run(procedure))
