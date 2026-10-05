from workflows.state import HospitalState


def route_intent(state: HospitalState) -> str:
    """
    Route the workflow based on the detected intent.
    """

    intent = state.get("intent", "READ")

    if intent == "WRITE":
        return "writer"

    if intent == "MEDICAL":
        return "medical"

    return "reader"
