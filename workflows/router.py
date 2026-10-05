from workflows.state import HospitalState


def route_intent(state: HospitalState) -> str:
    """
    Route the workflow based on the detected intent.

    The returned values must match the keys used by
    graph.add_conditional_edges() in hospital_graph.py.
    """

    intent = state.get("intent", "READ")

    if intent == "WRITE":
        return "WRITE"

    if intent == "MEDICAL":
        return "MEDICAL"

    return "READ"
