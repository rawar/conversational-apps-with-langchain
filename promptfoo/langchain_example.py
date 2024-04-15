import json
import sys
import os
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chains import LLMMathChain
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")
llm = AzureChatOpenAI(
    openai_api_version="2023-05-15",
    azure_deployment="gpt-4",
)
llm_math = LLMMathChain(llm=llm, verbose=True)


prompt = sys.argv[1]
provider_options = json.loads(sys.argv[2])
test_context = json.loads(sys.argv[3])

# print("Vars: ", test_context['vars'])

llm_math.run(prompt)
