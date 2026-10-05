from typing import Any, Dict

from agents.reader_agent import ReaderAgent


reader_agent = ReaderAgent()


def reader_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Execute the Reader Agent tool and store the result in the workflow state.
    """

    try:
        tool_name = state.get("tool_name")

        if not tool_name:
            raise ValueError("tool_name missing from state")

        tool_params = state.get("tool_params", {})

        if not isinstance(tool_params, dict):
            raise ValueError("tool_params must be a dictionary")

        result = reader_agent.execute(
            tool_name,
            **tool_params
        )

        state["tool_output"] = result
        state["response"] = (
            f"Reader tool '{tool_name}' executed successfully."
        )

        return state

    except Exception as ex:
        state["tool_output"] = {}
        state["response"] = f"Reader Agent Error: {str(ex)}"

        return state
