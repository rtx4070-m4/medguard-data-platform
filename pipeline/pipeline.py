
import pandas as pd
from compliance.compliance_engine import ComplianceEngine
from privacy.deidentify import DeIdentifier

class Pipeline:

    def run(self):

        checker=ComplianceEngine()
        print(checker.export_json())

        df=pd.read_csv("data/sample.csv")

        deid=DeIdentifier()
        if 'notes' in df.columns:
            df['notes']=df['notes'].apply(deid.mask)

        stats={
            "rows":len(df),
            "columns":len(df.columns)
        }

        return stats
