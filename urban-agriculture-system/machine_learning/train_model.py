import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load your rain prediction dataset
# Assuming a CSV file with columns: humidity, temperature, rain
data = pd.read_csv("rain_prediction_data.csv")

# Split the data into features (X) and target variable (y)
X_rain = data[['humidity', 'temperature']]
y_rain = data['rain']

# Split the data into training and testing sets
X_train_rain, X_test_rain, y_train_rain, y_test_rain = train_test_split(X_rain, y_rain, test_size=0.2, random_state=42)

# Create a Random Forest Classifier model
rain_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rain_model.fit(X_train_rain, y_train_rain)

# Make predictions on the testing set
predictions_rain = rain_model.predict(X_test_rain)

# Evaluate the model
accuracy = accuracy_score(y_test_rain, predictions_rain)
print(f"Rain Prediction Accuracy: {accuracy}")

# Save the trained rain prediction model
joblib.dump(rain_model, 'rain_prediction_model.joblib')
