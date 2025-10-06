import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# File path (relative to src folder)
file_path = "../data/processed/cleaned_space_missions.csv"

# Check if file exists
if not os.path.exists(file_path):
    print("❌ Processed data file not found! Run data_preprocessing.py first.")
    exit()

# Load data
df = pd.read_csv(file_path)
print("✅ Data loaded for EDA!")
print(df.head(), "\n")

# --- Basic Info ---
print("📊 Dataset Info:")
print(df.info(), "\n")

print("📈 Missing Values:")
print(df.isnull().sum(), "\n")

# --- Top Companies by Mission Count ---
top_companies = df['company_name'].value_counts().head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_companies.values, y=top_companies.index, palette="viridis")
plt.title("Top 10 Companies by Number of Missions")
plt.xlabel("Number of Missions")
plt.ylabel("Company Name")
plt.tight_layout()
plt.show()

# --- Mission Success Rate ---
mission_status = df['status_mission'].value_counts()
plt.figure(figsize=(6, 4))
sns.barplot(x=mission_status.index, y=mission_status.values, palette="coolwarm")
plt.title("Mission Success vs Failure Count")
plt.xlabel("Mission Status")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# --- Rocket Status Count ---
plt.figure(figsize=(6, 4))
sns.countplot(y=df['status_rocket'], palette="mako")
plt.title("Rocket Status Distribution")
plt.tight_layout()
plt.show()

print("✅ EDA completed successfully!")
