from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Threat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(50))
    threat_type = db.Column(db.String(100))
    severity = db.Column(db.String(50))

    def __repr__(self):
        return f'<Threat {self.threat_type}>'
