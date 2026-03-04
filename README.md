# Adaptive Cyber Defense Using Generative AI for Real-Time Threat Detection and Adaptive Authentication

## 📘 Introduction and Objective
*Title:* Adaptive Cyber Defense Using Generative AI for Real-Time Threat Detection and Adaptive Authentication

*Objective:* 
The goal of this project is to develop a cybersecurity system leveraging Generative AI for real-time threat detection and adaptive user verification.

---

## 📂 Project Structure
The project is organized as follows:

```bash
├── network_activity.csv              # Dataset file
├── anomaly_detection.py              # Anomaly detection module using LSTM
├── phishing_detection.py             # Phishing and malware detection using RandomForest
├── adaptive_authentication.py        # User behavior-based adaptive authentication
├── app.py                            # Flask app for dashboard
├── models.py                         # Database models
├── insert.py                         # Script for data insertion
├── create_table.py                   # Script for creating database tables
├── check_table.py                    # Script to check data in tables
└── templates/
    └── dashboard.html                # HTML template for threat dashboard


#🛠️ Setup Steps
Follow these steps to set up and run the project:

Step 1: Install Packages
Install the required packages:
pip install pandas scikit-learn tensorflow flask flask_s

Step 2: Create Database Tables
Run the following script to create the necessary database tables:
python create_table.py

Step 3: Run the Application
Start the application:
python app.py

📦 Module Descriptions
Each module in this project performs a critical role in ensuring adaptive cybersecurity:
1. Anomaly Detection:
* Implements LSTM (Long Short-Term Memory) networks to identify unusual network activity.
* Capable of real-time processing to detect deviations from typical behavior.

2.Phishing Detection:
* Employs a Random Forest classifier to detect phishing and malware attacks.
* Processes and analyzes synthetic phishing/malware datasets for high accuracy.

3. Adaptive Authentication:
* Verifies users dynamically based on behavioral patterns like typing speed, mouse movements, etc.
* Ensures minimal disruption to genuine users while enhancing security for anomalies.

4. Threat Intelligence Dashboard:
* Displays real-time data on detected threats and anomalies.
* Provides actionable insights for security teams to mitigate risks promptly.


##5. Flowcharts
Flowcharts explaining the project flow are available to give a clear overview of the workflow:

Overall Project Workflow
Threat Intelligence Dashboard-Wireframe
Anomaly Detection Process
Phishing Detection Process
Adaptive Authentication Process




