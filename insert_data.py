from app import app, db, Threat  # Adjust the import based on your file structure

with app.app_context():
    # Clear existing data (optional)
    db.drop_all()
    db.create_all()

    # Adding multiple threats
    new_threat1 = Threat(time="2024-11-02 12:00", threat_type="Phishing", severity="High")
    new_threat2 = Threat(time="2024-11-05 08:16:33", threat_type="Malware", severity="Medium")
    
    db.session.add(new_threat1)
    db.session.add(new_threat2)
    db.session.commit()
    
    print("New threats added successfully!")  # Success message
