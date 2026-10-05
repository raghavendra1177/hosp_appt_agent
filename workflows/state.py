from typing import Any, Dict, List, Optional, TypedDict


class HospitalState(TypedDict, total=False):
    user_query: str
    intent: str
    tool_name: Optional[str]
    tool_params: Dict[str, Any]
    tool_output: Any
    response: str
    sources: List[str]
