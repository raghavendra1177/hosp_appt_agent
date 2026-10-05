from tools.patient_tools import PatientTools
from tools.slot_tools import SlotTools
from tools.appointment_tools import AppointmentTools
#rom tools.doctor_tools import DoctorTools


class ReaderAgent:

    def __init__(self):
        self.patient_tools = PatientTools()
        self.slot_tools = SlotTools()
        self.appointment_tools = AppointmentTools()
        #elf.doctor_tools = DoctorTools()

    def execute(self, tool_name, **kwargs):
        tools = {
            "get_availability":
                self.slot_tools.get_availability,

            "check_slot_availability":
                self.slot_tools.check_slot_availability,

            "get_available_slots_by_date":
                self.slot_tools.get_available_slots_by_date,

            "get_patient_details":
                self.patient_tools.get_patient_details,

            "list_patients":
                self.patient_tools.list_patients,

            "get_patient_appointments":
                self.appointment_tools.get_patient_appointments,

            "get_appointment_details":
                self.appointment_tools.get_appointment_details,

            "get_upcoming_appointments":
                self.appointment_tools.get_upcoming_appointments,

            "get_patient_history":
                self.appointment_tools.get_patient_history,

            # "list_doctors":
            #     self.doctor_tools.list_doctors,
        }

        if tool_name not in tools:
            raise Exception(f"Unknown tool {tool_name}")

        return tools[tool_name](**kwargs)
