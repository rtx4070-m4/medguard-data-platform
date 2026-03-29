
import json

class ComplianceEngine:

    def checklist(self):
        return {
            "DPDP_India":[
                "Consent captured",
                "Purpose limitation",
                "Data fiduciary registered"
            ],
            "HIPAA":[
                "Safe Harbor applied",
                "Risk assessment completed"
            ],
            "GDPR":[
                "Lawful basis defined",
                "DPO assigned"
            ]
        }

    def export_json(self):
        return json.dumps(self.checklist(), indent=2)
