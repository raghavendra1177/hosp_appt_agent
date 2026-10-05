from typing import Any, Dict

from agents.writer_agent import WriterAgent


writer_agent = WriterAgent()


def writer_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Execute Writer Agent tools and store results in state.
    """

    try:
        tool_name = state.get("tool_name")

        if not tool_name:
            raise ValueError("tool_name missing from state")

        tool_params = state.get("tool_params", {})

        if not isinstance(tool_params, dict):
            raise ValueError("tool_params must be a dictionary")

        result = writer_agent.execute(
            tool_name,
            **tool_params
        )

        state["tool_output"] = result

        state["response"] = (
            f"Writer tool '{tool_name}' executed successfully."
        )

        return state

    except Exception as ex:
        state["tool_output"] = {}

        state["response"] = (
            f"Writer Agent Error: {str(ex)}"
        )

        return state
