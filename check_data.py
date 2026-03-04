from models import db, Threat
from app import app

with app.app_context():
    threats = Threat.query.all()
    if threats:
        for threat in threats:
            print(f"Time: {threat.time}, Type: {threat.threat_type}, Severity: {threat.severity}")
    else:
        print("No data found in 'threat' table.")
