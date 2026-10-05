import pandas as pd
from pathlib import Path


class WriterTools:

    def __init__(
        self,
        appointments_file="data/appointments.csv",
        slots_file="data/slots.csv"
    ):

        self.appointments_file = appointments_file
        self.slots_file = slots_file

    def _load_appointments(self):

        return pd.read_csv(
            self.appointments_file,
            dtype=str
        )

    def _load_slots(self):

        return pd.read_csv(
            self.slots_file,
            dtype=str
        )

    def book_appointment(
        self,
        patient_id: str,
        slot_id: str
    ):

        appointments = (
            self._load_appointments()
        )

        slots = self._load_slots()

        slot = slots[
            slots["slot_id"] == slot_id
        ]

        if slot.empty:

            return {
                "success": False,
                "message": "Slot not found"
            }

        available = str(
            slot.iloc[0]["is_available"]
        ).lower()

        if available != "true":

            return {
                "success": False,
                "message": "Slot unavailable"
            }

        new_id = str(
            len(appointments) + 1
        ).zfill(8)

        slot_record = slot.iloc[0]

        new_row = {

            "appointment_id": new_id,

            "slot_id": slot_id,

            "scheduling_date":
                pd.Timestamp.now()
                .strftime("%Y-%m-%d"),

            "appointment_date":
                slot_record["appointment_date"],

            "appointment_time":
                slot_record["appointment_time"],

            "scheduling_interval": "",

            "status": "scheduled",

            "check_in_time": "",

            "appointment_duration": "",

            "start_time": "",

            "end_time": "",

            "waiting_time": "",

            "patient_id": patient_id,

            "sex": "",

            "age": "",

            "age_group": ""
        }

        appointments.loc[
            len(appointments)
        ] = new_row

        slots.loc[
            slots["slot_id"] == slot_id,
            "is_available"
        ] = "False"

        appointments.to_csv(
            self.appointments_file,
            index=False
        )

        slots.to_csv(
            self.slots_file,
            index=False
        )

        return {

            "success": True,

            "appointment_id":
                new_id,

            "patient_id":
                patient_id,

            "slot_id":
                slot_id,

            "message":
                "Appointment booked successfully"
        }

    def cancel_appointment(
        self,
        appointment_id: str
    ):

        appointments = (
            self._load_appointments()
        )

        slots = self._load_slots()

        appointment = appointments[
            appointments[
                "appointment_id"
            ] == appointment_id
        ]

        if appointment.empty:

            return {
                "success": False,
                "message": "Appointment not found"
            }

        slot_id = appointment.iloc[0][
            "slot_id"
        ]

        appointments.loc[
            appointments[
                "appointment_id"
            ] == appointment_id,
            "status"
        ] = "cancelled"

        slots.loc[
            slots["slot_id"] == slot_id,
            "is_available"
        ] = "True"

        appointments.to_csv(
            self.appointments_file,
            index=False
        )

        slots.to_csv(
            self.slots_file,
            index=False
        )

        return {

            "success": True,

            "appointment_id":
                appointment_id,

            "slot_id":
                slot_id,

            "message":
                "Appointment cancelled successfully"
        }

    def reschedule_appointment(
        self,
        appointment_id: str,
        new_slot_id: str
    ):

        appointments = (
            self._load_appointments()
        )

        slots = self._load_slots()

        appointment = appointments[
            appointments[
                "appointment_id"
            ] == appointment_id
        ]

        if appointment.empty:

            return {
                "success": False,
                "message": "Appointment not found"
            }

        old_slot = appointment.iloc[0][
            "slot_id"
        ]

        new_slot = slots[
            slots["slot_id"]
            == new_slot_id
        ]

        if new_slot.empty:

            return {
                "success": False,
                "message": "New slot not found"
            }

        if str(
            new_slot.iloc[0][
                "is_available"
            ]
        ).lower() != "true":

            return {
                "success": False,
                "message": "New slot unavailable"
            }

        appointments.loc[
            appointments[
                "appointment_id"
            ] == appointment_id,
            "slot_id"
        ] = new_slot_id

        appointments.loc[
            appointments[
                "appointment_id"
            ] == appointment_id,
            "appointment_date"
        ] = new_slot.iloc[0][
            "appointment_date"
        ]

        appointments.loc[
            appointments[
                "appointment_id"
            ] == appointment_id,
            "appointment_time"
        ] = new_slot.iloc[0][
            "appointment_time"
        ]

        slots.loc[
            slots["slot_id"]
            == old_slot,
            "is_available"
        ] = "True"

        slots.loc[
            slots["slot_id"]
            == new_slot_id,
            "is_available"
        ] = "False"

        appointments.to_csv(
            self.appointments_file,
            index=False
        )

        slots.to_csv(
            self.slots_file,
            index=False
        )

        return {

            "success": True,

            "appointment_id":
                appointment_id,

            "old_slot":
                old_slot,

            "new_slot":
                new_slot_id,

            "message":
                "Appointment rescheduled successfully"
        }