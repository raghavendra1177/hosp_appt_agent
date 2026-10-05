from tools.medical_tools import MedicalTools
from services.openai_llm import llm


class MedicalAgent:

    def __init__(self):
        self.medical_tools = MedicalTools()

    def execute(
        self,
        query: str
    ):

        # Try to retrieve supporting information
        try:
            search_results = (
                self.medical_tools.search(query)
            )
        except Exception:
            search_results = []

        # ---------------------------------
        # CASE 1: Search results available
        # ---------------------------------

        if search_results:

            context = "\n\n".join(
                search_results
            )

            prompt = f"""
You are a medical information assistant.

Use the supplied context to answer the
user's question.

Do not diagnose the patient.

Question:
{query}

Context:
{context}

Provide, when relevant:

1. Summary
2. Symptoms
3. Causes
4. Treatments
5. Prevention

Keep the response clear and concise.

Answer:
"""

            answer = llm.invoke(prompt)

            return {
                "answer": answer,
                "sources":
                    self.medical_tools.get_sources()
            }

        # ---------------------------------
        # CASE 2: No search results
        # ---------------------------------

        prompt = f"""
You are a medical information assistant.

Answer the following general medical
information question using your medical
knowledge.

Do not diagnose the user.

Explain that the information is educational
and not a substitute for professional
medical advice when appropriate.

Question:
{query}

Provide, when relevant:

1. Summary
2. Symptoms
3. Causes
4. Treatments
5. Prevention

Keep the answer clear and concise.

Answer:
"""

        answer = llm.invoke(prompt)

        return {
            "answer": answer,
            "sources": []
        }