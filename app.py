from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///threats.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional: Disable modification tracking
db = SQLAlchemy(app)

class Threat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(50))
    threat_type = db.Column(db.String(100))
    severity = db.Column(db.String(50))

    def __repr__(self):
        return f'<Threat {self.threat_type}>'

# Create database tables if they don't exist
with app.app_context():
    db.create_all()

    # Check if there are any threats and add some initial data if none exist
    if Threat.query.count() == 0:  # Only add data if the table is empty
        new_threat1 = Threat(time="2024-11-02 12:00", threat_type="Phishing", severity="High")
        new_threat2 = Threat(time="2024-11-05 08:16:33", threat_type="Malware", severity="Medium")
        
        db.session.add(new_threat1)
        db.session.add(new_threat2)
        db.session.commit()
        print("Initial threats added to the database.")  # Success message

@app.route('/')
def dashboard():
    threats = Threat.query.all()  # Get all threats from the database
    print(f"Retrieved threats: {[threat.threat_type for threat in threats]}")  # Debugging output
    return render_template('dashboard.html', threats=threats)

@app.route('/api/threats')
def api_threats():
    threats = Threat.query.all()  # Get all threats
    return jsonify([{'time': threat.time, 'threat_type': threat.threat_type, 'severity': threat.severity} for threat in threats])

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode
