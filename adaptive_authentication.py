import time

# Example typing pattern
user_pattern = {"avg_typing_speed": 200}  # Replace with real data for each user

def authenticate_user(input_pattern):
    if abs(input_pattern["avg_typing_speed"] - user_pattern["avg_typing_speed"]) < 50:
        return "User authenticated"
    else:
        return "Authentication required"

# Simulated authentication check
input_pattern = {"avg_typing_speed": 210}  # Replace with dynamic user input
print(authenticate_user(input_pattern))
