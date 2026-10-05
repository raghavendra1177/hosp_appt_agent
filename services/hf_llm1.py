from huggingface_hub import InferenceClient

from config.settings import (
    HOSP_MODEL,
    HF_API_KEY
)


class HFLLM:

    def __init__(self):

        if not HF_API_KEY:
            raise ValueError(
                "HF_API_KEY not found in .env"
            )

        if not HOSP_MODEL:
            raise ValueError(
                "HF_MODEL not found in .env"
            )

        self.client = InferenceClient(
            provider="hf-inference",
            api_key=HF_API_KEY
        )

        self.model = HOSP_MODEL

    def invoke(
        self,
        prompt: str,
        max_tokens: int = 1000
    ) -> str:

        try:

            response = self.client.chat_completion(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a hospital assistant. "
                            "Provide accurate and helpful "
                            "healthcare information."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=max_tokens
            )

            if not response.choices:
                return "No response received from the model."

            return (
                response
                .choices[0]
                .message
                .content
            )

        except Exception as ex:

            return (
                f"HuggingFace API Error: "
                f"{str(ex)}"
            )


llm = HFLLM()