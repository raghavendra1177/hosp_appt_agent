import pandas as pd


class PatientTools:

    def __init__(
        self,
        patients_file="data/patients.csv"
    ):
        self.patients_file = patients_file

    def get_patient_details(
        self,
        patient_id: str
    ):

        df = pd.read_csv(
            self.patients_file,
            dtype=str
        )

        result = df[
            df["patient_id"] == patient_id
        ]

        if result.empty:
            return None

        return result.iloc[0].to_dict()

    def list_patients(self):

        df = pd.read_csv(
            self.patients_file,
            dtype=str
        )

        return df.to_dict(
            orient="records"
        )