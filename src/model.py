# src/model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

data_path = "data/processed/cleaned_space_missions.csv"

if not os.path.exists(data_path):
    print("❌ Cleaned data not found! Run data_preprocessing.py first.")
else:
    print("✅ Cleaned data loaded successfully!")
    df = pd.read_csv(data_path)

    # Encode target and features
    df = df.dropna(subset=["status_mission"])
    label_encoders = {}

    for col in df.select_dtypes(include=["object"]).columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    # Define features and target
    X = df.drop("status_mission", axis=1)
    y = df["status_mission"]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    print("\n🎯 Accuracy:", accuracy_score(y_test, y_pred))
    print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

    # Save model
    joblib.dump(model, "models/space_mission_model.pkl")
    print("\n✅ Model saved to: models/space_mission_model.pkl")
