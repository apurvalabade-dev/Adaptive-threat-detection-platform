import numpy as np
import pandas as pd
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

# Define the file path
file_path = r"C:\Adaptive_Cyber_Defense\network_activity.csv"

# Check if the file exists
if not os.path.exists(file_path):
    print("File does not exist. Please check the path:", file_path)
else:
    # Load the dataset
    data = pd.read_csv(file_path)

    # Select numeric columns only and handle non-numeric data
    numeric_data = data.select_dtypes(include=[np.number])

    # Preprocess the data: handle infinite and NaN values
    numeric_data = numeric_data.replace([np.inf, -np.inf], np.nan)  # Replace infinity with NaN
    numeric_data = numeric_data.dropna()  # Drop rows with NaN values

    # Scale the data
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(numeric_data).astype(np.float32)  # Use float32 to reduce memory usage

    # Prepare data for LSTM using a smaller time_step
    X, y = [], []
    time_steps = 3  # Further reduced time steps for faster processing
    for i in range(time_steps, len(data_scaled)):
        X.append(data_scaled[i-time_steps:i])
        y.append(data_scaled[i, 0])  # Ensure this is the correct target column index

    X, y = np.array(X), np.array(y)

    # Build the LSTM model with Input layer
    model = Sequential()
    model.add(Input(shape=(X.shape[1], X.shape[2])))
    model.add(LSTM(units=20, return_sequences=True))  # Reduced units to 20
    model.add(LSTM(units=20))  # Reduced units to 20
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model with fewer epochs and smaller batch size
    model.fit(X, y, epochs=2, batch_size=4, verbose=1)  # Reduced epochs to 2 and batch size to 4

    # Anomaly detection based on reconstruction error
    y_pred = model.predict(X)
    errors = np.abs(y_pred.flatten() - y)  # Calculate absolute error
    threshold = 0.01  # Adjust this based on model performance

    # Detect anomalies where error exceeds threshold
    anomalies = errors > threshold
    anomaly_indices = np.where(anomalies)[0]  # Get indices of anomalies

    print("Anomalies detected at indices:", anomaly_indices)
