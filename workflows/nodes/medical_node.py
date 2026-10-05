from typing import Any, Dict

from agents.medical_agent import MedicalAgent


medical_agent = MedicalAgent()


def medical_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Execute Medical RAG Agent.
    """

    try:
        query = state.get("user_query", "")

        if not query:
            raise ValueError("user_query missing from state")

        result = medical_agent.execute(query)

        if isinstance(result, dict):
            state["response"] = result.get(
                "answer",
                "No answer returned."
            )

            state["sources"] = result.get(
                "sources",
                []
            )

        else:
            state["response"] = str(result)
            state["sources"] = []

        return state

    except Exception as ex:
        state["response"] = (
            f"Medical Agent Error: {str(ex)}"
        )

        state["sources"] = []

        return state
