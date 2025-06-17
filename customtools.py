from langchain.agents import Tool
from openai import OpenAI
from bs4 import BeautifulSoup
from io import BytesIO
import base64
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

my_key_openai = os.getenv("OPENAI_KEY")
my_key_stabilityai = os.getenv("STABILITYAI_KEY")

client = OpenAI(
    api_key=my_key_openai,
)