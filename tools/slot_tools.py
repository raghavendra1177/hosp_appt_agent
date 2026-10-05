import pandas as pd


class SlotTools:

    def __init__(
        self,
        slots_file="data/slots.csv"
    ):
        self.slots_file = slots_file

    def get_availability(self):

        df = pd.read_csv(
            self.slots_file,
            dtype=str
        )

        available = df[
            df["is_available"]
            .astype(str)
            .str.lower()
            == "true"
        ]

        return available.to_dict(
            orient="records"
        )

    def check_slot_availability(
        self,
        slot_id
    ):

        df = pd.read_csv(
            self.slots_file,
            dtype=str
        )

        slot = df[
            df["slot_id"] == slot_id
        ]

        if slot.empty:
            return False

        return (
            str(
                slot.iloc[0][
                    "is_available"
                ]
            ).lower()
            == "true"
        )

    def get_available_slots_by_date(
        self,
        appointment_date
    ):

        df = pd.read_csv(
            self.slots_file,
            dtype=str
        )

        available = df[
            (
                df[
                    "appointment_date"
                ]
                ==
                appointment_date
            )
            &
            (
                df[
                    "is_available"
                ]
                .str.lower()
                ==
                "true"
            )
        ]

        return available.to_dict(
            orient="records"
        )