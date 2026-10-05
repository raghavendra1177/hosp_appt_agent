import streamlit as st

from workflows.hospital_graph import (
    hospital_graph
)


st.set_page_config(
    page_title="Agentic Hospital Booking System",
    page_icon="🏥",
    layout="wide"
)

st.title(
    "🏥 Agentic Hospital Booking System"
)

st.caption(
    "LangGraph + OpenAI + Multi-Agent Architecture"
)


# -------------------------------
# Chat History
# -------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# -------------------------------
# Display Chat History
# -------------------------------

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):
        st.markdown(
            message["content"]
        )


# -------------------------------
# User Input
# -------------------------------

user_query = st.chat_input(
    "Ask about appointments, slots, "
    "patients, doctors, or medical information..."
)


if user_query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_query
        }
    )

    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                # -----------------------
                # Initial LangGraph State
                # -----------------------

                state = {
                    "user_query": user_query,
                    "intent": "",
                    "tool_name": None,
                    "tool_params": {},
                    "tool_output": {},
                    "response": "",
                    "sources": []
                }

                # -----------------------
                # Always invoke graph
                # -----------------------

                result = (
                    hospital_graph.invoke(
                        state
                    )
                )

                response_text = ""

                # -----------------------
                # Agent Response
                # -----------------------

                if result.get("response"):

                    response_text += (
                        "### Response\n\n"
                        f"{result['response']}\n\n"
                    )

                # -----------------------
                # Tool Output
                # -----------------------

                if result.get("tool_output"):

                    response_text += (
                        "### Tool Output\n\n"
                    )

                    response_text += (
                        "```json\n"
                        f"{result['tool_output']}\n"
                        "```\n\n"
                    )

                # -----------------------
                # Sources
                # -----------------------

                if result.get("sources"):

                    response_text += (
                        "### Sources\n\n"
                    )

                    for source in result["sources"]:
                        response_text += (
                            f"- {source}\n"
                        )

                if not response_text:

                    response_text = (
                        "No response generated."
                    )

                st.markdown(
                    response_text
                )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response_text
                    }
                )

            except Exception as ex:

                error_message = (
                    f"❌ Error: {str(ex)}"
                )

                st.error(
                    error_message
                )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message
                    }
                )