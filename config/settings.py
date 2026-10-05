import os
from dotenv import load_dotenv

load_dotenv()


OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)

HOSP_MODEL = os.getenv(
    "HOSP_MODEL",
    "gpt-6-luna"
)