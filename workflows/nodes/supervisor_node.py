import re


def supervisor_node(state):

    query = (
        state
        .get("user_query", "")
        .lower()
        .strip()
    )

    # Reset tool information
    state["tool_name"] = None
    state["tool_params"] = {}

    # ==========================================
    # WRITE OPERATIONS
    # ==========================================

    if "book" in query:

        state["intent"] = "WRITE"
        state["tool_name"] = "book_appointment"

        # Expected example:
        # book appointment patient 00018 slot S001

        patient_match = re.search(
            r"patient\s+([a-zA-Z0-9_-]+)",
            query
        )

        slot_match = re.search(
            r"slot\s+([a-zA-Z0-9_-]+)",
            query
        )

        if patient_match:
            state["tool_params"]["patient_id"] = (
                patient_match.group(1)
            )

        if slot_match:
            state["tool_params"]["slot_id"] = (
                slot_match.group(1)
            )

        return state

    if "cancel" in query:

        state["intent"] = "WRITE"
        state["tool_name"] = "cancel_appointment"

        # Example:
        # cancel appointment A001

        match = re.search(
            r"(?:appointment\s+)?([a-zA-Z0-9_-]+)$",
            query
        )

        if match:
            state["tool_params"]["appointment_id"] = (
                match.group(1)
            )

        return state

    # ==========================================
    # READER - DOCTORS
    # ==========================================

    if (
        "list of doctors" in query
        or "list doctors" in query
        or query in ["doctor", "doctors"]
    ):

        state["intent"] = "READ"
        state["tool_name"] = "get_doctors"

        return state

    # ==========================================
    # READER - AVAILABLE SLOTS
    # ==========================================

    if (
        "available slots" in query
        or "availability" in query
    ):

        state["intent"] = "READ"
        state["tool_name"] = "get_availability"

        return state

    # ==========================================
    # READER - PATIENT DETAILS
    # ==========================================

    if "patient details" in query:

        state["intent"] = "READ"
        state["tool_name"] = "get_patient_details"

        # Supports:
        # patient details 00018
        # patient details of 00018
        # patient details for 00018

        match = re.search(
            r"patient\s+details"
            r"(?:\s+(?:of|for))?"
            r"\s+([a-zA-Z0-9_-]+)",
            query
        )

        if match:
            state["tool_params"]["patient_id"] = (
                match.group(1)
            )

        return state

    # ==========================================
    # READER - PATIENT APPOINTMENTS
    # ==========================================

    if "appointments for" in query:

        state["intent"] = "READ"
        state["tool_name"] = (
            "get_patient_appointments"
        )

        match = re.search(
            r"appointments\s+for\s+"
            r"([a-zA-Z0-9_-]+)",
            query
        )

        if match:
            state["tool_params"]["patient_id"] = (
                match.group(1)
            )

        return state

    # ==========================================
    # READER - APPOINTMENT DETAILS
    # ==========================================

    if (
        "appointment" in query
        and "details" in query
    ):

        state["intent"] = "READ"
        state["tool_name"] = (
            "get_appointment_details"
        )

        match = re.search(
            r"appointment\s+details"
            r"(?:\s+(?:of|for))?"
            r"\s+([a-zA-Z0-9_-]+)",
            query
        )

        if match:
            state["tool_params"]["appointment_id"] = (
                match.group(1)
            )

        return state

    # ==========================================
    # READER - SLOT CHECK
    # ==========================================

    if (
        "slot" in query
        and "check" in query
    ):

        state["intent"] = "READ"
        state["tool_name"] = (
            "check_slot_availability"
        )

        match = re.search(
            r"slot\s+([a-zA-Z0-9_-]+)",
            query
        )

        if match:
            state["tool_params"]["slot_id"] = (
                match.group(1)
            )

        return state

    # ==========================================
    # DEFAULT → MEDICAL
    # ==========================================

    state["intent"] = "MEDICAL"

    return state