from openai import OpenAI

from config.settings import (
    OPENAI_API_KEY,
    HOSP_MODEL
)


class OpenAILLM:

    def __init__(self):

        if not OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY not found in .env"
            )

        if not HOSP_MODEL:
            raise ValueError(
                "HOSP_MODEL not found in .env"
            )

        self.client = OpenAI(
            api_key=OPENAI_API_KEY
        )

        self.model = HOSP_MODEL

    def invoke(
        self,
        prompt: str,
        max_tokens: int = 1000
    ) -> str:

        try:

            response = self.client.responses.create(
                model=self.model,
                instructions=(
                    "You are a hospital medical information "
                    "assistant. Provide clear, accurate and "
                    "helpful information. Do not claim to "
                    "diagnose a patient."
                ),
                input=prompt,
                max_output_tokens=max_tokens
            )

            return response.output_text

        except Exception as ex:

            return (
                f"OpenAI API Error: {str(ex)}"
            )


llm = OpenAILLM()