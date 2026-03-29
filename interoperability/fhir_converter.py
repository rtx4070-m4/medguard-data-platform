
class FHIRConverter:

    def patient_resource(self,row):
        return {
            "resourceType":"Patient",
            "id":str(row.patient_id),
            "gender":row.gender
        }
