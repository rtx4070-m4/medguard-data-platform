
import pandas as pd

class MIMICLoader:

    def __init__(self,path="data/mimic"):
        self.path=path

    def load(self):
        patients=pd.read_csv(f"{self.path}/PATIENTS.csv")
        admissions=pd.read_csv(f"{self.path}/ADMISSIONS.csv")

        df=patients.merge(admissions,on="SUBJECT_ID")
        return df
