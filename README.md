
# CompliantCare Enterprise
Regulatory‑First Healthcare Data Platform

Pipeline:
Raw Data → Compliance → De‑identification → FHIR → Warehouse → ML → Dashboard

Supports:
DPDP Act 2023 (India)
HIPAA
GDPR

## Key Components

- FastAPI backend
- Streamlit analytics dashboard
- PostgreSQL clinical warehouse
- FHIR interoperability layer
- ML risk prediction (mortality prediction demo)
- Docker deployment

## Run

docker compose up --build

API:
http://localhost:8000

Dashboard:
http://localhost:8501
