from app import db, app  # Ensure 'app' is the Flask application instance

# Flask application context mein database create karna
with app.app_context():
    db.create_all()
    print("Tables created successfully!")
