from langgraph.graph import (
    StateGraph,
    END
)

from workflows.state import (
    HospitalState
)

from workflows.router import (
    route_intent
)

from workflows.nodes.supervisor_node import (
    supervisor_node
)

from workflows.nodes.reader_node import (
    reader_node
)

from workflows.nodes.writer_node import (
    writer_node
)

from workflows.nodes.medical_node import (
    medical_node
)


graph = StateGraph(
    HospitalState
)

graph.add_node(
    "supervisor",
    supervisor_node
)

graph.add_node(
    "reader",
    reader_node
)

graph.add_node(
    "writer",
    writer_node
)

graph.add_node(
    "medical",
    medical_node
)

graph.set_entry_point(
    "supervisor"
)

graph.add_conditional_edges(
    "supervisor",
    route_intent,
    {
        "READ": "reader",
        "WRITE": "writer",
        "MEDICAL": "medical"
    }
)

graph.add_edge(
    "reader",
    END
)

graph.add_edge(
    "writer",
    END
)

graph.add_edge(
    "medical",
    END
)

hospital_graph = graph.compile()