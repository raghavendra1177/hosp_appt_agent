from tools.writer_tools import WriterTools


class WriterAgent:

    def __init__(self):

        self.writer_tools = WriterTools()

    def execute(
        self,
        tool_name: str,
        **kwargs
    ):
        """
        Executes a writer tool.

        Supported Tools:
        ----------------
        book_appointment
        cancel_appointment
        reschedule_appointment
        """

        tools = {

            "book_appointment":
                self.writer_tools.book_appointment,

            "cancel_appointment":
                self.writer_tools.cancel_appointment,

            "reschedule_appointment":
                self.writer_tools.reschedule_appointment
        }

        if tool_name not in tools:

            raise ValueError(
                f"Unsupported writer tool: {tool_name}"
            )

        return tools[tool_name](**kwargs)