# https://dev.to/0xkoji/use-bard-api-164i
import os
from bardapi import Bard
from dotenv import load_dotenv


load_dotenv()

token = os.environ['COOKIE_TOKEN']
bard = Bard(token = token)
response = bard.get_answer("What is a LLM?")['content']
print(response)