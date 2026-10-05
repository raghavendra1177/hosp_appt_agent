import pandas as pd


class AppointmentTools:

    def __init__(
        self,
        appointments_file=
        "data/appointments.csv"
    ):

        self.appointments_file = (
            appointments_file
        )

    def get_patient_appointments(
        self,
        patient_id
    ):

        df = pd.read_csv(
            self.appointments_file,
            dtype=str
        )

        appointments = df[
            df["patient_id"]
            ==
            patient_id
        ]

        return appointments.to_dict(
            orient="records"
        )

    def get_appointment_details(
        self,
        appointment_id
    ):

        df = pd.read_csv(
            self.appointments_file,
            dtype=str
        )

        appointment = df[
            df["appointment_id"]
            ==
            appointment_id
        ]

        if appointment.empty:
            return None

        return (
            appointment
            .iloc[0]
            .to_dict()
        )

    def get_upcoming_appointments(
        self
    ):

        df = pd.read_csv(
            self.appointments_file,
            dtype=str
        )

        return df[
            df["status"]
            .str.lower()
            ==
            "scheduled"
        ].to_dict(
            orient="records"
        )

    def get_patient_history(
        self,
        patient_id
    ):

        df = pd.read_csv(
            self.appointments_file,
            dtype=str
        )

        history = df[
            df["patient_id"]
            ==
            patient_id
        ]

        return history.to_dict(
            orient="records"
        )
    